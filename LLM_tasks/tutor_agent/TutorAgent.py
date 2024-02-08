import os
import textwrap

from LLM_tasks.LLM_Task import LLM_Task

from academy_assistant.database.graphql import GraphqlClient


class TutorAgent(LLM_Task):
    def __init__(self, user_info):
        super().__init__(os.path.dirname(os.path.abspath(__file__)))
        self.user_info = user_info
        self.db_client = GraphqlClient(user_info)

        # Settings
        self.max_tokens = 512

    def run(self, input, route=''):
        print('--> CALLING TUTOR AGENT')
        messages = [{
            'role': 'system',
            'content': self.build_system_message(route)
        }]

        db_messages = self.db_client.get_messages()
        for message in db_messages:
            if 'sender' in message and message['sender'] == 'User':
                role = 'user'
            else:
                role = 'assistant'
            messages.append({
                'role': role,
                'content': message['text']
            })


        completion = self.get_chat_completion(messages)
        messages.append({
            'role': 'assistant',
            'content': completion
        })
        self.write_messages_to_file(messages, self.debug_file)
        return self.parse_completion(completion)


    def build_system_message(self, route):
        modules = self.db_client.get_learning_modules()

        # User report
        user_report = 'User Report:\n'
        user_report += 'Username: ' + self.user_info.user.username + '\n'
        user_report += self.get_user_module_report(modules)
        user_report += self.get_user_state_report(route, modules)

        return self.system_msg + '\n\n' + user_report


    #########################
    ### Context Functions ###
    #########################

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
                    print('--> USER ON SLIDE:', slide_idx)
                    slide = curr_lm['slides'][slide_idx]
                    state_report = 'state: viewing slide ' + str(slide_idx) + ' in learning module ' + lm_name + ':\n'
                    state_report += str(slide)




            # TODO: get learning module slide text and put in report
        else:
            state_report = ''
        return state_report






