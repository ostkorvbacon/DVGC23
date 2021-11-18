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
    
    channel_transmit = setUpChannel(channel=0)
    channel_receive = setUpChannel(channel = 1)

    transceiver = transciever.Transceiver(channel_transmit)
    receiver = receiver.Receiver(channel_receive)

    transceiver.transmit()
    receiver.receive()

    tearDownChannel(channel_transmit)
    tearDownChannel(channel_receive)
