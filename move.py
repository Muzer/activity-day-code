import time

LEFT_CORRECTION = 1
RIGHT_CORRECTION = 0.91

FRONT_TURN_CORRECTION = -1
LEFT_TURN_CORRECTION = 1
RIGHT_TURN_CORRECTION = 1

DEGREES_PER_SECOND = 210.0
DISTANCE_PER_SECOND = 0.95 # meters per second

TURNING_POWER = 70.0

SPEED = 80.0

'''
ASCII art of the diagram

           0 m[1].m0
          z z
         z   z
m[0].m1 0-----0 m[0].m0

'''

def forward(R, t):
    R.motors[0].m0.power = SPEED * RIGHT_CORRECTION
    R.motors[0].m1.power = -SPEED * LEFT_CORRECTION
    time.sleep(t)

    stop_all_motors(R)

def forward_dist(R, dist):
    forward(R, distance_to_time(dist))

def stop_all_motors(R):
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    R.motors[1].m0.power = 0

def slowly_stop_all_motors(R):
    print "Slowly ramping down"
    R.motors[0].m0.use_break = False
    R.motors[0].m1.use_break = False

    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    time.sleep(0.3)

    R.motors[0].m0.use_break = True
    R.motors[0].m1.use_break = True

def left(R, degrees):
    R.motors[0].m0.power = TURNING_POWER * RIGHT_TURN_CORRECTION
    R.motors[0].m1.power = TURNING_POWER * LEFT_TURN_CORRECTION
    R.motors[1].m0.power = TURNING_POWER * FRONT_TURN_CORRECTION
    time.sleep(abs(degrees / DEGREES_PER_SECOND))

    stop_all_motors(R)

def scoop_left(R, degrees):
    R.motors[0].m0.power = TURNING_POWER * RIGHT_TURN_CORRECTION
    R.motors[1].m0.power = TURNING_POWER * FRONT_TURN_CORRECTION
    time.sleep(abs(degrees / DEGREES_PER_SECOND))

    stop_all_motors(R)

def scoop_right(R, degrees):
    R.motors[0].m1.power = TURNING_POWER * LEFT_TURN_CORRECTION
    R.motors[1].m0.power = TURNING_POWER * FRONT_TURN_CORRECTION
    time.sleep(abs(degrees / DEGREES_PER_SECOND))

    stop_all_motors(R)


def right(R, degrees):
    left(R, -degrees)

def distance_to_time(distance):
    return (distance / DISTANCE_PER_SECOND)


