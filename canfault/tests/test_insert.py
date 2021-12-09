import unittest
from faultfunctions import faultfunction
from canlib import canlib, Frame


class TestInsert(unittest.TestCase):
    """Tests the faultfuncton.insert function."""
    def setUp(self):
        self.frame = Frame(23, [22], flags=canlib.MessageFlag.EXT)
        pass

    def tearDown(self):
        pass

    def test_insert(self):
        a = False
        s = faultfunction.insert(self.frame)
        new_frame = s[0]
        old_frame = s[1]
        self.assertEqual(old_frame, self.frame)
        if(new_frame.__class__ == Frame):
            a = True
        self.assertEqual(a, True)
