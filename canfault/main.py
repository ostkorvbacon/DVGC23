from canlib import canlib, Frame
from canlib.canlib import ChannelData
from environment import transciever, receiver, demo, messagefactory, database
import logging


def setUpChannel(channel=0,
                 openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_500K,
                 bitrateFlags=canlib.canDRIVER_NORMAL):
    logging.debug("Start")
    """Sets up a Channel, returns the channel.

    :param channel: channel number, defaults to 0
    :type channel: int, optional
    :param openFlags: flags to set when opening the channel,
    defaults to canlib.canOPEN_ACCEPT_VIRTUAL
    :type openFlags: unsigned int *, optional
    :param bitrate: bitrate of the channel, defaults to canlib.canBITRATE_500K
    :type bitrate: int, optional
    :param bitrateFlags: flags for the bitrate,
    defaults to canlib.canDRIVER_NORMAL
    :type bitrateFlags: int, optional

    :rtype: canlib.channel.Channel
    :return: ch
    """
    ch = canlib.openChannel(channel, openFlags)
    ch.setBusOutputControl(bitrateFlags)
    ch.setBusParams(bitrate)
    ch.busOn()
    logging.debug("End")
    return ch


def tearDownChannel(ch):
    logging.debug("Start")
    """Closes the provided canlib.channel.Channel."""
    ch.busOff()
    ch.close()
    logging.debug("End")

if __name__ == '__main__':
    """Setting up logger"""
    logging.basicConfig(filename='logging.log', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s %(filename)s.%(funcName)s - %(message)s',
                        datefmt='%Y/%m/%d %I:%M')

    """Runs the setup for demo and runs the demo."""
    channel_transmit = setUpChannel(channel=0)
    channel_receive = setUpChannel(channel=1)
    database = database.Database()

    transceiver = transciever.Transceiver(channel_transmit)
    receiver = receiver.Receiver(channel_receive)
    demo = demo.Demo(transceiver, receiver)

    demo.demo_all(1)

    tearDownChannel(channel_transmit)
    tearDownChannel(channel_receive)

    database.add_number_of_items(num=10)
    database.print_db()
