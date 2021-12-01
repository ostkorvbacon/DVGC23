import unittest
from canlib import Frame, frame

class TestPrintFrame(unittest.TestCase):
    def setUp(self) -> None:
        self.framefactory = framefactory.FrameFactory()

    def test_print_frame_type_right(self):
        self.assertRaises(TypeError, printframe.print_frame(self.framefactory.create_random_frame()))
    
    def test_print_frame_type_wrong(self):
        self.assertRaises(TypeError, printframe.print_frame, "INCORRECT")

if __name__ == '__main__':  # pragma: no cover
    import printframe
    import framefactory
    unittest.main()
else:
    from environment import printframe
    from environment import framefactory
