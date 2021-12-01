import random
from canlib import kvadblib, kvMessage

"""Class for creating and inserting messages with randomized data and signals"""
class MessageFactory:
    def __init__(self):
        self.str_min = 1
        self.str_max = 64
        self.min = 0
        self.max = 1023
        self.data_amount = 8
    
    def random_name(self):
        char_max = 255
        char_min = 0
        random.seed()
        name_length = random.randint(self.min, self.max)
        name = []

        for _ in range(name_length):
            name.append(chr(random.ranint(char_min, char_max)))
        
        return name

    """Set the signal of a message with possibly random data"""
    def set_message_signal(self, message, signal_type = kvadblib.SignalType.FLOAT, startbit = 0, length = 32, min = 0, max = 100, unit = ' m', comment = 'No comment' ):
        message.new_signal(
            name    = self.random_name(),
            type    = signal_type,
            size    = kvadblib.ValueSize( startbit = startbit, length = length) ,
            limits  = kvadblib.ValueLimits(min = min, max = max) ,
            unit    = unit,
            comment = comment
        )

    """Create a single messages with random data"""
    def create_random_message(self, db, name = 'Name', flag = 0, dlc = None, comment = None):
        name = self.random_name()
        id = random.randint(self.min, self.max)

        message = db.new_message(name, id, flags = flag, dlc = dlc, comment = None)
        self.set_message_signal(message)

    """Create a set of messages with random data and IDs returned as a list"""
    def create_messages(self, db, number_of_messages):
        if not isinstance(number_of_messages, int):
            raise(TypeError("number_of_messages needs to be an int"))
        for _ in range(number_of_messages):
            message = self.create_random_message(db)
            self.set_message_signal(message)