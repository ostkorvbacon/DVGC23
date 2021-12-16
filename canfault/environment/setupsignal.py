from canlib import kvadblib
import random
from canlib.kvadblib.framebox import FrameBox
from . import messagefactory
from faultfunctions import signalfault

class SetupSignal():
    def __init__(self, database_size):
        self.str_min = 1
        self.str_max = 64
        self.min = 0
        self.max = 2047
        self.db = kvadblib.Dbc(name="database")
        self.message_factory = messagefactory.MessageFactory()
        self.db_size = database_size
        self.framebox = FrameBox(self.db)

    def setup(self):
        c = 'a'
        for i in range(self.db_size):
            message = self.message_factory.create_random_message(db=self.db, id=i,name=c, signal_name=chr(ord(c)+1))
            c = chr(ord(c)+1)
        self.print_db()
        for message in self.db:
            self.framebox.add_message(message)
        for signal in self.framebox.signals():
            print(signal.name)
            signal.phys = random.randint(self.min, self.max)
        


    def print_db(self):
        """Prints the contents of the Dbc."""
        print(self.db)
        for message in self.db:
            print('\n {}'.format(message))
            for signal in message:
                print('\n {}'.format(signal))

    def signal_transmit(self, channel):
        for frame in self.framebox.frames():
            print("Transmitting: ")
            print(frame)
            message = self.db.interpret(frame)
            channel.write(frame)
            for messages in self.db:
                if message._frame.id == messages.id:
                    for signal in messages.signals():
                        print("SIGNAL")
                        print(signal.name)
                        new_frame = signalfault.corrupt_signal(signal.name, self.db, channel)
                        channel.write(new_frame)

    def signal_receive(self, channel):
        
        for _ in self.framebox.frames():
            print("Receiving: ")
            frame = channel.read()
            print(frame)
