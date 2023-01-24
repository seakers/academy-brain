import datetime
import json
from django.conf import settings

from academy_assistant.assistant.intents.ParameterExtractor import ParameterExtractor

from academy_assistant.database.client.GraphqlClient import GraphqlClient


class IntentHandler:


    def __init__(self, user_info, command, intent):
        self.app_path = settings.ACADEMY_PATH
        self.user_info = user_info
        self.command = command
        self.command_processed = settings.NLP_MODEL(self.command.strip())
        self.intent = intent
        self.extractor = ParameterExtractor(self.user_info, self.command_processed)



    def process(self):
        intent_func = 'intent_' + str(self.intent)
        if hasattr(self, intent_func):
            print('--> PROCESSING INTENT FUNCTION:', intent_func)
            func = getattr(self, intent_func)
            return func()
        else:
            raise Exception("Intent function DNE:", intent_func)

    ########################
    ### Intent Functions ###
    ########################
    # ["Analyst", "Engineer", "Critic", "Historian", "Teacher"]
    # Every one needs to be re-written for Cost Estimator Tutoring

    def insert_msg(self, message, type, writer, more_info=None):
        print('!!! Message insertion moved to end of view called by user message !!!')

    def intent_1000(self):
        print('--> REWRITE INTENT METHOD FOR DAPHNE ACADEMY')

    def intent_2000(self):
        print('--> REWRITE INTENT METHOD FOR DAPHNE ACADEMY')

    def intent_2001(self):
        print('--> REWRITE INTENT METHOD FOR DAPHNE ACADEMY')

    def intent_3000(self):
        print('--> REWRITE INTENT METHOD FOR DAPHNE ACADEMY')

    def intent_4000(self):
        print('--> REWRITE INTENT METHOD FOR DAPHNE ACADEMY')

    def intent_5000(self):
        print('--> REWRITE INTENT METHOD FOR DAPHNE ACADEMY')
        return {'text': 'Delta-V is the total change in velocity required for a mission'}

















