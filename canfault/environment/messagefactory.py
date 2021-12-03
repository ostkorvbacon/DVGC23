import random
from canlib import kvadblib

class MessageFactory:
    """Creates and insertes messages with randomized data and signals"""
    def __init__(self):
        self.str_min = 1
        self.str_max = 64
        self.min = 0
        self.max = 1023
        self.data_amount = 8
    
    def random_name(self):
        """Creates a randomized string of a randomized length between 0 and 255, returns the string"""
        char_max = 255
        char_min = 0
        random.seed()
        name_length = random.randint(self.str_min, self.str_max)
        str = ""

        for _ in range(name_length):
            char = chr(random.randint(char_min, char_max))
            str += char
        str += '\0'
        return str

    def set_message_signal(self, message, 
                            signal_type=kvadblib.SignalType.FLOAT, 
                            startbit=0, 
                            length=32, 
                            min=0, 
                            max=100, 
                            unit=' m', 
                            comment='No comment' ):
        """Set the signal of a message with possibly random data
        
        :param message: Message to assign the signal to.
        :type message: kvadblib.Message
        :param signal_type: The type for the signal. Defaults to FLOAT
        :type signal_type: kvadblib.SignalType
        :param startbit: Sets the first position of the data. Defaults to 0
        :type startbit: int
        :param length: Sets the distance between the startbit and the last bit of the data. Defaults to 32.
        :type length: int
        :param min: Minimum value for the data. Defaults to 0.
        :type min: int
        :param max: Maximum value for the data. Defaults to 100.
        :type max: int
        :param unit: Unit which the value is measured in. i.e. m, km/h, s... Defaults to ' m'.
        :type unit: String
        :param comment: Comment describing the contents of the signal. Defaults to 'No comment'.
        :type comment: String
        """
        message.new_signal(
            name = self.random_name(),
            type = signal_type,
            size = kvadblib.ValueSize( startbit = startbit, length = length),
            limits = kvadblib.ValueLimits(min = min, max = max),
            unit = unit,
            comment = comment
        )
    
    def create_random_message(self, db, name = 'Name', flag = 0, dlc = None, comment = None):
        """Creates a single messages with random data, returns the message
        
        :param db: Dbc to add the message to.
        :type db: kvadblib.Dbc
        :param name: Name of the message. Defaults to 'Name'
        :type name: String
        :param flag: The message flags. Defaults to 0
        :type flag: kvadblib.MessageFlag
        :param dlc: The DLC field. Defaults to 0.
        :param comment: Comment describing the message. Defaults to None
        :tyoe comment: String
        """
        if name == 'Name':
            name = self.random_name()
        id = random.randint(self.min, self.max)

        message = db.new_message(name, id, flags = flag, dlc = dlc, comment = comment)
        self.set_message_signal(message)
        return message

    def create_messages(self, db, number_of_messages):
        """Creates a set of messages with random data and IDs, returns the set as a list
        
        :param db: Dbc to add the messages to.
        :type db: kvadblib.Dbc
        :param number_of_messages: The number of messages to be created.
        :type number of messages: int
        """
        if not isinstance(number_of_messages, int):
            raise(TypeError("number_of_messages needs to be an int"))
        for _ in range(number_of_messages):
            message = self.create_random_message(db)
            self.set_message_signal(message)