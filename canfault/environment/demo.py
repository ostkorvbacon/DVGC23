import time
from . import transciever
from faultfunctions import faultfunction
#import faultfunction
"""Contains functions for demoing each of the faultinjection methods."""
class Demo:
    def __init__(self, transceiver, receiver):
        self.transceiver = transceiver
        self.receiver = receiver

    def demo_write_swap(self):
        self.transceiver.transmit(faultfunction.swap)
        self.transceiver.transmit(faultfunction.swap)

    def demo_write_duplicate(self):
        self.transceiver.transmit(faultfunction.duplicate)

    def demo_write_corrupt(self):
        params = [3, 10]
        self.transceiver.transmit(faultfunction.corrupt, params)

    def demo_write_delay(self):
        print("Transmitting at time: {}".format(time.time()))
        self.transceiver.transmit(func = faultfunction.delay, params = [1])

    def demo_read_swap(self):
        self.receiver.receive(faultfunction.swap)
        self.receiver.receive(faultfunction.swap)

    def demo_read_duplicate(self):
        self.receiver.receive(func=faultfunction.duplicate)

    def demo_read_corrupt(self):
        params = [3, 10]
        self.receiver.receive(faultfunction.corrupt, params)

    def demo_read_delay(self):
        self.receiver.receive(func = faultfunction.delay, params = [1])
        print("Received at time: {}".format(time.time()))

    def demo_all(self, iterations = 1):
        for i in range(0, iterations):
            print("\n________________________________________Start demo________________________________________")
            print("\n------------------------------------------------------------------------------------------")
            print("Faults on write:")
            print("------------------------------------------------------------------------------------------")

            print("\n-------------Swap------------")
            self.demo_write_swap()
            self.receiver.receive()

            print("----------Duplicate-----------")
            self.demo_write_duplicate()
            self.receiver.receive()

            print("-----------Corrupt------------")
            self.demo_write_corrupt()
            self.receiver.receive()

            print("-----------Delay------------")
            self.demo_write_delay()
            print("Received at time: {}".format(time.time()))
            self.receiver.receive()

            print("\n------------------------------------------------------------------------------------------")
            print("Faults on read:")
            print("------------------------------------------------------------------------------------------")
            print("\n------------Swap------------")
            self.transceiver.transmit()
            self.transceiver.transmit()
            self.demo_read_swap()

            print("---------Duplicate-----------")
            self.transceiver.transmit()
            self.demo_read_duplicate()

            print("----------Corrupt-----------")
            self.transceiver.transmit()
            self.demo_read_corrupt()

            print("-----------Delay------------")
            print("Transmitting at time: {}".format(time.time()))
            self.transceiver.transmit()
            self.demo_read_delay()

            print("_________________________________________End demo_________________________________________\n")
