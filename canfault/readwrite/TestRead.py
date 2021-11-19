import tracemalloc
from canlib import canlib, Frame
from canlib.canlib import ChannelData

import CanReadFault
import CanWriteFault
#from faultfunctions.swap import swap

def do_nothing(frame, params):
    return frame

def setUpChannel(channel=0,
        openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
        bitrate=canlib.canBITRATE_500K,
        bitrateFlags=canlib.canDRIVER_NORMAL):

    ch = canlib.openChannel(channel, openFlags)
    print("Using channel: %s, EAN: %s" % (ChannelData(channel).channel_name,
                                          ChannelData(channel).card_upc_no))
    ch.setBusOutputControl(bitrateFlags)
    ch.setBusParams(bitrate)
    ch.busOn()
    return ch

def tearDownChannel(ch):
    ch.busOff()
    ch.close()

def test():
    print("Setting up channel!")
    channel0 = setUpChannel()
    channel1 = setUpChannel(1)
    print("Writing frame!")
    frame = Frame(
        id_=562,
        data=[255, 255, 40, 255, 255],
        flags=canlib.MessageFlag.EXT
    )
    CanWriteFault.write(channel1, do_nothing, frame)
    print("Reading on channel!")
    msg = CanReadFault.read(channel0, do_nothing, params = ["Hej", "hejsan"])
    print(msg)
    print(frame.data[2])
    tearDownChannel(channel0)
    tearDownChannel(channel1)

if __name__ == '__main__':
    test()
