import move

# All strategies are a separate function


def basic(R):

    pass


def charge_and_swerve():

    move.forward_dist(R, 1.7)
    move.slowly_stop_all_motors(R)
    move.scoop_left(R, 90)

    move.forward_dist(R, 2)
