import os
from LLM_tasks import utils
import importlib.util
import sys
from academy_auth.models import UserInformation
from LLM_tasks.LLM_Task import LLM_Task
import re
from knowledgebase.client import KnowledgebaseClient
from academy_assistant.database.graphql import GraphqlClient
from LLM_tasks.pdf_slide_vision_model.AdaptiveRAG import AdaptiveRAG
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from LLM_tasks.summary_generation.SummaryGenerator import SummaryGenerator
import whisper
import pyaudio
import wave
import pyttsx3
import tempfile
from openai import OpenAI


class DialogueGenerator(LLM_Task):
    def __init__(self, user_info=None):
        super().__init__(os.path.dirname(os.path.abspath(__file__)))
        self.user_info = user_info
        print('USER INFO', user_info)

        # Generator Statements
        self.system_msg = utils.read_file(os.path.join(self.task_path, 'system_msg.txt'))  # No generator statements

        # Overriden Settings
        self.num_examples = 20

        # Helpers
        self.kb_client = KnowledgebaseClient()
        self.summary_gen = SummaryGenerator()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        slides_path = os.path.join(current_dir, '..', 'pdf_slide_vision_model', 'slide_vision', 'slide_vector_store')
        pdfs_path = os.path.join(current_dir, '..', 'pdf_slide_vision_model', 'pdf_vision', 'pdf_vector_store')

        self.rag = AdaptiveRAG(
            slides_path=slides_path,
            pdfs_path=pdfs_path
        )
        self.llm = ChatOpenAI(
            model="gpt-4o",
            max_tokens=256,
            temperature=0.0
        )

        self.audio_model = whisper.load_model("base")  # or "tiny" for faster but less accurate
        self.tts_engine = pyttsx3.init()
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
    
    def speech_to_text(self, audio_data=None):
        try:
            if audio_data is None:
                raise ValueError("No audio data provided")
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio:
                temp_audio.write(audio_data.read())
                temp_path = temp_audio.name
            result = self.audio_model.transcribe(temp_path)
            os.unlink(temp_path)
            return result["text"].strip()
        except Exception as e:
            print(f"Error in speech to text: {str(e)}")
            return None
        
    def text_to_speech(self, text=None):
        try:
            client = OpenAI()
            response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=text 
            )
            output_path = "output.mp3"
            response.stream_to_file(output_path)
            return output_path

        except Exception as e:
            print(f"Error in text_to_speech: {str(e)}")
            return None 

    # def text_to_speech(self, text):
    #     engine = pyttsx3.init()
    #     engine.say(text)
    #     engine.runAndWait()
    #     engine.stop()

    # def process_voice(self):
    #     user_input = self.speech_to_text()
    #     print(f"You said: {user_input}")
    #     response = self.run(user_input)
    #     print(f"Response: {response}")
    #     self.text_to_speech(response)
    #     return response

    def run(self, input, route=''):

        # 1. System message
        system_msg = "You are given an image. Analyze the image and answer the question."
        system_message = system_msg + self.exam_check(route)
        messages = [
            {
                'role': 'system',
                'content': system_message
            },
        ]

        # 2. Examples
        # messages += self.search_convo_examples(input, examples=self.req_examples, num_examples=2)
        # messages += self.search_convo_examples(input)
        # messages.append({
        #     'role': 'user',
        #     'content': "END OF EXAMPLES"
        # })

        # 3. User Input
        messages.append({
            'role': 'user',
            'content': input
        })

        # 4. Start Conversation
        return self.start_dialogue(messages, route)
    
    def generate_slide_summary(self, module_name, slide_number):
        try:
            # Retrieve slide content from your data source
            db_client = GraphqlClient(self.user_info)
            imageurl_info = db_client.get_slide_info(module_name, slide_number)
            
            if not imageurl_info or len(imageurl_info) == 0:
                return "Sorry, couldn't find the slide image."
            
            slide_image_url = imageurl_info[0]['image_url']
            print("------------> Slide Image URL: ", slide_image_url)

            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful teaching assistant. Explain the content of this slide in detail."
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Please explain this slide content in detail. Include all text, diagrams, and their relationships."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": slide_image_url
                                }
                        }
                    ]
                }
            ]
            response = self.llm.invoke(messages)
            explanation = response.content
            print("------------> Explanation: ", explanation)
            return explanation

        except Exception as e:
            print(f"Error generating slide summary: {str(e)}")
            return None
    
    def run_vision(self, input, slide_info, conversation_history, route=''):

        # 1. System message
        print("##### IN DIALOUGE GEN ######")
        system_msg = "You are given an image. Analyze the image and answer the question."
        system_message = system_msg + self.exam_check(route)
        messages = [
            {
                'role': 'system',
                'content': system_message
            },
        ]

        # 2. Examples
        # messages += self.search_convo_examples(input, examples=self.req_examples, num_examples=2)
        # messages += self.search_convo_examples(input)
        # messages.append({
        #     'role': 'user',
        #     'content': "END OF EXAMPLES"
        # })

        ############## ADD FOR GPT VISION #####################
        # slide_image_url = None
        slide_image_url = "http://drive.google.com/uc?export=view&id=1yrGe-_kej1hG5h5rbTE63562UOUigx7i"

        ################ TO DO :: ADD CODE TO ASSIGN "slide_image_url" URL of image ####################
        # slide_info = {topic: this.currentTopic, module: this.currentModule, slide: this.currentSlide}
        ## Call query to get slide_image_url for particular topic, module and slide

        db_client = GraphqlClient(self.user_info)
        
        # imageurl_info = db_client.get_slide_info(slide_info["topic"], slide_info["module"], slide_info["slide"])
        imageurl_info = db_client.get_slide_info(slide_info["module"], slide_info["slide"]-1)
        print("##### slide_info ####", slide_info)
        current_slide = slide_info["slide"]

        db_client = GraphqlClient(self.user_info)
        modules = db_client.get_learning_modules()
        module_set = {}
        for module in modules:
            module_set[module['id']] = module['name']
        print("modulessssssss 1", module_set)

        # module_set = {'1':'Space Mission Overview','2':'Space Environment and Orbits','3':'Spacecraft Technologies and Architectures','4':'Satellite Scientific Payloads'}
        current_module = None
        try:
            current_module = module_set[int(slide_info["module"])]
        except:
            pass
        print("##### current_slide ####", current_slide)
        print("##### current_module ####", current_module)
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
        return self.start_dialogue(messages, current_module, current_slide, conversation_history, route)
    
    def process_references(self, answer):
        # Find all references in square brackets
        # module_patterns = [
        # r'\[Module ([^\]]+)\s+Slide\s+(\d+)\]',
        # r'\[Module Name: ([^,]+), Slide (\d+)\]',
        # r'\[([\w\s]+)\s*-\s*Slide\s*(\d+)\]',
        # r'\[Module ([^,]+), Slide (\d+)\]'
        # ]

        reference_pattern = r'\[(.*?)\]'
        matches = re.findall(reference_pattern, answer)
        
        dic = {}
        references = set()
        
        module_set = {
            'Space Mission Overview': '1',
            'Space Environment and Orbits': '2',
            'Spacecraft Technologies and Architectures': '3',
            'Satellite Scientific Payloads': '4'
        }
        
        for match in matches:
            # Split multiple references by semicolon
            refs = [ref.strip() for ref in match.split(';')]
            
            for ref in refs:
                if 'Slide' in ref:
                    # Process slide reference
                    module_name = ref.split('-')[0].strip()
                    slide_number = ref.split('Slide')[1].strip()
                    
                    if module_name not in dic and module_name in module_set:
                        url = f"http://localhost:8080/#/LearningModule/{module_name.replace(' ', '%20')}/{module_set[module_name]}/{slide_number}"
                        answer += f"\n\nReference: <a href='javascript:void(0)' onclick=\"window.location.href='{url}'\">{module_name} - Slide {slide_number}</a>"
                        dic[module_name] = True
                else:
                    # Process textbook/chapter reference
                    if "=" not in ref:
                        references.add(f"**Reference:** {ref}")
        
        if references:
            answer += "\n\n" + "\n".join(references)
        
        return answer

    def start_dialogue(self, messages, current_module, current_slide, conversation_history, route):
        # This function will loop calling the LLM until a final answer is reached
        print("##### STARTING ######",messages)
        user_message = next(msg for msg in messages if msg['role'] == 'user')
        question = user_message['content'][0]['text']

        classification_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a question classifier. 
            Determine if the question is asking about analyzing or explaining an image/graph/diagram.
            Return only 'true' or 'false'."""),
            ("user", "{question}")
        ])
        response = self.llm.invoke(
            classification_prompt.format(question=question)
        )

        if response.content.lower().strip() == 'true':
            completion = self.stream_chat_completion(messages, prefix='Convo Generator: ')
            db_client = GraphqlClient(self.user_info)
            modules = db_client.get_learning_modules()
            module_set = {}
            for module in modules:
                module_set[module['name']] = module['id']
            print("modulessssssss", module_set)
            
            # if module_name in module_set:
            url = f"/#/LearningModule/{current_module.replace(' ', '%20')}/{module_set[current_module]}/{current_slide}"
            completion += f"\n\nReference: <a href='{url}'>Module {current_module} - Slide {current_slide}</a>"

            messages.append({
                'role': 'assistant',
                'content': completion
            })
            return completion

        docs = self.rag.slides_vectorstore.similarity_search(
            question,
            k=1,
            filter={
                "slide_number": current_slide,
                "module_name": current_module
                }
        )
        print("-------------Searching Current Slide---------------\n", current_slide, current_module)
        current_slide_data = [{
                "content": doc.page_content,
                "metadata": doc.metadata
            } for doc in docs]
        
        answer = self.rag.query(question, current_module, current_slide, conversation_history, current_slide_data)
        print(f"Question: {question}")
        print(f"Final Answer: {answer}\n")

        answer = self.process_references(answer)
        
        messages.append({
            'role': 'assistant',
            'content': answer
        })

        # self.text_to_speech(answer)


        # while self.stop_condition(completion) is False:
        #     # Search Information Space
        #     module, query = self.parse_completion(completion)
        #     search_results = \
        #     self.kb_client.query({'class': module, 'query': query, 'user_info': self.user_info, 'route': route})[
        #         'formatted_results']

        #     # Get search result message
        #     if len(search_results) == 0:
        #         search_result_msg = 'NO RESULTS'
        #     else:
        #         search_result_msg = self.summary_gen.run(query, search_results, module)
        #         if 'Insufficient information' in search_result_msg:
        #             search_result_msg = 'NO RESULTS'
        #     messages.append({
        #         'role': 'user',
        #         # 'content': search_result_msg,
        #         'content': 'Query Response: ' + search_result_msg
        #     })

        #     # Get next completion
        #     completion = self.stream_chat_completion(messages, prefix='Convo Generator: ')
        #     messages.append({
        #         'role': 'assistant',
        #         'content': completion
        #     })

            # # Save messages
            # utils.write_messages_to_file(messages, self.debug_file)

        return answer

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
    llm_task = DialogueGenerator(UserInformation.objects.get(id=5))
    question = ""
    question = "How is orbit velocity calculated?"

    response = llm_task.run(question)
