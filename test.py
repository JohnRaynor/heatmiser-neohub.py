#!/usr/bin/env python3
import asyncio
import sys
import argparse
import json
import logging
import socket
import os
from neohub import NeoHub, NeoDevice
from SwitchPlugs import SwitchOn, SwitchOff

SwitchOn('House Plug')
