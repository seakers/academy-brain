from django.core.management.base import BaseCommand, CommandError

from academy_assistant.assistant.training.api import Training

class Command(BaseCommand):
    help = 'Train comet assistant models'

    def handle(self, *args, **options):
        print('--> TRAINING MODELS')
        client = Training(version='QA')
        client.train()


