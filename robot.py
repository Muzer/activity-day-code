#!/usr/bin/env python2
import move
import strategy
import time
from sr import *

R = Robot()

MATCH_LENGTH = 2 * 60
start_time = time.clock()

def match_running():
    match_time = time.clock() - start_time

    return match_time < MATCH_LENGTH

center_marker = 32

if R.zone == 0: # Zone A
    close_marker = 33
    far_marker = 34
else: # Zone B
    close_marker = 34
    far_marker = 33

"""while match_running():
    markers = R.see()

    can_see_marker = False

    for marker in markers:
        if marker.info.code == far_marker: # The marker in the opposite zone
            # move towards marker
            move.forward(R, marker.dist)

            can_see_marker = True


    if not can_see_marker:
        print("Cannot see")
"""

def calibrate():

    forward_dist(2)

    print("Done")

calibrate()
