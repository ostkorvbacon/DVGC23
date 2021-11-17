from canlib import canlib, Frame
from canlib.canlib import ChannelData

def corrupt_frame(frame):
    print(frame)
    #print(dir(frame))
    print(frame.data)
    frame.data = "derp"
    print(frame)
