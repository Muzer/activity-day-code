import time

LEFT_CORRECTION = 1
RIGHT_CORRECTION = 1

DEGREES_PER_SECOND = 90
DISTANCE_PER_SECOND = 1 #meters

TURNING_POWER = 30

'''
ASCII art of the diagram

           0 m[1].m0
          z z
         z   z
m[0].m1 0-----0 m[0].m1

'''

def forward(R, time):
    R.motors[0].m0.power = 100 * LEFT_CORRECTION
    R.motors[0].m1.power = 100 * RIGHT_CORRECTION
    time.sleep(time)

    stop_all_motors(R)

def stop_all_motors(R):
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0
    R.motors[1].m0.power = 0

def slowly_stop_all_motors(R):
    i = R.motors[0].m0.power
    while i > 0:
        R.motors[0].m0.power = i
        R.motors[0].m1.power = i
        R.motors[1].m0.power = i

        i -= 1

def left(R, degrees):
    R.motors[0].m0.power = TURNING_POWER
    R.motors[0].m1.power = TURNING_POWER
    R.motors[1].m0.power = TURNING_POWER
    time.sleep(abs(degrees / DEGREES_PER_SECOND))

    stop_all_motors(R)

def right(R, degrees):
    left(R, -degrees)

def distance_to_time(distance):
    return (distance / DISTANCE_PER_SECOND)