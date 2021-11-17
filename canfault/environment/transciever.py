
from readwrite import canwritefault
import framefactory

class Transceiver:
    def __init__(self):
        self.factory

    """Specify the number of frames to be created and transmitted over the channel"""
    def transmit(self, number_of_frames):
        frames = self.factory.create_frames(number_of_frames)
        for f in frames:
            print("Transmitting frame\n")
            return f