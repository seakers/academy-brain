import os
from LLM_tasks import utils
import importlib.util
import sys

from LLM_tasks.LLM_Task import LLM_Task
import re
from knowledgebase.client import KnowledgebaseClient
from academy_assistant.database.graphql import GraphqlClient

from LLM_tasks.summary_generation.SummaryGenerator import SummaryGenerator


class DialogueGenerator(LLM_Task):
    def __init__(self, user_info=None):
        super().__init__(os.path.dirname(os.path.abspath(__file__)))
        self.user_info = user_info

        # Generator Statements
        self.system_msg = utils.read_file(os.path.join(self.task_path, 'system_msg.txt'))  # No generator statements

        # Overriden Settings
        self.num_examples = 20

        # Helpers
        self.kb_client = KnowledgebaseClient()
        self.summary_gen = SummaryGenerator()

        self.max_tokens = 512

    def exam_check(self, route):
        db_client = GraphqlClient(self.user_info)
        modules = db_client.get_learning_modules()
        if 'LearningModule' in route:
            split_string = route.split('/')
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
                    if slide['type'] == 'question':
                        print(slide)
                        question_text = slide['question']['text']
                        question_choices = slide['question']['choices']
                        return '\n\nThe user is answering the following exam question. If their question is about it, directly answer saying you cannot answer their question:' \
                               '\n - Question: ' + question_text + \
                               '\n - Choices: ' + question_choices
        return ''

    def run(self, input, route=''):

        # 1. System message
        system_message = self.system_msg + self.exam_check(route)
        messages = [
            {
                'role': 'system',
                'content': system_message
            },
        ]

        # 2. Examples
        # messages += self.search_convo_examples(input, examples=self.req_examples, num_examples=2)
        messages += self.search_convo_examples(input)
        messages.append({
            'role': 'user',
            'content': "END OF EXAMPLES"
        })

        # 3. User Input
        messages.append({
            'role': 'user',
            'content': input
        })

        # 4. Start Conversation
        return self.start_dialogue(messages, route)

    def run_vision(self, input, slide_info, route=''):

        # 1. System message
        print("##### IN DIALOUGE GEN ######")
        system_message = self.system_msg + self.exam_check(route)
        messages = [
            {
                'role': 'system',
                'content': system_message
            },
        ]

        # 2. Examples
        # messages += self.search_convo_examples(input, examples=self.req_examples, num_examples=2)
        messages += self.search_convo_examples(input)
        messages.append({
            'role': 'user',
            'content': "END OF EXAMPLES"
        })

        ############## ADD FOR GPT VISION #####################
        # slide_image_url = None
        slide_image_url = "http://drive.google.com/uc?export=view&id=1yrGe-_kej1hG5h5rbTE63562UOUigx7i"

        ################ TO DO :: ADD CODE TO ASSIGN "slide_image_url" URL of image ####################
        # slide_info = {topic: this.currentTopic, module: this.currentModule, slide: this.currentSlide}
        ## Call query to get slide_image_url for particular topic, module and slide

        db_client = GraphqlClient(self.user_info)
        
        # imageurl_info = db_client.get_slide_info(slide_info["topic"], slide_info["module"], slide_info["slide"])
        imageurl_info = db_client.get_slide_info(slide_info["module"], slide_info["slide"])
        print("##### imageurl_info ####", imageurl_info)

        if len(imageurl_info):
            slide_image_url = imageurl_info[0]['image_url']
            
        print("##### slide_image_url ####", slide_image_url)

        ################################################################################################

        # 3. User Input
        print('--> INPUT', input)
        messages.append({
            'role': 'user',
            'content': [
                {
                    "type": "text",
                    "text": input
                    },
                {
                    "type": "image_url",
                    "image_url": {
                    "url": slide_image_url
                    }
                }
            ]
        })
        #######################################################


        # 4. Start Conversation
        return self.start_dialogue(messages, route)

    def start_dialogue(self, messages, route):
        # This function will loop calling the LLM until a final answer is reached

        completion = self.stream_chat_completion(messages, prefix='Convo Generator: ')
        messages.append({
            'role': 'assistant',
            'content': completion
        })

        while self.stop_condition(completion) is False:

            # Search Information Space
            module, query = self.parse_completion(completion)
            search_results = \
            self.kb_client.query({'class': module, 'query': query, 'user_info': self.user_info, 'route': route})[
                'formatted_results']

            # Get search result message
            if len(search_results) == 0:
                search_result_msg = 'NO RESULTS'
            else:
                search_result_msg = self.summary_gen.run(query, search_results, module)
                if 'Insufficient information' in search_result_msg:
                    search_result_msg = 'NO RESULTS'
            messages.append({
                'role': 'user',
                # 'content': search_result_msg,
                'content': 'Query Response: ' + search_result_msg
            })

            # Get next completion
            completion = self.stream_chat_completion(messages, prefix='Convo Generator: ')
            messages.append({
                'role': 'assistant',
                'content': completion
            })

            # Save messages
            utils.write_messages_to_file(messages, self.debug_file)

        return completion

    def stop_condition(self, completion):
        if completion.strip().startswith('('):
            return False
        else:
            return True

    def parse_completion(self, completion):
        completion = completion.strip()
        pattern = r'\((.*?)\)'
        matches = re.findall(pattern, completion)
        module = matches[0]
        query = completion[completion.find(')') + 1:].strip()
        return module, query

    ################
    ### Combined ###
    ################

    def load_file_examples(self, example_file):
        spec = importlib.util.spec_from_file_location("module.examples", example_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if isinstance(module.examples[0], list):
            print('Convo based examples')
            examples = [example for example in module.examples]
        else:
            examples = [example for example in module.examples if example['user'] != '']
        return examples


if __name__ == '__main__':
    llm_task = DialogueGenerator()
    question = ""
    question = "How is orbit velocity calculated?"

    response = llm_task.run(question)
