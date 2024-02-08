import os
from LLM_tasks import utils
import importlib.util
import sys
import textwrap

from LLM_tasks.LLM_Task import LLM_Task
import re
from knowledgebase.client import KnowledgebaseClient


class SummaryGenerator(LLM_Task):
    def __init__(self):
        super().__init__(os.path.dirname(os.path.abspath(__file__)))

        # Generator Statements
        self.system_msg = utils.read_file(os.path.join(self.task_path, 'system_msg.txt'))  # No generator statements

        # Overriden Settings
        self.num_examples = 5
        self.max_tokens = 1024

        self.kb_client = KnowledgebaseClient()

    def run(self, input, search_results=[], module=''):

        # 1. System Message
        messages = [
            {
                'role': 'system',
                'content': self.system_msg
            },
        ]

        # 2. User Input
        parsed_results = self.parse_results(search_results, module)
        user_input = parsed_results + '\n\n' + input
        messages.append({
            'role': 'user',
            'content': user_input
        })

        # 3. Completion
        completion = self.stream_chat_completion(messages, prefix='Summary Generator:')
        messages.append({
            'role': 'assistant',
            'content': completion
        })
        utils.write_messages_to_file(messages, self.debug_file)
        return completion


    def parse_results(self, search_results, module):
        context = '"""\n'
        for idx, entry in enumerate(reversed(search_results)):
            pattern = re.compile(r'^Slide (\d+)$', re.MULTILINE)
            match = pattern.search(entry)
            if match:
                slide_number = int(match.group(1))
            else:
                slide_number = -1
            new_entry = pattern.sub('', entry).strip()
            if module == 'UserInfo':
                context_line = new_entry + '\n'
            else:
                context_line = 'Slide ' + str(slide_number) + ':\n ' + textwrap.indent(new_entry, '\t') + '\n'
            context += context_line
        context += '"""'
        context = context.strip()
        return context


    def parse_completion(self, completion):
        return ''





if __name__ == '__main__':
    llm_task = SummaryGenerator()
    # response = llm_task.run('Is ADCS cost a component of satellite bus cost?')
    # print(response)








