import unittest
from main import setUpChannel

class TestTransceiver(unittest.TestCase):
    def setUp(self) -> None:
        self.ch = setUpChannel()
        self.transceiver = transciever.Transceiver(self.ch)

    def test_transmit(self):
        self.transceiver.transmit()

if __name__ == '__main__':  # pragma: no cover
    import transciever
    unittest.main()
else:
    from environment import transciever