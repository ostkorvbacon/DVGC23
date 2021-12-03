from typing import Callable, List
import canlib
from readwrite import readfault
from canlib import Frame
from . import printframe


class Receiver:
    """Handles the reception of messages on the supplied channel, prints the messages"""
    def __init__(self, channel):
        if not isinstance(channel, canlib.canlib.channel.Channel):
            raise(TypeError("Object passed to receiver must be a canlib channel"))
        else:
            self.channel = channel

    def receive(self, func = None, params = []):
        """Prints the content of the frame"""
        if func is not None and not isinstance(func, Callable):
            raise(TypeError("Object func passed to receive needs to be a Callable"))
        if not isinstance(params, List):
            raise(TypeError("Object params passed to receive needs to be a List of parameters"))
        
        frame = readfault.read(channel=self.channel, func=func, params=params)
        while frame is not None:
            print("Receiving:")
            if isinstance(frame, List):
                for i in frame:
                    printframe.print_frame(i)
            else:
                printframe.print_frame(frame)
            frame = readfault.read(channel=self.channel, func=func, params=params)
