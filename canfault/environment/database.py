from canlib import kvadblib
from . import messagefactory

class Database():
    def __init__(self):
        self.db = kvadblib.Dbc(name = 'Database')
        self.message_factory = messagefactory.MessageFactory()
    
    def print_db(self):
        print(self.db)
        for message in self.db:
            print('\n {}'.format(message))
            for signal in message:
                print('\n {}'.format(signal))

    def add_item(self):
        self.message_factory.create_random_message(self.db)

    def add_number_of_items(self, num):
        self.message_factory.create_messages(db = self.db, number_of_messages = num)
    

