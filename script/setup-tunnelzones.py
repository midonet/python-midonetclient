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

    tz1 = mc.add_tunnel_zone()
    tz1.name('tomohiko')
    tz1.type('gre')
    tz1.create()

if __name__ == '__main__':
    main()
