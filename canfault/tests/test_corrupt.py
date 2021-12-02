import unittest
from faultfunctions import faultfunction
from canlib import canlib, Frame
from bitarray import bitarray
from bitarray import util
import logging

class TestCorrup(unittest.TestCase):

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
        logging.error("inverted_frame: {}". format(inverted_frame.data))
        inverted_test_data = bytes(faultfunction.bit_filler(bitarray('1111 1111 1111 1111 1111 1111')))


        logging.error("inverted_test_data: {}". format(inverted_test_data))

        self.assertEqual(inverted_frame.data, inverted_test_data)
