import canlib
from readwrite import CanReadFault
from canlib import Frame

class Receiver:
    def __init__(self, channel):
        self.channel = channel

    def receive(self):
        frame = CanReadFault.read()
        print("Receiving:\n")
        print(frame)
        print("\n")
