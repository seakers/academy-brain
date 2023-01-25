import time

from django.core.management.base import BaseCommand, CommandError

from academy_assistant.assistant.Classifier import Classifier

from academy_assistant.assistant.intents.IntentHandler import IntentHandler
from academy_auth.models import UserInformation


class Command(BaseCommand):
    help = 'Creates training data for academy models'

    def handle(self, *args, **options):
        command = 'what is the structures and mechanisms subsystem'


        user_info_id = 38
        user_info = UserInformation.objects.get(id=user_info_id)



        print('--> TEST COMMAND CLASSIFICATION:', command)
        start = time.time()

        classifier = Classifier(user_info, library='QA')
        print('--> CONSTRUCTOR: ', time.time() - start)

        material_result = classifier.recommend_material(command)
        print(material_result)


        # role_result = classifier.classify_role(command)
        # print('--> ROLE:', role_result, classifier.get_role(role_result))
        #
        # intent_result = classifier.classify_role_intent(command, role_result)
        # intent = classifier.get_intent(role_result, intent_result)
        # print('--> INTENT:', intent_result, intent)












