import unittest
import printframe

class TestPrintFrame(unittest.TestCase):
    def test_print_frame_type(self):
        self.assertRaises(TypeError, printframe.print_frame("mmmmm"))

if __name__ == '__main__':
    unittest.main()