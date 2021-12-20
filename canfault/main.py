from typing import List
from faultfunctions import faultfunction
from canlib import canlib, Frame, kvadblib
from canlib.canlib import ChannelData
from canlib.kvadblib import message
from readwrite.writefault import write
from readwrite.readfault import read
from environment import transciever, receiver
from environment import demo, messagefactory, framefactory, printframe
from faultfunctions import signalfault
from environment import setupsignal
import logging
import threading
from time import sleep


class CanRxThread(threading.Thread):
    def __init__(self, channel, demo, test_case):
        threading.Thread.__init__(self)
        self._running = True
        self._ch = channel
        self._test_case = test_case
        self._demo = demo

    def stop(self):
        self._running = False

    def receive(self, func=None, params=[]):
        frame = read(channel=self._ch, func=func, params=params)
        print("Received:")
        if isinstance(frame, Frame):
            printframe.print_frame(frame)
        elif isinstance(frame, List):
            for f in frame:
                printframe.print_frame(f)

    def run(self):
        if(self._test_case == "write"):
            while self._running:
                try:
                    frame = read(self._ch)
                    print("Reading from loop")
                    printframe.print_frame(frame)
                except Exception:
                    print("Timeout error")
        elif(self._test_case == "read"):
            print("-----------------------Read--------------------------------")
            print("Duplicate...")
            self.receive(func=faultfunction.duplicate)
            sleep(0.050)
            print("Corrupt...")
            self.receive(func=faultfunction.corrupt, params=[3, 10])
            sleep(0.050)
            print("Drop...")
            self.receive(func=faultfunction.drop)
            sleep(0.050)
            print("Insert...")
            self.receive(func=faultfunction.insert)
            sleep(0.050)
            print("Swap...")
            self.receive(func=faultfunction.swap)
            self.receive(func=faultfunction.swap)
            sleep(0.050)
            print("Delay...")
            self.receive(func=faultfunction.delay)
            sleep(1)
            self._running = False


class CanTxThread(threading.Thread):
    def __init__(self, channel, demo, test_case):
        threading.Thread.__init__(self)
        self._running = True
        self._ch = channel
        self._demo = demo
        self._test_case = test_case

    def stop(self):
        self._running = False

    def run(self):
        if(self._test_case == "write"):
            print("Duplicate...")
            self._demo.demo_write_duplicate()
            sleep(0.050)
            print("Corrupt...")
            self._demo.demo_write_corrupt()
            sleep(0.050)
            print("Drop...")
            self._demo.demo_write_drop()
            sleep(0.050)
            print("Insert...")
            self._demo.demo_write_insert()
            sleep(0.050)
            print("Swap...")
            self._demo.demo_write_swap()
            sleep(0.050)
            print("Delay...")
            self._demo.demo_write_delay()
            sleep(1)
        elif(self._test_case == "read"):
            while(self._running):
                demo.transceiver.transmit()
                sleep(1)


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

    transceiver = transciever.Transceiver(channel_transmit)
    receiver = receiver.Receiver(channel_receive)
    demo = demo.Demo(transceiver, receiver)

    # Testing write
    # Setup reader
    rx_thread = CanRxThread(channel_receive, demo, "write")
    rx_thread.start()

    # Setup writer
    tx_thread = CanTxThread(channel_transmit, demo, "write")
    tx_thread.start()

    sleep(5)

    rx_thread.stop()
    tx_thread.stop()
    rx_thread.join()
    tx_thread.join()
    # Testing read
    # Setup reader
    rx_thread = CanRxThread(channel_receive, demo, "read")
    rx_thread.start()

    # Setup writer
    tx_thread = CanTxThread(channel_transmit, demo, "read")
    tx_thread.start()

    sleep(20)

    rx_thread.stop()
    tx_thread.stop()

    tearDownChannel(channel_transmit)
    tearDownChannel(channel_receive)

    # SIGNAL
    channel_signaltransmit = setUpChannel(channel=0)
    channel_signalreceive = setUpChannel(channel=1)

    # signalsetup = setupsignal.SetupSignal(10)
    # signalsetup.setup()
    # signalsetup.signal_transmit(channel_signaltransmit, channel_signalreceive)
    # signalsetup.signal_receive(channel_signalreceive, channel_signaltransmit)

    tearDownChannel(channel_signaltransmit)
    tearDownChannel(channel_signalreceive)
