from canlib import canlib, Frame
import random
from readwrite import canwritefault

def create_random_frame():
    random.seed(0)
    min = 0
    max = 100
    data_amount = 4
    data = []
    for i in range(0, data_amount):
        data.append(random.randint(min, max))
    frame = Frame(id_ = 100, data = data, flags = canlib.MessageFlag.EXT)
    return frame

def create_frames(number_of_frames):
    frames = []
    for i in range(0, number_of_frames):
        frames.append(create_random_frame())
    return frames

def transmit(number_of_frames):
    frames = create_frames(number_of_frames)
    for f in frames:
        print("transmitting\n")
        #canwritefault()