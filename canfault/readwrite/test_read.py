import unittest
from canlib import canlib, Frame
from canlib.canlib import ChannelData

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

class TestRead(unittest.TestCase):
    
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

    def test_read(self):
        self.channel_write.write(self.frame1)
        ret_frame = read(self.channel_read, do_nothing)
        self.assertEqual(self.frame1, ret_frame)

    def test_read_provided_frame(self):
        ret_frame = read(self.channel_read, do_nothing, self.frame1)
        self.assertEqual(ret_frame, self.frame1)
    
    def test_read_no_func(self):
        ret_frame = read(self.channel_read, frame = self.frame1)
        self.assertEqual(ret_frame, self.frame1)
    
    def test_read_no_msg(self):
        ret_frame = read(self.channel_read)
        self.assertIsNone(ret_frame)
    
    def test_read_int_as_frame(self):
        self.assertRaises(TypeError, read, self.channel_read, frame = 1)

    

    
if __name__ == '__main__':
    from CanReadFault import read
    unittest.main()
else:
    from readwrite.CanReadFault import read