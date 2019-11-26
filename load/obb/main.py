# from twisted.internet import epollreactor
# epollreactor.install()
from io import IOBase
import core
import sys
import json
import time
import math
import click
import threading
import logging
import urllib
from datetime import datetime
from twisted.internet import reactor, defer, task
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent, readBody
from twisted.web.http_headers import Headers

from zope.interface import implementer

from twisted.internet.defer import succeed
from twisted.web.iweb import IBodyProducer

from typing import List

STATE_REQUEST = 0
STATE_REQUESTED = 1
STATE_RESPONSE = 2
STATE_SUCCEEDED = 3
STATE_FAILDED = 4

class RequestContext:
    
    index = 0
    connected_at = None
    requested_at = None
    body_readed_at = None
    state = STATE_REQUEST
    data = None
    behaviour = None

    def __init__(self, index, context):
        self.index = index
        self.context = context
        if context:
            self.behaviour = context.behaviour_class(index)

    def succeed(self):
        self.context.done += 1
        self.context.succeeded += 1
        self.state = STATE_SUCCEEDED

        self.is_done()

    def is_done(self):
        if self.context.done == self.context.requests:
            reactor.stop()
            load_done(self.context)

    def fail(self):
        self.context.done += 1
        self.context.failed += 1
        self.state = STATE_FAILDED

        self.is_done()

class RequestContextList:

    size: int = 0
    sequence: int = 0
    request_contexts: List[RequestContext] = []

    def __init__(self, size: int):
        self.size = size

    def alloc(self) -> RequestContext:
        rc = RequestContext(sequence, None)
        self.sequence += 1
        return rc

    def push(self, request_context: RequestContext):
        self.request_contexts.append(request_context)

    def pop(self, timeout=1.0) -> RequestContext:
        while True:
            if len(self.request_contexts) == 0:
                time.sleep(1)
                continue
            
            out = self.request_contexts[0]
            del self.request_contexts[0]

            return out

    def is_full(self) -> bool:
        return self.size == self.sequence + 1


class CSVReporter(threading.Thread):
    """
    >>> import io
    >>> rcs = RequestContextList(1)
    >>> rc = RequestContext(0, None)
    >>> rc.body_readed_at = datetime.now()
    >>> rc.connected_at = datetime.now()
    >>> rc.responsed_at = datetime.now()
    >>> rcs.push(rc)
    >>> output = io.StringIO()
    >>> reporter = CSVReporter(rcs, output)
    >>> reporter.quiting = True
    >>> reporter.run()
    >>> len(output.getvalue()) > 0
    True
    """

    quiting: bool = False
    request_context_list: List[RequestContext]
    output: IOBase = None

    def __init__(self, request_context_list: List[RequestContext], output):
        super().__init__()
        self.request_context_list = request_context_list
        self.output = output

    def run(self):
        while True:
            rc = self.request_context_list.pop()
            logging.debug('test')

            try:
                resposne_datetime = rc.body_readed_at - rc.connected_at
                output = "%s,%s,%s,%s,%s\n" % (datetime_split(rc.responsed_at) \
                    + datetime_split(rc.body_readed_at) +
                    (resposne_datetime.seconds + resposne_datetime.microseconds / 1000 / 1000,)
                    )
            except Exception as e:
                raise e
                continue
            
            self.output.write(output)
            self.output.flush()

            if self.quiting:
                break

    def quit(self):
        self.quiting = True

class ApplicationLifecycle:
    def quit(self):
        pass

@implementer(IBodyProducer)
class BytesProducer(object):
    def __init__(self, body):
        self.body = str.encode(body)
        self.length = len(body)

    def startProducing(self, consumer):
        consumer.write(self.body)
        return succeed(None)

    def pauseProducing(self):
        pass

    def stopProducing(self):
        pass

done = 0
launched = 0
request_index = 0

def datetime_split(dt):
    responsed_at_date = dt.strftime("%Y-%m-%d")
    responsed_at_time = "%s.%d" % (dt.time().strftime("%H:%M:%S"), 
        dt.time().microsecond / 1000)

    return (responsed_at_date, responsed_at_time)

def load_done(context):
    pass

class Context:
    requests = 1
    rate = 1
    launched = 0
    request_index = 0
    launch_total = 0
    done = 0
    succeeded = 0
    failed = 0
    startup_at = 0


agent = Agent(reactor)

class ReadBodyProtocol(Protocol):
    request_context = None
    derfer = None
    size = 0

    def __init__(self, request_context, defer):
        self.request_context = request_context
        self.defer = defer

    def dataReceived(self, data):
        self.size += len(data)

    def connectionLost(self, reason):
        self.request_context.body_readed_at = datetime.now()
        self.request_context.succeed()
        self.defer.callback(None)

def callbackCancel():
    print("cancel")

def callbackRequestError(err, request_context):
    logging.debug(err)
    request_context.fail()
    pass

def callbackResponseSuccess(response, request_context):
    request_context.responsed_at = datetime.now()
    d = defer.Deferred(callbackCancel)
    response.deliverBody(ReadBodyProtocol(request_context, d))

    return d

def request(request_context):
    request_context.connected_at = datetime.now()

    byte = None
    if request_context.data:
        byte = BytesProducer(request_context.data)

    behaviour = request_context.behaviour
    if hasattr(behaviour, 'data'):
        data = behaviour.data()

        if isinstance(data, dict):
            data = json.dumps(data)

        byte = BytesProducer(data)

    method = 'GET'
    if hasattr(behaviour, 'method'):
        method = behaviour.method()
    
    headers = {'User-Agent': ['Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0']}
    if hasattr(behaviour, 'headers'):
        headers.update(behaviour.headers())

    d = agent.request(
        str.encode(method),
        b'http://127.0.0.1:5001/form/mysql',
        Headers(headers),
        byte)

    d.addCallbacks(callbackResponseSuccess, \
        callbackRequestError, \
        callbackArgs=[request_context], \
        errbackArgs=[request_context]
    )


class HttpRequest:
    def do(self, rc: RequestContext):
        pass

class MotherShip:
    launched: int = 0
    total: int = 0
    concurrency: int = 0

    def __init__(self, concurrency: int, requests: int):
        self.concurrency = concurrency
        self.total = math.ceil(requests / concurrency)

    def fly(self):
        pass

    def launch(self):
        """
        >>> ms = MotherShip(10, 10)
        >>> reactor.run()
        """
        
        self.launched += 1
        start = time.time()
        for i in range(self.concurrency):
            reactor.callLater(1 / self.concurrency, self.fly, *[self.request_context_list.alloc()])
        end = time.time()
        next_schedule = (end - start)

        if self.launched < self.total:
            reactor.callLater(next_schedule, self.launch)


class ReactorTest:
    def test(self):
        """
        >>> def stop():
        ...     reactor.stop()
        >>> deplayed_call = reactor.callLater(0.1, stop)
        >>> reactor.run()
        >>> True
        True
        """
        pass

def launch(context):
    context.launched += 1
    start = time.time()
    
    for i in range(context.concurrency):
        reactor.callLater((1 / context.concurrency) * i, request, *[context.request_context_list.alloc()])
    end = time.time()
    next_schedule = (end - start)
    if context.launched < context.launch_total:
        reactor.callLater(next_schedule, launch, *[context])


def monitor(context):
    report = "Duration %d seconds, done %d succeeded %d failed %d" % (time.time() - context.startup_at, context.done, context.succeeded, context.failed)
    print(report)

@click.command()
@click.argument('url', default=None)
@click.option('-c', '--concurrency', default=1, help='Number of multiple requests to perform at a time. Default is one request at a time.')
@click.option('-f', '--file')
@click.option('-n', '--requests', help='Number of requests to perform for the benchmarking session. The default is to just perform a single request which usually leads to non-representative benchmarking results.')
@click.option('-t', '--timelimit')
@click.option('-h', '--header')
@click.option('-d', '--data')
@click.option('--debug', default=False)
@click.option('--csv', default=None)
def bench(url=None, concurrency=1, file=None, requests=1, timelimit=0, header={}, data=None, debug=False, csv=None):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    behaviour_module = __import__("submit")

    context = Context()
    context.startup_at = time.time()
    context.requests = int(requests)
    context.concurrency = int(concurrency)
    context.url = url
    context.data = data
    context.launch_total = (context.requests / context.concurrency)
    context.behaviour_class = behaviour_module.HttpRequestBehaviour
    context.csv = csv
    context.request_context_list = RequestContextList(context.requests)

    launch(context)

    loop = task.LoopingCall(monitor, *[context])

    loopDeferred = loop.start(1.0)

    reactor.run()

# responsed_at = sum([request_context.body_readed_at - request_context.connected_at for request_context in request_contexts])
# wait_time = sum([request_context.responsed_at - request_context.connected_at for request_context in request_contexts])
# logging.info("Total %.2f" % responsed_at)
# logging.info("Avg wait time %.2f" % (wait_time / float(requests), ))
# logging.info("Avg response time %.2f" % (responsed_at / float(requests)),)

if __name__ == "__main__":
    bench()