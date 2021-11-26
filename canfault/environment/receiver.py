from typing import List
import canlib
from readwrite import readfault
from canlib import Frame
from . import printframe

"""Handles the reception of messages on the supplied channel"""
class Receiver:
    def __init__(self, channel):
        if not isinstance(channel, canlib.canlib.channel.Channel):
            raise(TypeError("Object passed to receiver must be a canlib channel"))
        else:
            self.channel = channel

    """Print the content of the frame"""
    def receive(self, func = None, params = []):
        frame = readfault.read(channel=self.channel, func=func, params=params)
        while frame is not None:
            print("Receiving:")
            if isinstance(frame, List):
                for i in frame:
                    printframe.print_frame(i)
            else:
                printframe.print_frame(frame)
            frame = readfault.read(channel=self.channel, func=func, params=params)
