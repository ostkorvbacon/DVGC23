from faultfunctions import duplicate, swap
from readwrite import CanWriteFault
from . import framefactory
from . import printframe

class Transceiver:
    def __init__(self, channel):
        self.channel = channel
        self.factory = framefactory.FrameFactory()

    """Transmit a random frame over the channel, optionally supply faultfunction"""
    def transmit(self, func = None, params = []):
        frame = self.factory.create_random_frame()
        print("Transmitting:")
        printframe.print_frame(frame)
        CanWriteFault.write(self.channel, func, frame, params)

