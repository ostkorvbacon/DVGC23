from . import transciever
from faultfunctions import swap, duplicate, DelayFrames, corrupt

"""Contains functions for demoing each of the faultinjection methods."""
class Demo:
    def __init__(self, transceiver, receiver):
        self.transceiver = transceiver
        self.receiver = receiver

    def demo_swap(self):
        self.transceiver.transmit(swap.swap)
        self.transceiver.transmit(swap.swap)

    def demo_duplicate(self):
        self.transceiver.transmit(duplicate.duplicate)

    def demo_corrupt(self):
        params = [3, 10]
        self.transceiver.transmit(corrupt.corrupt, params)

    def demo_delay(self):
        self.transceiver.transmit(DelayFrames.DelayFrames)

    def demo_all(self, iterations = 1):
        for i in range(0, iterations):
            print("\n--------Demoing swap--------")
            self.demo_swap()
            self.receiver.receive()

            print("-----Demoing duplicate------")
            self.demo_duplicate()
            self.receiver.receive()

<<<<<<< HEAD
        print("-----Demoing corrupt------")
        self.demo_corrupt()
        self.receiver.receive()

        print("----------End demo----------\n")
=======
            print("-----Demoing corrupt------")
            self.demo_corrupt()
            self.receiver.receive()

            print("----------End demo----------\n")
>>>>>>> 3e8c8572417a82ee364a8a7650798b543652bfc7
