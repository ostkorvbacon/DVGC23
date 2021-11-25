import unittest
import transciever

class TestTransceiver(unittest.TestCase):
    def setUp(self) -> None:
        self.transceiver = transciever.Transceiver

    def test_transmit(self):
        self.transceiver.transmit()

if __name__ == '__main__':
    unittest.main()