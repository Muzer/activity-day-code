#!/usr/bin/env python2

from sr import *
import move

import time

match_length = 2 * 60
start_time = time.clock()

R = Robot()
move.forward(R, 2)

def match_running():
    match_time = time.clock() - start_time

    return match_time < match_length
