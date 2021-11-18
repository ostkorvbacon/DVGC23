import canlib
from faultfunctions import corrupt
from readwrite import CanReadFault
from canlib import Frame

class Receiver:
    def __init__(self, channel):
        self.channel = channel

    def receive(self):
        frame = self.channel.read()
        print("Receiving\n")
        print(frame)
        #canreadfault()
        print("Corrupting to:\n")
        print(corrupt.corrupt_frame(frame))
        #print(frame)
