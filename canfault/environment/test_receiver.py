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
    
    def test_correct(self):
        self.ch.write(self.framefactory.create_random_frame())
        self.receiver.receive()
    
    def test_correct_duplicate(self):
        self.ch.write(self.framefactory.create_random_frame())
        self.receiver.receive(func = duplicate) 
    
    def test_init(self):
        fault = "INCORRECT"
        self.assertRaises(TypeError, receiver.Receiver, fault)

    def test_faulty_arguments_func(self):
        self.assertRaises(TypeError, self.receiver.receive, func = [1, "hej"])

    def test_faulty_arguments_params(self):
        self.assertRaises(TypeError, self.receiver.receive, params = 1)

    def tearDown(self) -> None:
        self.ch.busOff()
        self.ch.close()
        self.ch1.busOff()
        self.ch1.close()

if __name__ == '__main__':  # pragma: no cover
    import framefactory
    import receiver
    from faultfunctions import duplicate

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
    from faultfunctions.duplicate import duplicate
