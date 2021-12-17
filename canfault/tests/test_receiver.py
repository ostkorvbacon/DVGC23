import unittest
from canlib import canlib
from main import setUpChannel
from environment import framefactory
from environment import receiver
from faultfunctions import faultfunction


class TestReceiver(unittest.TestCase):
    
    """Tests the environment.receiver function."""
    
    def setUp(self) -> None:
        self.ch = setUpChannel()
        self.ch1 = setUpChannel(1)
        self.receiver = receiver.Receiver(self.ch1)
        self.framefactory = framefactory.FrameFactory()

    def test_receive(self):
        self.assertIsNotNone(self.receiver)

    def test_correct(self):
        self.ch.write(self.framefactory.create_random_frame())
        self.receiver.receive()

    def test_correct_duplicate(self):
        self.ch.write(self.framefactory.create_random_frame())
        self.receiver.receive(func=faultfunction.duplicate)

    def test_init(self):
        fault = "INCORRECT"
        self.assertRaises(TypeError, receiver.Receiver, fault)

    def test_faulty_arguments_func(self):
        self.assertRaises(TypeError, self.receiver.receive, func=[1, "hej"])

    def test_faulty_arguments_params(self):
        self.assertRaises(TypeError, self.receiver.receive, params=1)

    def tearDown(self) -> None:
        self.ch.busOff()
        self.ch.close()
        self.ch1.busOff()
        self.ch1.close()
