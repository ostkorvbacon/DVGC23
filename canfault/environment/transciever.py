from faultfunctions import faultfunction
from readwrite import writefault
from . import framefactory
from . import printframe
from typing import Callable, List

class Transceiver:
    """Creates a Frame and transmits over the channel, optionally supply faultfunction"""
    def __init__(self, channel):
        self.channel = channel
        self.factory = framefactory.FrameFactory()

    def transmit(self, func = None, params = []):
        """Transmit a random Frame over the channel, optionally supply faultfunction"""
        if func is not None and not isinstance(func, Callable):
            raise(TypeError("Object func passed to transmit needs to be a Callable"))
        if not isinstance(params, List):
            raise(TypeError("Object params passed to transmit needs to be a List of parameters"))

        frame = self.factory.create_random_frame()
        print("Transmitting:")
        printframe.print_frame(frame)
        writefault.write(self.channel, frame, func, params)

