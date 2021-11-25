import unittest

from canlib import canlib
from main import setUpChannel

class TestReceiver(unittest.TestCase):
    def setUp(self) -> None:
        self.ch = setUpChannel()
        self.ch1 = setUpChannel()
        self.receiver = receiver.Receiver(self.ch1)
        self.framefactory = framefactory.FrameFactory()

    def test_receive(self):
        self.assertIsNotNone(self.receiver)
    
    def test_receiver_correct(self):
        self.ch.write(self.framefactory.create_random_frame())
        self.receiver.receive()
        self.ch.busOff()
        self.ch.close()
        self.ch1.busOff()
        self.ch1.close()
    
    def test_receiver_init(self):
        fault = "INCORRECT"
        self.assertRaises(TypeError, receiver.Receiver, fault)

if __name__ == '__main__':  # pragma: no cover
    import framefactory
    import receiver

    def setUpChannel():
        def setUpChannel(channel=0,
                 openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_500K,
                 bitrateFlags=canlib.canDRIVER_NORMAL):

            ch = canlib.openChannel(channel, openFlags)
            ch.setBusOutputControl(bitrateFlags)
            ch.setBusParams(bitrate)
            ch.busOn()
            return ch

    unittest.main()
else:
    from environment import framefactory
    from environment import receiver
