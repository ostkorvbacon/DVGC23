import canlib
from readwrite import CanReadFault
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
    def receive(self):
        frame = CanReadFault.read(self.channel)
        while frame is not None:
            print("Receiving:")
            printframe.print_frame(frame)
            frame = CanReadFault.read(self.channel)
        print("No more frames\n")
