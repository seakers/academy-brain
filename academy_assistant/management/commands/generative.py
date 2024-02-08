import time

from django.core.management.base import BaseCommand, CommandError

from academy_assistant.assistant.Classifier import Classifier

from academy_auth.models import UserInformation
# from LLM_tasks.tutor_agent.TutorAgent import TutorAgent
from LLM_tasks.dialogue_generation.DialogueGenerator import DialogueGenerator

class Command(BaseCommand):
    help = 'Creates training data for academy models'

    def handle(self, *args, **options):


        user_info_id = 5
        user_info = UserInformation.objects.get(id=user_info_id)

        command = 'What information do you have about me?'
        route = ''

        agent = DialogueGenerator(user_info)
        agent.run(command, route)








