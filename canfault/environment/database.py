from canlib import kvadblib
from . import messagefactory

class Database():
    """Class for creating and handling Dbc:s."""
    def __init__(self):
        self.db = kvadblib.Dbc(name = 'Database')
        self.message_factory = messagefactory.MessageFactory()
    
    def print_db(self):
        """Prints the contents of the Dbc."""
        print(self.db)
        for message in self.db:
            print('\n {}'.format(message))
            for signal in message:
                print('\n {}'.format(signal))

    def add_item(self):
        """Adds a random item to the database."""
        self.message_factory.create_random_message(self.db)

    def add_number_of_items(self, num):
        """Adds a number of random items to the database.
        
        :param num: Number of entries to add.
        :type num: int
        """
        self.message_factory.create_messages(db = self.db, number_of_messages = num)
    

