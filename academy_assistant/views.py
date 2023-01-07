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


##################################
# Called for classifying intents #
##################################

class Command(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        command = request.data["command"]

        # --> 1. Create classifier
        try:
            print('--> PROCESSING COMMAND: ', command)
            classifier = Classifier(library='EOSS')
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
        except Exception as ex:
            print(ex)
            return Response({'response_status': 'error', 'message': 'Error processing intent: ' + str(ex)})

        # --> 5. Return ok
        return Response({'response_status': 'ok', 'message': str(datetime.datetime.now()), 'result': json.dumps(result_obj)})




class LMCommand2(APIView):

    def post(self, request, format=None):

        user_info = get_or_create_user_information(request.session, request.user)
        command = request.data["command"]

        # --> 1. Create classifier
        try:
            print('--> PROCESSING COMMAND: ', command)
            classifier = Classifier(library='CA')
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







#################################################################
# Called for classifying slides with relevant learning material #
#################################################################

class LMCommand(APIView):
    daphne_version = "CA"
    command_options = ['Spacecraft Bus', 'Mission Payloads', 'Parametric Estimation', 'Lifecycle Cost']
    condition_names = ['Spacecraft Bus', 'Mission Payloads', 'Parametric Estimation', 'Lifecycle Cost']

    def post(self, request, format=None):
        print('--> PROCESSING LM COMMAND')
        user_info = get_or_create_user_information(request.session, request.user, self.daphne_version)

        # --> Process command and return
        confidence = self.process_command(user_info, request)
        return Response({'response': json.dumps(confidence)})


    def process_command(self, user_info, request):
        context_client = ContextClient(user_info)
        context = context_client.context

        # --> 1. Create command object
        command = Command(request.data['command'])
        command = command.set_session(request.session)
        command = command.set_user_info(user_info)
        command = command.set_context_client(context_client)
        command = command.set_roles(self.command_options)
        command = command.set_conditions(self.condition_names)
        command = command.set_version(self.daphne_version)

        # --> 2. Classify command (no need to process intents)
        client = CommandClassifier(command, daphne_version='CA')
        client.classify(max_role_matches=4)

        # --> 3. Return confidence levels for learning modules and slides
        confidence = client.get_prediction_confidence()
        return confidence
