import time

LEFT_CORRECTION = 1
RIGHT_CORRECTION = 1


'''
ASCII art of the diagram

   0 m[1].m0
  / \
 /   \
0-----0 m[0].m1

'''


def forward(R, time):
    R.motors[0].m0.power = 100 * LEFT_CORRECTION
    R.motors[0].m1.power = 100 * RIGHT_CORRECTION
    time.sleep(time)

def distance_to_time(distance):

    return distance