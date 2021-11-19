from canlib import canlib, Frame
import random

class FrameFactory:
    def __init__(self, min_value = 0, max_value = 255):
        self.min = min_value
        self.max = max_value
        self.data_amount = 8

    """Create a single frame with random ID and data"""
    def create_random_frame(self):
        random.seed() 
        data = []
        for i in range(0, self.data_amount):
           datapoint = random.randint(self.min, self.max)
           data.append(datapoint)
        print(data)
        frame = Frame(id_ = random.randint(0, 1023), data = data, flags = canlib.MessageFlag.EXT)
        print(bytearray(frame.data))
        return frame

    """Create a set of frames with random data and IDs returned as a list"""
    def create_frames(self, number_of_frames):
        frames = []
        for i in range(0, number_of_frames):
            frames.append(self.create_random_frame(self))
        
        return frames