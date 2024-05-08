import os
import json
import datetime
import re
from scipy.stats import percentileofscore

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework.views import APIView
from rest_framework.response import Response

from academy_auth.helpers import get_or_create_user_information
from academy_auth.models import UserInformation
from academy_assistant.assistant.Classifier import Classifier
from academy_assistant.assistant.intents.IntentHandler import IntentHandler

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

        db_client = GraphqlClient(user_info)
        db_client.index_action(action_desc)

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




####################
# Generative Model #
####################


class GMCommand(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        command = request.data["command"]
        route = request.data['route']
        print("############### INFO #############", request.user)
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

            ## GET USER CUSTOM MESSAGE
            db_client = GraphqlClient(user_info)
            result = db_client.get_system_message()
            print("result", result)
            custom_system_message = result[0]["system_message"]
            
            response = agent.run_vision(command, slide_info, route, custom_system_message)
            
        else:    
            response = agent.run(command, route)
        ###################################

        if 'ANSWER:' in response:
            response = response.replace('ANSWER:', '')

        # Remove UserInfo citations
        pattern = re.compile(r'\(UserInfo.*?\)')
        response = pattern.sub('', response)



        return Response({'response': response})



#########################
# System Message by User #
#########################


class SYSMessage(APIView):

    # SAVE USER SYSTEM MESSAGE
    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        message = request.data["message"]
        print(user_info.id)

        ############## SAVE SYS MESSAGE FOR USER #####################
        db_client = GraphqlClient(user_info)
        result = db_client.update_system_message(message)

        return Response({'response': 'ok'})
    
class GETSYSMessage(APIView):

    # GET USER SYSTEM MESSAGE
    def get(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        response = {
            'system_message': ""
        }

        ############## GET SYS MESSAGE FOR USER #####################
        db_client = GraphqlClient(user_info)
        result = db_client.get_system_message()
        response["system_message"] = result[0]["system_message"]

        return Response(response)
    
class GETUserReport(APIView):

    # GET USER SYSTEM MESSAGE
    def get(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        response = {
            # 'topic 1': "Percentile"
        }

        ############## GET TOPICS FOR USER WHICH HAS ABILITY PARAMS #####################
        db_client = GraphqlClient(user_info)
        user_ability_info = db_client.get_ability_levels_by_user()

        ### LOOP THROUGH ALL TOPICS AND FIND ALL USERS VALUES AND PERCENTILE ###
        for value in user_ability_info:
            ## FOR EACH TOPIC 
            # print("$$$$$", value)
            if value["value"]:
                topic_name = value["topic"]["name"]

                ## FIND ABILITY VALUES OF ALL USERS FOR THAT TOPIC AND FIND PERCENTILE
                users_topic_ability_info = db_client.get_ability_levels_by_topic(value["topic_id"])

                ## Gather all users Ability level of that topic
                print("#####", users_topic_ability_info)
                ability_list = []
                for val in users_topic_ability_info:
                    # If ability has value and that ability param is not if current user
                    if val["value"] and val["user_id"] != user_info.user.id:
                    # if val["value"] and val["user_id"] != 1:
                        ability_list.append(val["value"])

                ## For all users get percentile of the selected values
                percentile = 100
                if len(ability_list):
                    percentile = percentileofscore(ability_list, value["value"], kind='rank')

                print("########### TOPIC ################ TOPIC: {}, ability_list: {}".format(topic_name, str(ability_list)))
                ## Assign topic name with percentile
                response[topic_name] = percentile
        
        # GET TOPIC WITH LESS THAN 35 Percentile FOR WEAKNESS
        # GET TOPIC WITH GREATER THAN 65 Percentile FOR STRENGTHS

        weakness_list = []
        strength_list = []
        for topic in response:
            if response[topic] <= 35:
                weakness_list.append(topic)
            elif response[topic] >= 65:
                strength_list.append(topic)    
        response["WEAKNESS"] = weakness_list
        response["STRENGTHS"] = strength_list
        response["RECOMMENDATIONS"] = []

        print("RESPONSE", response)
        return Response(response)
