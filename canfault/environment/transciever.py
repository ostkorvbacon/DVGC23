
from faultfunctions import duplicate
from readwrite import CanWriteFault
from . import framefactory

class Transceiver:
    def __init__(self, channel):
        self.channel = channel
        self.factory = framefactory.FrameFactory()

    """Transmit a random frame over the channel"""
    def transmit(self):
        frame = self.factory.create_random_frame()
        print("Frame {} being transmitted\n".format(frame))
        CanWriteFault.write(self.channel, duplicate.duplicate, frame)
