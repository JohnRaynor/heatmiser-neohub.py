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

    cmd = "switch_on"

    args = 'Greenhouse'
    #retval = loop.run_until_complete(main(neo, cmd, args))
    retval = loop.run_until_complete(main(neo, cmd, args))
    loop.close()
    sys.exit(retval)
 



if __name__ == '__main__':
    main()
    
