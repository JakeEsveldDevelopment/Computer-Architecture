#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load("../LS8/examples/call.ls8")
cpu.run()