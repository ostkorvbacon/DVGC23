import unittest
from duplicate import duplicate
from canlib import canlib, Frame
class TestDuplicate(unittest.TestCase):
    
    def setUp(self):
        self.frame = Frame(23, 22, flags = canlib.MessageFlag.EXT)
        pass
    def tearDown(self):
        pass

    def test_duplicate(self):
        f = duplicate(2)
        g = [2,2]
        self.assertEqual(f,g)
        f = duplicate(self.frame)
        g = [self.frame, self.frame]
        self.assertEqual(f,g)
