from canlib import canlib, Frame, kvadblib
from canlib.kvadblib.framebox import FrameBox
import random

from environment import framefactory
from . import messagefactory
from . import printframe
from faultfunctions import signalfault

class SetupSignal():
    '''Class for setting up an environment to demonstrate the corrupt_signal function'''
    def __init__(self, database_size):
        self.str_min = 1
        self.str_max = 64
        self.min = 0
        self.max = 2047
        self.db = kvadblib.Dbc(name="database")
        self.message_factory = messagefactory.MessageFactory()
        self.frame_factory = framefactory.FrameFactory()
        self.db_size = database_size
        self.framebox = FrameBox(self.db)
        self.frames = []
        self.bound_messages = []

    def setup(self):
        c = 'a'
        for i in range(self.db_size):
            message = self.message_factory.create_random_message(db=self.db, id=i,name=c, signal_name= c + chr(ord(c)+1))
            c = chr(ord(c)+1)
       
        for i in range(0, self.db_size):
            data = []
            for _ in range(0, 8):
                datapoint = random.randint(0, 255)
                data.append(datapoint)
            frame = Frame(id_=i, data=data, dlc=8, flags=canlib.MessageFlag.EXT)
            self.frames.append(frame)

        i = 0
        for mess in self.db.messages():
            bound = mess.bind(self.frames[i])
            self.bound_messages.append(bound)
            i = i+1

    def print_db(self):
        """Prints the contents of the Dbc."""
        print(self.db)
        for message in self.db.messages():
            print('\n {}'.format(message))
            for signal in message:
                print('\n {}'.format(signal))

    def signal_transmit(self, channel, channel_read):
        '''
        Transmit a random frame from the database. Read and corrupt the frame using the signal name from the database.

        :param channel: Write channel
        :type channel: canlib.Channel
        :param channel_read: Read channel
        :type channel_read: canlib.Channel

        '''
        bound = random.choice(self.bound_messages)
        for signal in bound:
            print("Transmitting:")
            printframe.print_frame(bound._frame)
            channel.write(bound._frame)
            bound_message = signalfault.corrupt_signal(signal.signal.name, self.db, channel_read)
            channel.write(bound_message._frame)

    def signal_receive(self, channel):
        '''
        Receive CAN-frames on a channel.

        :param channel: Channel from which to read a frame.
        :type channel: canlib.Channel

        '''
        print("Receiving: ")
        frame = channel.read()
        printframe.print_frame(frame)