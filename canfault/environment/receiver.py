import canlib
from canfault.faultfunctions.corrupt import corrupt_frame
from readwrite import canreadfault
from canlib import Frame

class Receiver:
    def __init__(self, channel):
        self.channel = channel

    def receive():
        frame = self.ch.read()
        print("Receiving\n")
        print(frame)
        #canreadfault()
        print("Corrupting to:\n")
        print(corrupt_frame(frame))
        #print(frame)
