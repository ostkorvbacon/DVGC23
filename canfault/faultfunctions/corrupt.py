from canlib import canlib, Frame
from canlib.canlib import ChannelData

def corrupt_frame(frame):
    print(frame)
    #print(dir(frame))
    frame.data = "derp"
    return frame
