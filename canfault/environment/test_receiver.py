import unittest
from canfault.environment import framefactory
import receiver
from canlib import canlib

class TestReceiver(unittest.TestCase):
    def setUp(self) -> None:
        self.receiver = receiver.Receiver
        self.framefactory = framefactory.FrameFactory

    def test_receive(self):
        self.assertIsNotNone(self.receiver)
    
    def test_receiver(self):
        ch = canlib.openChannel(channel= 0, openFlags = canlib.canOPEN_ACCEPT_VIRTUAL)
        ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
        ch.setBusParams(canlib.canBITRATE_500K)
        ch.busOn()
        ch.write(self.framefactory.create_random_frame())
        self.receiver.receive()
        ch.busOff()
        ch.close()

if __name__ == '__main__':
    unittest.main()