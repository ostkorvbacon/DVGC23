import CanReadFault
import CanWriteFault
from canlib import canlib, Frame
from canlib.canlib import ChannelData
import tracemalloc

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
    CanWriteFault.write(channel1, CanWriteFault.do_nothing, frame)
    print("Reading on channel!")
    CanReadFault.read(channel0, print)
    tearDownChannel(channel0)
    tearDownChannel(channel1)


main()
