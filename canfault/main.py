from canlib import canlib, Frame
from canlib.canlib import ChannelData
from environment import transciever, receiver
from faultfunctions import corrupt, duplicate
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


if __name__ == '__main__':

    ch = setUpChannel(channel=0)
    ch1 = setUpChannel(channel = 1)
    ch.write(transceiver.transmit(1))
    corrupt.corrupt_frame(ch1.read())
    tearDownChannel(ch)
    tearDownChannel(ch1)
