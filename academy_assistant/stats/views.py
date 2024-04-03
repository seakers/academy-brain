import json

from distutils.util import strtobool

from rest_framework.views import APIView
from rest_framework.response import Response
from academy_auth.helpers import get_or_create_user_information

from academy_assistant.stats.api import StatsClient
from academy_assistant.database.client.GraphqlClient import GraphqlClient


class UpdateModel(APIView):

    def post(self, request, format=None):
        print('--> UPDAING CA MODEL')

        user_info = get_or_create_user_information(request.session, request.user)
        slide = json.loads(request.data['slide'])

        # --> 1. Determine topics to update
        graphql_client = GraphqlClient(user_info)
        question_info = graphql_client.get_ca_question_topics(slide['question']['id'])
        topic_ids = [int(x['topic']['id']) for x in question_info['topics']]

        # --> 2. Update ability model for each topic
        stats_client = StatsClient(user_info)
        for topic_id in topic_ids:
            stats_client.update_model(topic_id)

        return Response({})


class UpdateModelTID(APIView):

    def post(self, request, format=None):
        user_info = get_or_create_user_information(request.session, request.user)
        stats_client = StatsClient(user_info)
        topic_ids = json.loads(request.data['topic_ids'])
        question_ids = json.loads(request.data['question_ids']) # [question_ids, 1 or 0]

        print('--> UPDAING CA MODEL', topic_ids)
        for topic_id in topic_ids:
            stats_client.update_model(topic_id)

        # UPDATING AB PARAMETER OF QUESTION
        print('--> UPDAING QUESTION a,b', question_ids)
        stats_client.update_parameter_model(question_ids)

        return Response({})


class AdaptiveQuestion(APIView):

    def post(self, request, format=None):
        print('\n----- GETTING ADAPTIVE QUESTION -----')

        user_info = get_or_create_user_information(request.session, request.user)
        stats_client = StatsClient(user_info)
        topics = json.loads(request.data['topics'])

        question = stats_client.select_question()

        return Response(question)
