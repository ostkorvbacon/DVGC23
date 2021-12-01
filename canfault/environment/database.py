from canlib import kvadblib
import messagefactory

class Database():
    def __init__(self):
        self.db = kvadblib.Dbc(name = 'Database')

    def add_item(self):
        messagefactory.MessageFactory.create_random_message(self.db)

    def add_number_of_items(self, num):
        messagefactory.MessageFactory.create_messages(self.db, num)
    

