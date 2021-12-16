import unittest
from faultfunctions import faultfunction
from canlib import canlib, Frame


class TestDuplicate(unittest.TestCase):
    """Tests the faultfuncton.drop function."""
    def setUp(self):
        self.frame = Frame(23, [22], flags=canlib.MessageFlag.EXT)
        pass

    def tearDown(self):
        pass

    def test_drop(self):
        r = faultfunction.drop(self.frame)
        self.assertEqual(r, None)
