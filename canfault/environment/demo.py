from . import transciever
from faultfunctions import swap, duplicate, delay, corrupt

"""Contains functions for demoing each of the faultinjection methods."""
class Demo:
    def __init__(self, transceiver, receiver):
        self.transceiver = transceiver
        self.receiver = receiver

    def demo_write_swap(self):
        self.transceiver.transmit(swap.swap)
        self.transceiver.transmit(swap.swap)

    def demo_write_duplicate(self):
        self.transceiver.transmit(duplicate.duplicate)

    def demo_write_corrupt(self):
        params = [3, 10]
        self.transceiver.transmit(corrupt.corrupt, params)

    def demo_write_delay(self):
        self.transceiver.transmit(delay.delay)

    def demo_read_swap(self):
        self.receiver.receive(swap.swap)
        self.receiver.receive(swap.swap)

    def demo_read_duplicate(self):
        self.receiver.receive(duplicate.duplicate)

    def demo_read_corrupt(self):
        params = [3, 10]
        self.receiver.receive(corrupt.corrupt, params)

    def demo_read_delay(self):
        self.transceiver.transmit(delay.delay)

    def demo_all(self, iterations = 1):
        for i in range(0, iterations):
            print("\n____________________________")
            print("Faults on write:")
            print("\n--------Demoing swap--------")
            self.demo_write_swap()
            self.receiver.receive()

            print("-----Demoing duplicate------")
            self.demo_write_duplicate()
            self.receiver.receive()

            print("------Demoing corrupt-------")
            self.demo_write_corrupt()
            self.receiver.receive()

            print("-------Demoing delay--------")
            self.demo_write_corrupt()
            self.receiver.receive()

            print("\n____________________________")
            print("Faults on read:")
            print("\n--------Demoing swap--------")
            self.transceiver.transmit()
            self.transceiver.transmit()
            self.demo_read_swap()

            print("-----Demoing duplicate------")
            self.transceiver.transmit()
            self.demo_read_duplicate()

            print("------Demoing corrupt-------")
            self.transceiver.transmit()
            self.demo_read_corrupt()

            print("-------Demoing delay--------")
            self.transceiver.transmit()
            self.demo_read_corrupt()

            print("----------End demo----------\n")
