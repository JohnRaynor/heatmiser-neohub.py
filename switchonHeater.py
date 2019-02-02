#!/usr/bin/env python3
## switchonHeater.py

import asyncio
import sys
import argparse
import json
import logging
import socket
import os
from neohub import NeoHub, NeoDevice


def main():
    os.environ.setdefault("NEOHUB_IP","192.168.5.162")
    host = os.environ.get("NEOHUB_IP")
    if host is None:
        print("Please set the NEOHUB_IP environment variable")
        print("eg: NEOHUB_IP=\'192.168.0.123\'")
        sys.exit(1)
    loop = asyncio.get_event_loop()
    neo = NeoHub(host, 4242)
    print (await neo.neoplugs())[args[0]].switch_on()
    print (neo.neoplugs())
    for name in neo.neoplugs():
        ns = neo.neoplugs()[name]
        print(repr(ns))
    return 0
 



if __name__ == '__main__':
    main()
    
