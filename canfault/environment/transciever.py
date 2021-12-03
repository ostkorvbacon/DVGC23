from faultfunctions import faultfunction
from readwrite import writefault
from . import framefactory
from . import printframe
from typing import Callable, List

class Transceiver:
    def __init__(self, channel):
        """Handles the transmission of messages on the supplied channel
    
        :param channel: Channel in which to write and inject faults.
        :type channel: canlib.channel.Channel
        """
        self.channel = channel
        self.factory = framefactory.FrameFactory()

    def transmit(self, func = None, params = []):
        """Transmit a random frame over the channel. Optionally supply faultfunction. Print the result.
        
        :param func: A faultfunction in which to send the frame. Defaults to None.
        :type func: Callable
        :param params: Parameters to be passed to the fault function. Defaults to []
        :type params: List
        """
        if func is not None and not isinstance(func, Callable):
            raise(TypeError("Object func passed to transmit needs to be a Callable"))
        if not isinstance(params, List):
            raise(TypeError("Object params passed to transmit needs to be a List of parameters"))

        frame = self.factory.create_random_frame()
        print("Transmitting:")
        printframe.print_frame(frame)
        writefault.write(self.channel, frame, func, params)

