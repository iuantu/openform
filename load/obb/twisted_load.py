from twisted.internet import epollreactor
epollreactor.install()

import time
import click
import logging
from twisted.internet import reactor, defer
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent, readBody
from twisted.web.http_headers import Headers

logging.basicConfig(level=logging.DEBUG)

requests = 3000
rate = 2000
done = 0
launched = 0
request_index = 0

STATE_REQUEST = 0
STATE_REQUESTED = 1
STATE_RESPONSE = 2
STATE_DONE = 3
STATE_ERROR = 4

class RequestContext:
    
    index = 0
    connect_time = 0.0
    requested_time = 0.0
    response_time = 0.0
    read_body_time = 0.0
    state = STATE_REQUEST

    def __init__(self, index):
        self.index = index


    def done(self):
        global done
        done += 1
        self.state = STATE_DONE

        self.is_done()

    def is_done(self):
        if done == requests:
            reactor.stop()

    def error(self):
        global done
        done += 1
        self.state = STATE_ERROR

        self.is_done()

contexts = [RequestContext(i) for i in range(requests)]

agent = Agent(reactor)

class ReadBodyProtocol(Protocol):
    context = None
    derfer = None
    size = 0

    def __init__(self, context, defer):
        self.context = context
        self.defer = defer

    def dataReceived(self, data):
        self.size += len(data)

    def connectionLost(self, reason):
        self.context.read_body_time = time.time()
        self.context.done()
        self.defer.callback(None)

def callbackCancel():
    print("cancel")

pdbed = False

def callbackRequestError(err, context):
    global pdbed
    if not pdbed:
        
        pdbed = not pdbed
        import pdb; pdb.set_trace()
    logging.error(err)
    context.error()
    pass

def callbackResponseSuccess(response, context):
    context.response_time = time.time()
    d = defer.Deferred(callbackCancel)
    response.deliverBody(ReadBodyProtocol(context, d))

    return d

def request(context):
    global done
    context.connect_time = time.time()
    d = agent.request(
        b'GET',
        b'http://127.0.0.1/',
        Headers({'User-Agent': ['Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0']}),
        None)

    d.addCallbacks(callbackResponseSuccess, callbackRequestError, callbackArgs=[context], errbackArgs=[context])

launch_total = requests / rate
def launch():
    global launched, request_index
    launched += 1

    logging.info("launch %d " % launched)

    start = time.time()
    
    for i in range(rate):
        context = contexts[request_index]
        request_index += 1
        reactor.callLater((1 / rate) * i, request, *[context])
    end = time.time()
    next_schedule = 1# - (end - start)

    if launched < launch_total:
        reactor.callLater(next_schedule, launch)

launch()

@click.command()
@click.argument('url')
@click.option('-c', '--concurrency', default=1, help='Number of multiple requests to perform at a time. Default is one request at a time.')
@click.option('-n', '--requests', help='Number of requests to perform for the benchmarking session. The default is to just perform a single request which usually leads to non-representative benchmarking results.')
@click.option('-h', '--header')
@click.option('-d', '--data')
def bench(url, concurrency, requests, header, data):

reactor.run()

response_time = sum([context.read_body_time - context.connect_time for context in contexts])
wait_time = sum([context.response_time - context.connect_time for context in contexts])
# logging.info("Total %.2f" % response_time)
# logging.info("Avg wait time %.2f" % (wait_time / float(requests), ))
logging.info("Avg response time %.2f" % (response_time / float(requests)),)