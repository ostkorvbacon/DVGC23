from faultfunctions import duplicate, swap
from readwrite import CanWriteFault
from . import framefactory
from . import printframe

class Transceiver:
    def __init__(self, channel):
        self.channel = channel
        self.factory = framefactory.FrameFactory()

    """Transmit a random frame over the channel"""
    def transmit(self):
        frame = self.factory.create_random_frame()
        #print("Frame being transmitted:")
        #printframe.print_frame(frame)
        #CanWriteFault.write(self.channel, duplicate.duplicate, frame)

        frame2 = self.factory.create_random_frame()
        print("Frame being transmitted:")
        printframe.print_frame(frame)
        CanWriteFault.write(self.channel, swap.swap, frame)
        print("Frame being transmitted:")
        printframe.print_frame(frame2)
        CanWriteFault.write(self.channel, swap.swap, frame2)

