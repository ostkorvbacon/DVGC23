import unittest
from canlib import canlib, Frame
from faultfunctions import faultfunction
from timeit import default_timer as timer

class TestDelay(unittest.TestCase):
    """Tests the faultfuncton.delay function."""
    def setUp(self):
        self.frame1 = Frame(
            id_=0,
            data=[0],
            flags=canlib.MessageFlag.EXT
        )
        self.frame2 = Frame(
            id_=1,
            data=[1],
            flags=canlib.MessageFlag.EXT
        )
    
    def test_delay_one_sec(self):
        start = timer()
        ret_frame = delay(self.frame1, [1])
        time = timer() - start
        self.assertGreaterEqual(time, 1)
        self.assertLess(time, 2)
        self.assertEqual(ret_frame, self.frame1)

    def test_delay_no_param(self):
        start = timer()
        ret_frame = delay(self.frame1)
        time = timer() - start
        self.assertGreaterEqual(time, 0.1)
        self.assertLess(time, 1)
        self.assertEqual(ret_frame, self.frame1)
