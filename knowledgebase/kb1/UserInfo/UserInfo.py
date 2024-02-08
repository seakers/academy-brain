import os
from LLM_tasks import utils
import json
from io import StringIO
import textwrap
from knowledgebase.Module import Module
from academy_assistant.database.graphql import GraphqlClient




class UserInfo(Module):

    def __init__(self):
        super().__init__(os.path.dirname(os.path.abspath(__file__)))


    def get_entries(self, user_info, route):
        db_client = GraphqlClient(user_info)
        modules = db_client.get_learning_modules()

        # User report
        user_report = 'User Report:\n'
        user_report += 'Username: ' + user_info.user.username + '\n'
        user_report += self.get_user_module_report(modules)
        user_report += self.get_user_state_report(route, modules)

        entries = [{'entry': user_report}]
        return entries

    def get_user_module_report(self, modules):
        module_report = 'Assigned Learning Modules:\n'
        module_text = ''
        for module in modules:  # ['id', 'name', 'icon', 'join_info', 'slides']
            progress = 0
            slide_questions = 0
            slide_questions_answered = 0
            for idx, slide in enumerate(module['slides']):
                if slide['type'] == 'question':
                    slide_questions += 1
                    if slide['answered'] is True:
                        slide_questions_answered += 1
            if slide_questions > 0:
                progress = (slide_questions_answered / slide_questions) * 100
            module_text += module['name'] + ': ' + str(progress) + '% complete\n'
        return module_report + textwrap.indent(module_text, '\t')

    def get_user_state_report(self, route, modules):
        print('--> ROUTE:', route)  # /LearningModule/Space Mission Overview/1  |  /take-exam
        if 'mastery' in route:
            state_report = 'state: user is viewing the Mastery page.'
        elif 'take-exam' in route:
            state_report = 'state: user is taking adaptive exam.'
            # TODO: try to get test question and tell model not to answer it
        elif 'LearningModule' in route:
            split_string = route.split('/')
            print('split_string', split_string)
            # Check if there are enough elements in the list
            if len(split_string) < 4:
                state_report = "state: no learning module selected\n"
            else:
                lm_name = split_string[2]
                curr_lm = None
                for module in modules:
                    if module['name'] == lm_name:
                        curr_lm = module
                if curr_lm is None:
                    state_report = "state: learning module not recognized\n"
                else:
                    # get index of slide
                    slide_idx = int(curr_lm['join_info'][0]['slide_idx'])
                    slide = curr_lm['slides'][slide_idx]
                    state_report = 'state: viewing slide ' + str(slide_idx) + ' in learning module ' + lm_name + ':\n'
                    state_report += str(slide)
        else:
            state_report = ''
        return state_report

    ##############
    ### Search ###
    ##############

    def search(self, inputs):

        # 1. Get Entries
        all_entries = self.get_entries(inputs['user_info'], inputs['route'])

        # 2. Search Entries
        # query = inputs['query']
        # results, entries = self.similarity.search(query, search_strings, top_n=self.num_results)
        # top_entries = [all_entries[index] for score, index in results]
        # return top_entries
        return all_entries

    def get_entry_search_string(self, entry):
        return entry['entry']



if __name__ == '__main__':
    module = UserInfo()
    query_block = {
        'type': 'query',
        'id': 'Q1',
        'class': 'UserInfo',
        'query': 'How is x y z calculated?'
    }
    results = module.search(query_block)
    print(results)












