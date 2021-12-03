import unittest
from faultfunctions import faultfunction
from canlib import canlib, Frame
class TestDuplicate(unittest.TestCase):
    """Tests the faultfuncton.duplicate function."""
    def setUp(self):
        self.frame = Frame(23, [22], flags = canlib.MessageFlag.EXT)
        pass
    def tearDown(self):
        pass

    def test_duplicate(self):
        f = faultfunction.duplicate(2)
        g = [2,2]
        self.assertEqual(f,g)
        f = faultfunction.duplicate(self.frame)
        g = [self.frame, self.frame]
        self.assertEqual(f,g)
        f = faultfunction.duplicate(self.frame,params=[3])
        g = [self.frame, self.frame, self.frame]
        self.assertEqual(f,g)
