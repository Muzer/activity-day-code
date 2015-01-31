import time


def forward(R, time):
    R.motors[0].m0.power = 100
    R.motors[0].m1.power = 100
    time.sleep(time)

def distance_to_time(distance):

    return distance