import os
import json
import datetime
import re

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI
from django.http import HttpResponse, StreamingHttpResponse

from academy_auth.helpers import get_or_create_user_information
from academy_auth.models import UserInformation
from academy_assistant.assistant.Classifier import Classifier
from academy_assistant.assistant.intents.IntentHandler import IntentHandler
from academy_assistant.database.graphql import GraphqlClient

from LLM_tasks.tutor_agent.TutorAgent import TutorAgent
from LLM_tasks.dialogue_generation.DialogueGenerator import DialogueGenerator

from academy_assistant.database.graphql import GraphqlClient
# from academy_assistant.database.index import experiment_users


experiment_user_1 = {
    'username': 'exuser1',
    'email': 'exuser1@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True
}
experiment_user_2 = {
    'username': 'exuser2',
    'email': 'exuser2@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False
}
experiment_users = [
    experiment_user_1,
    experiment_user_2
]



class Action(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        action_desc = request.data["description"]
        print("action", action_desc)

        db_client = GraphqlClient(user_info)
        db_client.index_action(action_desc)
        print("db client", db_client)

        return Response({'response': 'ok'})



class ExperimentInfo(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        username = user_info.user.username

        experiment_info = ''
        for user in experiment_users:
            if username == user['username']:
                experiment_info = {
                    'task_order': user['task_order'],
                    'assistant': user['assistant']
                }

        # Stringify info
        info = json.dumps(experiment_info)
        return Response({'response': 'ok', 'info': info})















#########################################
# Called for returning textual response #
#########################################

class Command(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        command = request.data["command"]

        # --> 1. Create classifier
        try:
            print('--> PROCESSING COMMAND: ', command)
            classifier = Classifier(user_info, library='QA')
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error creating classifier: ' + str(ex)})

        # --> 2. Classify role
        try:
            role_result = classifier.classify_role(command)
            role = classifier.get_role(role_result)
            print('--> ROLE:', role)
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error classifying role: ' + str(ex)})

        # --> 3. Classify intent
        try:
            intent_result = classifier.classify_role_intent(command, role_result)
            intent = classifier.get_intent(role, intent_result)
            print('--> INTENT:', intent)
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error classifying intent: ' + str(ex)})

        # --> 4. Handle intent and insert response
        result_obj = {}
        try:
            intent_handler = IntentHandler(user_info, command, intent)
            result = intent_handler.process()
            if result is not None:
                result_obj = result
            return Response({'response_status': 'ok', 'response': json.dumps(result_obj)})
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error processing intent: ' + str(ex)})




####################################
# Called for recommending material #
####################################

class LMCommand(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        command = request.data["command"]

        # --> 1. Create classifier
        try:
            print('--> PROCESSING COMMAND: ', command)
            classifier = Classifier(user_info, library='MR')
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error creating classifier: ' + str(ex)})

        # --> 2. Get all classifications
        try:
            print('--> GETTING RECOMMENDED MATERIAL')
            confidence = classifier.recommend_material(command)
            print('--> MATERIAL CONFIDENCE:', confidence)
            return Response({'response': json.dumps(confidence)})
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error classifying material: ' + str(ex)})


####################################
# Called for audio transcribing #
####################################

class TranscribeAudio(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        command = request.data["audio"]
        print("came here to post audio")

        # --> 1. Create classifier
        try:
            print('--> PROCESSING COMMAND: ', command)
            agent = DialogueGenerator(user_info)
            transcribed_text = agent.speech_to_text(command)
            return Response({
                'response': transcribed_text
            })
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=500)
        
####################################
#    Called for Text to speech    #
####################################

def audio_chunk_generator(content, chunk_size=4096):
    for i in range(0, len(content), chunk_size):
        yield content[i:i + chunk_size]

class TextToSpeech(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        print(request.data)
        command = request.data["audio_text"]
        print("came here to post audio")
        if not command:
            return Response({"error": "No text provided"}, status=400)

        # --> 1. Create classifier
        try:
            print('--> PROCESSING COMMAND: ', command)
            agent = DialogueGenerator(user_info)
            client = OpenAI()
            response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=command,
            )
            print("audio response", response)
            return StreamingHttpResponse(
                audio_chunk_generator(response.content),
                content_type="audio/mp3"
            )
            # print("audio response created, returning stream")
            # return StreamingHttpResponse(
            #     response.iter_bytes(chunk_size=4096),  # Use iter_bytes instead of our custom function
            #     content_type="audio/mp3"
            # )
            # def stream_generator():
            #     # Get binary stream of audio data
            #     for chunk in response.iter_bytes(chunk_size=4096):
            #         yield chunk
            
            # print("audio response created, returning stream")
            # # Return a streaming response with the audio data
            # return StreamingHttpResponse(
            #     stream_generator(),
            #     content_type="audio/mp3"
            # )
        
        except Exception as e:
            return Response({"error": str(e)}, status=500)

####################################
# Called for explaining Slide #
####################################

class ExplainSlide(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        slide_info = json.loads(request.data['slide_info'])
        module_id = slide_info.get('module')
        slide_number = slide_info.get('slide')
        print("explaining slide", slide_info)
        db_client = GraphqlClient(user_info)
        try:
            existing_explanation = db_client.get_slide_explanation(module_id, slide_number)
            print("existing explanation", existing_explanation)
            if existing_explanation:
                    summary = existing_explanation
                    print("Retrieved existing explanation for Module='%s', Slide='%d'.", module_id, slide_number)
                    return Response({'response': summary})

            agent = DialogueGenerator(user_info)
            print("generating slide summary", slide_info['module'], slide_info['slide'])
            summary = agent.generate_slide_summary(slide_info['module'], slide_info['slide'])
            if summary:
                db_client.store_slide_explanation(
                        module_id=module_id,
                        slide_number=slide_number,
                        explanation=summary
                    )
                print("Stored new explanation for Module='%s', Slide='%d'.", module_id, slide_number)
                    
                return Response({'response': summary})
            else:
                return Response(
                    {'response_status': 'error', 'message': 'Could not generate summary.'},
                    status=500
                )
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=500)


####################
# Generative Model #
####################


class GMCommand(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        command = request.data["command"]
        route = request.data['route']
        print(user_info)
        # print(user_info.keys())
        # print(user_info.user)
        print(request.user)
        print(user_info.id)
        print(request.data)
        # tutor = TutorAgent(user_info)
        # response = tutor.run(command, route)

        agent = DialogueGenerator(user_info)
        response = None

        ############## ADD FOR GPT VISION #####################
        print("############### GOING FOR VISION ##############")
        # print(request.data['slide_info'][0])
        print(request.data['vision'][0])
        print(json.loads(request.data['slide_info']))
        print("vision" in request.data)

        if "vision" in request.data and str(request.data['vision']) == "true":
            slide_info = json.loads(request.data['slide_info'])
            print(slide_info["topic"])
            conversation_history = json.loads(request.data['conversation_history'])
            print("############### VISION ############")
            response = agent.run_vision(command, slide_info, conversation_history, route)
            print("###################### FINAL RESPONSE ###############", response)
            
        else:    
            print("############### NO VISION ############")
            conversation_history = json.loads(request.data['conversation_history'])
            response = agent.run(command, route)
        ###################################

        if 'ANSWER:' in response:
            response = response.replace('ANSWER:', '')

        # Remove UserInfo citations
        pattern = re.compile(r'\(UserInfo.*?\)')
        response = pattern.sub('', response)



        return Response({'response': response})



