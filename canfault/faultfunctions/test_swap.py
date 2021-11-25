import unittest
from canlib import canlib, Frame

class TestSwap(unittest.TestCase):

    def reset_swap(self):
        if(swap(self.frame1) is None):
            swap(self.frame1)

    def setUp(self):
        self.frame1 = Frame(
            id_=0,
            data=[0],
            flags=canlib.MessageFlag.EXT
        )
        self.frame2 = Frame(
            id_=1,
            data=[1],
            flags=canlib.MessageFlag.EXT
        )
        self.reset_swap()

    def test_swap_called_once(self):
        ret1_frame = swap(self.frame1)
        self.assertIsNone(ret1_frame)

    def test_swap_called_twice_intended_behaviour(self):
        ret1_frame = swap(self.frame1)
        ret2_frame = swap(self.frame2)
        self.assertIsNone(ret1_frame)
        self.assertEqual(ret2_frame[0], self.frame2)
        self.assertEqual(ret2_frame[1], self.frame1)

    def test_swap_called_thrice(self):
        swap(self.frame1)
        swap(self.frame2)
        ret3_frame = swap(self.frame1)
        self.assertIsNone(ret3_frame)

    def test_swap_for_None_frames(self):
        ret1_frame = swap(None)
        ret2_frame = swap(None)
        self.assertIsNone(ret1_frame)
        self.assertEqual(ret2_frame, [None, None])

    def test_swap_for_None_and_real_frames(self):
        ret1_frame = swap(None)
        ret2_frame = swap(self.frame2)
        self.assertIsNone(ret1_frame)
        self.assertEqual(ret2_frame[0], self.frame2)
        self.assertIsNone(ret2_frame[1])

    def test_swap_for_real_and_None_frames(self):
        ret1_frame = swap(self.frame2)
        ret2_frame = swap(None)
        self.assertIsNone(ret1_frame)
        self.assertEqual(ret2_frame[1], self.frame2)
        self.assertIsNone(ret2_frame[0])


if __name__ == '__main__': # pragma: no cover
    from swap import swap
    unittest.main()
else:
    from faultfunctions.swap import swap
