import click
import json
import urllib.request

@click.command()
@click.argument('url')
@click.option('-c', '--concurrency', default=1, help='Number of multiple requests to perform at a time. Default is one request at a time.')
@click.option('-n', '--requests', help='Number of requests to perform for the benchmarking session. The default is to just perform a single request which usually leads to non-representative benchmarking results.')
@click.option('-h', '--header')
@click.option('-d', '--data')
def bench(url, concurrency, requests, header, data):

    while True:
        request = urllib.request.Request(url, data=data, method='POST')
        request.add_header('Content-Type', "application/json")
        r = urllib.request.urlopen(request)
    
    pass

if __name__ == '__main__':
    bench()