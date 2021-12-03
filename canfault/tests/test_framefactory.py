import unittest
from environment import framefactory

class TestFrameFactory(unittest.TestCase):
    """Tests the environment.frameFactory function."""
    def setUp(self) -> None:
        self.framefactory = framefactory.FrameFactory()

    def test_create_random_frame(self):
        self.assertIsNotNone(self.framefactory.create_random_frame())

    def test_create_frames(self):
        self.assertIsNotNone(self.framefactory.create_frames(2))
    
    def test_create_frames_input(self):
        self.assertRaises(TypeError, self.framefactory.create_frames, "NNNNNNNN")