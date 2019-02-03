#!/usr/bin/env python3
import asyncio
import sys
import argparse
import json
import logging
import socket
import os
from neohub import NeoHub, NeoDevice


logging.basicConfig(level=logging.DEBUG)


def ok(what):
    if what:
        return 0
    else:
        print(repr(what))
        return 1

async def main(neo, cmd, args):
    await neo.async_setup()

    if cmd == "switch_on":
        return (await neo.neoplugs())[args[0]].switch_on()

    if cmd == "switch_off":
        return (await neo.neoplugs())[args[0]].switch_off()

    if cmd == "list":
        for name in neo.neostats():
            ns = neo.neostats()[name]
            print(repr(ns))
        print("")
        for name in neo.neoplugs():
            ns = neo.neoplugs()[name]
            print(repr(ns))
        return 0

    if cmd == "list-stats":
        for name in neo.neostats():
            ns = neo.neostats()[name]
            print(repr(ns))
        return 0

    if cmd == "list-plugs":
        for name in neo.neoplugs():
            ns = neo.neoplugs()[name]
            print (neo.neoplugs())
            print( neo.neoplugs)
            #print (ns)
            #print(repr(ns))
        return 0
    return 1

if __name__ == '__main__':
    os.environ.setdefault("NEOHUB_IP","192.168.5.162")
    host = os.environ.get("NEOHUB_IP")
    if host is None:
        print("Please set the NEOHUB_IP environment variable")
        print("eg: NEOHUB_IP=\"192.168.0.123\" %s ..." % sys.argv[0])
        sys.exit(1)

    loop = asyncio.get_event_loop()
    neo = NeoHub(host, 4242)

    cmd = "list-plugs"
    args = ""
    #cmd = "switch-on"
    #args = 'Greenhouse'

##    cmd = sys.argv[1]
##    args = sys.argv[2:]
    retval = loop.run_until_complete(main(neo, cmd, args))
    loop.close()
    sys.exit(retval)

