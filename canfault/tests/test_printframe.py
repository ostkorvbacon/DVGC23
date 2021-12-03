import unittest
import printframe
import framefactory
from canlib import Frame, frame

class TestPrintFrame(unittest.TestCase):
    """Tests the environment.printframe function."""
    def setUp(self) -> None:
        self.framefactory = framefactory.FrameFactory()

    def test_print_frame_type_right(self):
        self.assertRaises(TypeError, printframe.print_frame(self.framefactory.create_random_frame()))
    
    def test_print_frame_type_wrong(self):
        self.assertRaises(TypeError, printframe.print_frame, "INCORRECT")