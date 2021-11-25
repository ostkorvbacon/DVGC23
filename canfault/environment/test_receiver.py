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
    
    def test_receiver(self):
        
        self.ch.write(self.framefactory.create_random_frame())
        self.receiver.receive()
        self.ch.busOff()
        self.ch.close()
        self.ch1.busOff()
        self.ch1.close()

if __name__ == '__main__':
    import framefactory
    import receiver
    unittest.main()
else:
    from environment import framefactory
    from environment import receiver
