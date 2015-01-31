import move
import time

# All strategies are a separate function


def basic(R):

    pass


def charge_and_swerve(R):

    move.forward_dist(R, 0.8)
    move.slowly_stop_all_motors(R)
    move.scoop_left(R, 130)

    move.forward_dist(R, 1.2)


def charge_and_swerve_F_minus(R):
    center_marker = 32

    if R.zone == 0: # Zone A
        close_marker = 33
        far_marker = 34
    else: # Zone B
        close_marker = 34
        far_marker = 33

    move.forward_dist(R, 0.9)
    move.slowly_stop_all_motors(R)
    move.scoop_left(R, 130)


    can_see_marker = False

    time.sleep(3)
    markers = R.see()
    print "I see", len(markers)
    for marker in markers:
        print marker.info.code, marker.dist
        if marker.info.code == far_marker: # The marker in the opposite zone
            # move towards marker
            move.forward(R, marker.dist)
            can_see_marker = True

    if not can_see_marker:
        print("Cannot see")

    #move.forward_dist(R, 2)
