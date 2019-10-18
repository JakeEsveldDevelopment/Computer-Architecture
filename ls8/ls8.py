#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

cpu.load("../LS8/examples/sctest.ls8")
cpu.run()