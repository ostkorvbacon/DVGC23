import unittest

class TestFrameFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.framefactory = framefactory.FrameFactory()

    def test_create_random_frame(self):
        self.assertIsNotNone(self.framefactory.create_random_frame())

    def test_create_frames(self):
        self.assertIsNotNone(self.framefactory.create_frames(2))
    
    def test_create_frames_input(self):
        self.assertRaises(TypeError, self.framefactory.create_frames, "NNNNNNNN")

if __name__ == '__main__':  # pragma: no cover
    import framefactory
    unittest.main()
else:
    from environment import framefactory