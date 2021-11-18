import tracemalloc
from canlib import canlib, Frame
from canlib.canlib import ChannelData
import sys
sys.path.append("..")

import CanReadFault
import CanWriteFault
from main import setUpChannel, tearDownChannel

def do_nothing(frame, params):
    return frame

def main():
    print("Setting up channel!")
    channel0 = setUpChannel()
    channel1 = setUpChannel(1)
    print("Writing frame!")
    frame = Frame(
        id_=100,
        data=[1, 2, 3, 4],
        flags=canlib.MessageFlag.EXT
    )
    CanWriteFault.write(channel1, do_nothing, frame)
    print("Reading on channel!")
    msg = CanReadFault.read(channel0, do_nothing, params = ["Hej", "hejsan"])
    print(msg)
    tearDownChannel(channel0)
    tearDownChannel(channel1)


main()
