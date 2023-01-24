from django.core.management.base import BaseCommand, CommandError

from academy_assistant.assistant.preprocess.api import Preprocessing

class Command(BaseCommand):
    help = 'Creates training data for comet models'

    def handle(self, *args, **options):
        print('--> CREATING TRAINING DATA')
        client = Preprocessing(version='EOSS')
        client.process()








