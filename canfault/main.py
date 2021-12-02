from canlib import canlib, Frame
from canlib.canlib import ChannelData
from environment import transciever, receiver, demo, messagefactory, database

def setUpChannel(channel=0,
                 openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_500K,
                 bitrateFlags=canlib.canDRIVER_NORMAL):

    ch = canlib.openChannel(channel, openFlags)
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
    database = database.Database()

    transceiver = transciever.Transceiver(channel_transmit)
    receiver = receiver.Receiver(channel_receive)
    demo = demo.Demo(transceiver, receiver)

    demo.demo_all(1)

    tearDownChannel(channel_transmit)
    tearDownChannel(channel_receive)

    database.add_number_of_items(num = 10)
    database.print_db()
