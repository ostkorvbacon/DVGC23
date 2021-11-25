from canlib import canlib, Frame
from canlib.canlib import ChannelData
from CanWriteFault import write
import unittest

def do_nothing(frame, params):
    return frame

def setUpChannel(channel=0,
        openFlags=canlib.canOPEN_ACCEPT_VIRTUAL,
        bitrate=canlib.canBITRATE_500K,
        bitrateFlags=canlib.canDRIVER_NORMAL):

    ch = canlib.openChannel(channel, openFlags)
    print("Using channel: %s, EAN: %s" % (ChannelData(channel).channel_name,
                                          ChannelData(channel).card_upc_no))
    ch.setBusOutputControl(bitrateFlags)
    ch.setBusParams(bitrate)
    ch.busOn()
    return ch

def tearDownChannel(ch):
    ch.busOff()
    ch.close()

class TestWrite(unittest.TestCase):
    
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

    def tearDown(self):
        tearDownChannel(self.channel_read)
        tearDownChannel(self.channel_write)

    def test_write(self):
        write(self.channel_write, self.frame1)
        ret_frame = self.channel_read.read()
        self.assertEqual(ret_frame, self.frame1)
    
    def test_write_array(self):
        write(self.channel_write, [self.frame1, self.frame2])
        ret_frame1 = self.channel_read.read()
        ret_frame2 = self.channel_read.read()
        self.assertEqual([self.frame1, self.frame2], [ret_frame1, ret_frame2])

    def test_write_int_as_frame(self):
        self.assertRaises(TypeError, write, self.channel_write, 1)

    def test_write

    

    
if __name__ == '__main__':
    unittest.main()
