import unittest
from main import setUpChannel

class TestTransceiver(unittest.TestCase):
    """Tests the environment.transciever function."""
    def setUp(self) -> None:
        self.ch = setUpChannel()
        self.transceiver = transciever.Transceiver(self.ch)

    def test_transmit(self):
        self.transceiver.transmit()
    
    def test_faulty_arguments_func(self):
        self.assertRaises(TypeError, self.transceiver.transmit, func = [1, "hej"])

    def test_faulty_arguments_params(self):
        self.assertRaises(TypeError, self.transceiver.transmit, params = 1)

    def tearDown(self) -> None:
        self.ch.busOff()
        self.ch.close()

if __name__ == '__main__':  # pragma: no cover
    import transciever
    unittest.main()
else:
    from environment import transciever