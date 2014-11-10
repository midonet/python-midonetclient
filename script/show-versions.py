#!/usr/bin/env python

from midonetclient.api import MidonetApi
import logging

logging.basicConfig(level=logging.DEBUG)

args = {
    'base_uri': "http://localhost:8080/midonet-api",
    'username': 'quantum',
    'password': 'quantum',
    'project_id': 'service',
}


def main():
    # mn_uri = 'http://localhost:8081'
    # mc = MidonetApi(mn_uri, 'admin', 'password')
    mc = MidonetApi(**args)

    hosts = mc.get_host_versions()
    for host in hosts:
        print('host: %s, host_id: %s, version: %s' % (host.get_host(),
                                                      host.get_host_id(),
                                                      host.get_version()))

if __name__ == '__main__':
    main()
