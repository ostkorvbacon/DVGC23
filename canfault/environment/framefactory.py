from canlib import canlib, Frame
import random

class FrameFactory:
    """Class for creating and returning frames with randomized IDs and data."""
    def __init__(self):
        self.min = 0
        self.max = 255
        self.data_amount = 8

    def create_random_frame(self):
        """Create a single frame with random ID and data.

        :return: frame
        :rtype: canlib.Frame
        """
        random.seed()
        data = []
        for _ in range(self.data_amount):
           datapoint = random.randint(self.min, self.max)
           data.append(datapoint)

        frame = Frame(id_=random.randint(0, 1023), data=data, dlc=8, flags=canlib.MessageFlag.EXT)
        
        return frame

    def create_frames(self, number_of_frames):
        """Create a set of frames with random data and IDs returned as a list
        
        param number_of_frames: number of frames to be created
        type number_of_frames: int

        :return: [canlib.Frame]
        :rtype: List
        """
        if not isinstance(number_of_frames, int):
            raise(TypeError("number_of_frames needs to be an int"))
        frames = []
        for _ in range(number_of_frames):
            frames.append(self.create_random_frame())
        
        return frames