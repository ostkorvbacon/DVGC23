from canlib import canlib, Frame
import random

class FrameFactory:
    """Creates Frames with random IDs between 0 and 1023 and data between 0 and 255, returns the Frame"""
    def __init__(self):
        self.min = 0
        self.max = 255
        self.data_amount = 8

    def create_random_frame(self):
        """Creates Frames with random IDs and data, returns the Frame"""
        random.seed()
        data = []
        for _ in range(self.data_amount):
           datapoint = random.randint(self.min, self.max)
           data.append(datapoint)
        frame = Frame(id_ = random.randint(0, 1023), data = data, flags = canlib.MessageFlag.EXT)

        return frame

    def create_frames(self, number_of_frames):
        """Creates a set of Frames with random data and IDs, returnes the set as a list"""
        if not isinstance(number_of_frames, int):
            raise(TypeError("number_of_frames needs to be an int"))
        frames = []
        for _ in range(number_of_frames):
            frames.append(self.create_random_frame())
        
        return frames