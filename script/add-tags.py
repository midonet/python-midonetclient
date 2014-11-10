#!/usr/bin/env python

from midonetclient.api import MidonetApi


def main():
    mn_uri = 'http://localhost:8081'
    my_laptop = 'c1b9eb8a-c83b-43d3-b7b8-8613f921dbe7'
    mc = MidonetApi(mn_uri, 'admin', 'password')

    bridges = mc.get_bridges({'tenant_id': my_laptop})
    bridge = bridges[0]
    bridge.add_tag().tag("tomohiko_tag1").create()
    bridge.add_tag().tag("tomohiko_tag2").create()

if __name__ == '__main__':
    main()
