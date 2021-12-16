from canlib import canlib, Frame, kvadblib
from canlib.canlib import ChannelData
from canlib.kvadblib import message
from readwrite.writefault import write
from environment import transciever, receiver, demo, messagefactory, framefactory, printframe
from faultfunctions import signalfault
from environment import setupsignal


def setUpChannel(channel=0,
                 openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_500K,
                 bitrateFlags=canlib.canDRIVER_NORMAL):
    """Sets up a Channel, returns the channel.

    :param channel: channel number, defaults to 0
    :type channel: int, optional
    :param openFlags: flags to set when opening the channel, defaults to canlib.canOPEN_ACCEPT_VIRTUAL
    :type openFlags: unsigned int *, optional
    :param bitrate: bitrate of the channel, defaults to canlib.canBITRATE_500K
    :type bitrate: int, optional
    :param bitrateFlags: flags for the bitrate, defaults to canlib.canDRIVER_NORMAL
    :type bitrateFlags: int, optional

    :rtype: canlib.channel.Channel
    :return: ch
    """
    ch = canlib.openChannel(channel, openFlags)
    ch.setBusOutputControl(bitrateFlags)
    ch.setBusParams(bitrate)
    ch.busOn()
    return ch


def tearDownChannel(ch):
    """Closes the provided canlib.channel.Channel."""
    ch.busOff()
    ch.close()

if __name__ == '__main__':
    """Runs the setup for demo and runs the demo."""
    channel_transmit = setUpChannel(channel=0)
    channel_receive = setUpChannel(channel=1)
   
    transceiver = transciever.Transceiver(channel_transmit)
    receiver = receiver.Receiver(channel_receive)
    demo = demo.Demo(transceiver, receiver)
    
    demo.demo_all(1)

    tearDownChannel(channel_transmit)
    tearDownChannel(channel_receive)

    #SIGNAL
    channel_signaltransmit = setUpChannel(channel = 0)
    channel_signalreceive = setUpChannel(channel = 1)

    signalsetup = setupsignal.SetupSignal(10)
    signalsetup.setup()
    signalsetup.signal_transmit(channel_signaltransmit)
    signalsetup.signal_receive(channel_signalreceive)

    tearDownChannel(channel_signaltransmit)
    tearDownChannel(channel_signalreceive)
