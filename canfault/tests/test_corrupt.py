import unittest
from faultfunctions import faultfunction
from canlib import canlib, Frame
from bitarray import bitarray
from bitarray import util
import logging

class TestCorrup(unittest.TestCase):
    """Tests the faultfuncton.corrupt function."""
    def setUp(self):
        self.frame = Frame(23, 22, flags = canlib.MessageFlag.EXT)
        test_data = bytes(bitarray('1111 1111 0000 0000 1111 1111'))
        self.frame.data = test_data

        pass
    def tearDown(self):
        pass

    def test_corrupt(self):
        params = [8, 8]
        inverted_frame = faultfunction.corrupt(self.frame, params)
        inverted_test_data = bytes(faultfunction.bit_filler(bitarray('1111 1111 1111 1111 1111 1111')))
        self.assertEqual(inverted_frame.data, inverted_test_data)


        self.frame.data = bytes(faultfunction.bit_filler())
        inverted_test_data = bytes(faultfunction.bit_filler())
        inverted_frame = faultfunction.corrupt(self.frame, [0, 100])
        self.assertEqual(inverted_frame.data, inverted_test_data)

        self.frame.data = None
        inverted_test_data = bytes(faultfunction.bit_filler(bitarray('0000 0000 1111 1111')))
        inverted_frame = faultfunction.corrupt(self.frame, params)
        self.assertEqual(inverted_frame.data, inverted_test_data)
