from canlib import canlib, Frame
from canlib.canlib import ChannelData
from environment import transciever, receiver
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
    ch.write(transciever.create_random_frame())
    print("Read: {}", format(ch1.read()))
    tearDownChannel(ch)
