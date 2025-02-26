from academy_assistant.database.client.modules.textbook import get_module as get_textbooks

class TextBook:

    def __init__(self, client):
        self.client = client
        self.textbooks = get_textbooks()

    def index(self):
        for textbook in self.textbooks:
            # --> 1. Get user ids
            for user in self.client.get_users():
                self.client.index_textbook(textbook['title'], user.id, textbook['textbook_url'])
