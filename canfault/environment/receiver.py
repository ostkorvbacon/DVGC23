import canlib
from readwrite import CanReadFault
from canlib import Frame

class Receiver:
    def __init__(self, channel):
        self.channel = channel

    """Print the content of the frame"""
    def receive(self):
        frame = CanReadFault.read(self.channel)
        while frame is not None:
            print("Receiving:\n")
            print(frame)
            print("\n")
            frame = CanReadFault.read(self.channel)
