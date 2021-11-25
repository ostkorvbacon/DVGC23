import unittest
import framefactory

class TestFrameFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.framefactory = framefactory.FrameFactory

    def test_create_random_frame(self):
        self.assertIsNotNone(self.framefactory.create_random_frame())

    def test_create_frames(self):
        self.assertIsNotNone(self.framefactory.create_frames(2))

if __name__ == '__main__':
    unittest.main()