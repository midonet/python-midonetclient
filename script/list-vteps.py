#!/usr/bin/env python

from midonetclient.api import MidonetApi
import logging

logging.basicConfig(level=logging.DEBUG)

args = {
    'base_uri': "http://127.0.0.1:8080/midonet-api",
    'username': 'quantum',
    'password': 'quantum',
    'project_id': 'service',
}


def main():
    mc = MidonetApi(**args)

    # vtep_management_ip = '119.15.112.22'
    # vtep_management_port = '6633'

    # Create a new VTEP
    # vtep = mc.add_vtep().name('My VTEP')\
    #                     .management_ip(vtep_management_ip)\
    #                     .management_port(vtep_management_port)\
    #                     .create()
    # print 'Created a VTEP.'

    # list VTEPs
    vteps = mc.get_vteps()
    print 'Retrieved a list of %d VTEPs.' % len(vteps)


if __name__ == '__main__':
    main()
