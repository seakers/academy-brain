import os
import json
import datetime

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework.views import APIView
from rest_framework.response import Response

from academy_auth.helpers import get_or_create_user_information
from academy_auth.models import UserInformation
from academy_assistant.assistant.Classifier import Classifier
from academy_assistant.assistant.intents.IntentHandler import IntentHandler


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
            confidence = classifier.recommend_material(command)
            print('--> MATERIAL CONFIDENCE:', confidence)
            return Response({'response': json.dumps(confidence)})
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error classifying material: ' + str(ex)})

