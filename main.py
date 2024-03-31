import json

import requests

from task01.ip_extractor import IpExtractor
from task01.ip_geolocation import IpGeolocation
from task01.trace_route import TraceRoute


def main():
    trace_router = TraceRoute('5.189.17.8')
    trace_router_output = trace_router.execute()
    for ip in IpExtractor(trace_router_output).extract():
        print(IpGeolocation.get_info(ip))


if __name__ == '__main__':
    main()
