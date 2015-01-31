import move
import strategy
import time
#import ultrasound
from sr.robot import *

#R = Robot.setup()
#R.ruggeduino_set_handler_by_fwver("SRus", ultrasound.USRuggeduino)
#R.init()
#R.wait_start()
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

def calibrate():

    move.forward_dist(R, 2)

    print("Done")

#print R.ruggeduinos[0].distance()
#calibrate()
#strategy.charge_and_swerve_F_minus(R)
strategy.charge_and_swerve(R)



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
