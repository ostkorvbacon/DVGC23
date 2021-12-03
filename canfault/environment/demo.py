import time
from . import transciever
from faultfunctions import faultfunction

class Demo:
    """Contains functions for demoing each of the faultinjection methods.

        :param transceiver: A handle to a transceiver object to send faultfunctions on write.
        :type transceiver: environment.Transceiver
        :param receiver: A handle to a receiver object to send faultfunctions on read.
        :type receiver: environment.Receiver
    """
    def __init__(self, transceiver, receiver):
        self.transceiver = transceiver
        self.receiver = receiver

    def demo_write_swap(self):
        """Demo swap on write."""
        self.transceiver.transmit(faultfunction.swap)
        self.transceiver.transmit(faultfunction.swap)

    def demo_write_duplicate(self):
        """Demo duplicate on write."""
        self.transceiver.transmit(faultfunction.duplicate)

    def demo_write_corrupt(self):
        """Demo corrupt on write."""
        params = [3, 10]
        self.transceiver.transmit(faultfunction.corrupt, params)

    def demo_write_delay(self):
        """Demo delay on write."""
        print("Transmitting at time: {}".format(time.time()))
        self.transceiver.transmit(func = faultfunction.delay, params = [1])

    def demo_write_insert(self):
        """Demo insert on write."""
        self.transceiver.transmit(func=faultfunction.insert)

    def demo_read_swap(self):
        """Demo swap on read."""
        self.receiver.receive(faultfunction.swap)
        self.receiver.receive(faultfunction.swap)

    def demo_read_duplicate(self):
        """Demo duplicate on read."""
        self.receiver.receive(func=faultfunction.duplicate)

    def demo_read_corrupt(self):
        """Demo corrupt on read."""
        params = [3, 10]
        self.receiver.receive(faultfunction.corrupt, params)

    def demo_read_delay(self):
        """Demo delay on read."""
        self.receiver.receive(func = faultfunction.delay, params = [1])
        print("Received at time: {}".format(time.time()))

    def demo_read_insert(self):
        """Demo insert on read."""
        self.receiver.receive(func=faultfunction.insert)

    def demo_all(self, iterations = 1):
        """Demo all faultfunctions on both read and write a specified number of times.
        
        :param iterations: Number of times to run the demo of all faultfunctions. Defaults to 1.
        :type iterations: int
        """
        for _ in range(0, iterations):
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

            print("-----------Insert------------")
            self.demo_write_insert()
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

            print("----------Insert-----------")
            self.transceiver.transmit()
            self.demo_read_insert()

            print("_________________________________________End demo_________________________________________\n")
