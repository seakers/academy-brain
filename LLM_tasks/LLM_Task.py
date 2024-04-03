import os
import importlib.util
import sys
import openai
# openai.api_key = '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'
openai.api_key = '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'

from retrying import retry
import concurrent.futures
import time

from LLM_tasks.embeddings.search import similarity








class LLM_Task:

    def __init__(self, task_path):
        self.task_path = task_path
        self.debug_file = os.path.join(task_path, 'debug.txt')

        self.system_msg_file = os.path.join(task_path, 'system_msg.txt')
        self.system_msg = self.read_file(self.system_msg_file)

        self.example_file = os.path.join(task_path, 'examples.py')
        self.examples = self.load_examples()

        # Settings
        self.max_tokens = 256
        self.model = 'gpt-4-turbo-preview'  # 'gpt-4'
        self.temperature = 0.0

        # Similarity Search
        self.similarity = similarity

        # Num Examples
        self.num_examples = 5


    ################
    ### Examples ###
    ################
    def load_examples(self):
        spec = importlib.util.spec_from_file_location("module.examples", self.example_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if isinstance(module.examples[0], list):
            print('Convo based examples')
            examples = [example for example in module.examples]
        else:
            examples = [example for example in module.examples if example['user'] != '']
        return examples

    def search_examples(self, input, examples=None):
        if examples is None:
            examples = self.examples
        user_messages = [example['user'] for example in examples]
        results, entries = self.similarity.search(input, user_messages, top_n=self.num_examples)
        top_examples = [examples[index] for score, index in results]
        examples_msg = []
        for ex in top_examples:
            examples_msg.append({
                'role': 'user',
                'content': ex['user']
            })
            examples_msg.append({
                'role': 'assistant',
                'content': ex['assistant']
            })
        return examples_msg

    def search_convo_examples(self, input, examples=None, num_examples=None):
        if num_examples is None:
            num_examples = self.num_examples
        if examples is None:
            examples = self.examples
        user_messages = []
        for example in examples:
            for msg in example:
                if msg[0] == 'user':
                    user_messages.append(msg[1])
                    break
        results, entries = self.similarity.search(input, user_messages, top_n=num_examples)
        top_examples = [examples[index] for score, index in results]
        examples_msg = []
        idx = 1
        for ex in reversed(top_examples):
            for msg in ex:
                examples_msg.append({
                    'role': msg[0],
                    # 'content': 'Example ' + str(idx) + ': ' + msg[1]
                    'content': msg[1]
                })
            idx += 1
        return examples_msg


    ###########
    ### Run ###
    ###########

    def run(self, input):
        messages = [{
            'role': 'system',
            'content': self.system_msg
        }]
        messages += self.search_examples(input)
        messages.append({
            'role': 'user',
            'content': input
        })
        completion = self.get_chat_completion(messages)
        messages.append({
            'role': 'assistant',
            'content': completion
        })
        self.write_messages_to_file(messages, self.debug_file)
        return self.parse_completion(completion)


    #############
    ### Parse ###
    #############

    def parse_completion(self, completion):
        return completion



    ######################
    ### Get Completion ###
    ######################

    def get_chat_completion(self, messages, timeout=30):
        try:
            print('--> ATTEMPTING COMPLETION')
            response = self.get_chat_completion_with_timeout(messages, timeout)
            completion = response.choices[0].message.content
        except Exception as e:
            print(f"Error after 4 attempts: {e}")
            completion = ''
        return completion

    @retry(stop_max_attempt_number=4, retry_on_exception=lambda e: isinstance(e, (openai.Error, concurrent.futures.TimeoutError)))
    def get_chat_completion_with_timeout(self, messages, timeout):
        # the Executor will run the function in a separate thread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(self.get_chat_completion_robust, messages)
            try:
                return future.result(timeout=timeout)
            except concurrent.futures.TimeoutError:
                print('Timeout! Retrying...')
                raise


    def get_chat_completion_robust(self, messages):
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )
        return completion



    #########################
    ### Stream Completion ###
    #########################

    def stream_chat_completion(self, messages, prefix='Task: '):
        streamed_completion = openai.ChatCompletion.create(
            # model=self.model,
            model="gpt-4-vision-preview",
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            stream=True,
        )
        sys.stdout.write(prefix)
        sys.stdout.flush()
        aggregated_completion = ''
        for completion in streamed_completion:
            completion_segment = completion.choices[0]['delta']
            if 'content' in completion_segment:
                content = completion_segment['content']
                aggregated_completion += content
                sys.stdout.write(content)
                sys.stdout.flush()
        print('\n')
        return aggregated_completion




    #############
    ### Utils ###
    #############

    def read_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        return ''.join(lines)

    def write_messages_to_file(self, messages, output_file):
        with open(output_file, 'w+') as f:
            for message in messages:
                f.write(f"{message['role'].capitalize()}:\n")
                f.write(f"{message['content']}\n\n")