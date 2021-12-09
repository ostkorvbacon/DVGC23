import unittest
from canlib import canlib, Frame
from canlib.canlib import ChannelData
from readwrite.readfault import read


def do_nothing(frame, params):
    return frame


def setUpChannel(channel=0,
                 openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
                 bitrate=canlib.canBITRATE_500K,
                 bitrateFlags=canlib.canDRIVER_NORMAL):

    ch = canlib.openChannel(channel, openFlags)
    ch.setBusOutputControl(bitrateFlags)
    ch.setBusParams(bitrate)
    ch.busOn()
    return ch


def tearDownChannel(ch):
    ch.busOff()
    ch.close()


def reset(ch):
    """Makes sure there are no Frames left in the
       message queue on the provided channel."""
    frame = read(ch)
    while frame is not None:
        frame = read(ch)


class TestRead(unittest.TestCase):
    """Tests the readwrite.read function."""
    def setUp(self):
        self.channel_read = setUpChannel(0)
        self.channel_write = setUpChannel(1)
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
        reset(self.channel_read)

    def tearDown(self):
        tearDownChannel(self.channel_read)
        tearDownChannel(self.channel_write)

    def test_read(self):
        self.channel_write.write(self.frame1)
        ret_frame = read(self.channel_read, do_nothing)
        self.assertEqual(self.frame1, ret_frame)

    def test_read_provided_frame(self):
        ret_frame = read(self.channel_read, do_nothing, self.frame1)
        self.assertEqual(ret_frame, self.frame1)

    def test_read_no_func(self):
        ret_frame = read(self.channel_read, frame=self.frame1)
        self.assertEqual(ret_frame, self.frame1)

    def test_read_no_msg(self):
        ret_frame = read(self.channel_read)
        self.assertIsNone(ret_frame)

    def test_read_int_as_frame(self):
        self.assertRaises(TypeError, read, self.channel_read, frame=1)

    def test_read_int_as_channel(self):
        self.assertRaises(TypeError, read, 1)

    def test_write_faulty_arguments_func(self):
        self.assertRaises(TypeError, read, self.channel_read, func=1)

    def test_write_faulty_arguments_params(self):
        self.assertRaises(TypeError, read, self.channel_read, params=1)
