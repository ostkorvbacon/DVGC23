from canlib import canlib, Frame
import random

"""Class for creating and returning frames with randomized IDs and data"""
class FrameFactory:
    def __init__(self):
        self.min = 0
        self.max = 255
        self.data_amount = 8

    """Create a single frame with random ID and data"""
    def create_random_frame(self):
        random.seed() 
        data = []
        for i in range(0, self.data_amount):
           datapoint = random.randint(self.min, self.max)
           data.append(datapoint)
        print("Creating frame with data: {}".format(data))
        frame = Frame(id_ = random.randint(0, 1023), data = data, flags = canlib.MessageFlag.EXT)
        return frame

    """Create a set of frames with random data and IDs returned as a list"""
    def create_frames(self, number_of_frames):
        frames = []
        for i in range(0, number_of_frames):
            frames.append(self.create_random_frame(self))
        
        return frames