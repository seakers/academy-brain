import json

from academy_assistant.database.client.modules.lifecycle_cost import get_module as get_lc_module
from academy_assistant.database.client.modules.mission_payloads import get_module as get_rms_module
from academy_assistant.database.client.modules.parametric_ca import get_module as get_pca_module
from academy_assistant.database.client.modules.spacecraft_bus import get_module as get_sb_module

# Experiment Modules
# from academy_assistant.database.client.modules.intro_to_space import get_module as get_intro_module
# from academy_assistant.database.client.modules.space_env_and_orbits import get_module as get_orb_env_module

# Production Modules isc_smo, isc_seo, isc_sta, isc_ssp
from academy_assistant.database.client.modules.isc_smo import get_module as get_isc_smo
from academy_assistant.database.client.modules.isc_seo import get_module as get_isc_seo
from academy_assistant.database.client.modules.isc_sta import get_module as get_isc_sta
from academy_assistant.database.client.modules.isc_ssp import get_module as get_isc_ssp




class LearningModule:

    def __init__(self, client):
        self.client = client

        self.modules = {
            # 'Basics': get_basic_module(),

            # Space Training 101
            # 'Space Mission Overview': get_intro_module(),
            # 'Space Environment and Orbits': get_orb_env_module(),
            # 'Spacecraft Bus': get_sb_module(),
            # 'Mission Payloads': get_rms_module(),
            # 'Bottom Up Estimation': get_buca_module(),
            # 'Economies of Scale': get_eocl_module(),
            # 'Parametric Estimation': get_pca_module(),
            # 'Lifecycle Cost': get_lc_module(),

            # Production Modules
            'Space Mission Overview': get_isc_smo(),
            'Space Environments and Orbits': get_isc_seo(),
            'Spacecraft Technologies and Architectures': get_isc_sta(),
            'Satellite Scientific Payloads': get_isc_ssp(),
        }


    def index_info_slide(self, slide, module_id):

        # --> 1. Get user ids
        users = self.client.get_users()
        user_ids = [None]
        for user in users:
            user_ids.append(user.id)

        # --> 2. Index slide for each user
        for user_id in user_ids:
            print("######SLIDE#######", slide['image_url'])
            self.client.index_info_slide(module_id, slide['type'], slide['src'], user_id, slide['idx'], slide['context'], slide['image_url'])

    def index_question_slide(self, slide, module_id):

        # --> 1. Index question and get question_id
        question = slide['question']
        question_id = self.client.index_question(question['text'], json.dumps(question['choices']),
                                                 question['difficulty'], question['discrimination'],
                                                 question['guessing'], question['topics'], question['explanation'])

        # --> 2. Index slide for each user
        graded = slide['graded']
        users = self.client.get_users()
        user_ids = [None]
        for user in users:
            user_ids.append(user.id)
        for user_id in user_ids:
            # (self, module_id, type, question_id, answered, correct, choice_id, user_id, idx)
            self.client.index_question_slide(module_id, slide['type'], question_id, slide['answered'], slide['correct'],
                                             slide['choice_id'], user_id, slide['idx'], graded, slide['context'])

    def index_quiz_start_slide(self, slide, module_id):

        # --> 1. Get user ids
        users = self.client.get_users()
        user_ids = [None]
        for user in users:
            user_ids.append(user.id)

        # --> 2. Index slide for each user
        for user_id in user_ids:
            self.client.index_quiz_start_slide(module_id, slide['type'], user_id, slide['idx'], slide['context'])
        return 0

    def index_quiz_end_slide(self, slide, module_id):

        # --> 1. Get user ids
        users = self.client.get_users()
        user_ids = [None]
        for user in users:
            user_ids.append(user.id)

        # --> 2. Index slide for each user
        for user_id in user_ids:
            self.client.index_quiz_start_slide(module_id, slide['type'], user_id, slide['idx'], slide['context'])
        return 0

    def index_exam_finish_slide(self, slide, module_id):

        # --> 1. Get user ids
        users = self.client.get_users()
        user_ids = [None]
        for user in users:
            user_ids.append(user.id)

        # --> 2. Index slide for each user
        for user_id in user_ids:
            self.client.index_exam_finish_slide(module_id, slide['type'], user_id, slide['idx'], slide['context'])
        return 0


    def index(self):

        for module, info in self.modules.items():
            slides = info['slides']
            icon = info['icon']
            slide_idx = info['slide_idx']
            topics = info['topics']
            course = info['course']
            status = info['status']
            # --> 1. Index learning module
            module_id = self.client.index_learning_module(module, icon, topics, course, status)

            # --> 2. Index Join__User_LearningModule for all users
            for user in self.client.get_users():
                self.client.index_join_user_learning_module(user.id, module_id, slide_idx)

            # --> 3. Index Learning Module Slides
            for slide in slides:
                if slide['type'] == 'info':
                    self.index_info_slide(slide, module_id)
                elif slide['type'] == 'question':
                    self.index_question_slide(slide, module_id)
                elif slide['type'] == 'quiz_start':
                    self.index_quiz_start_slide(slide, module_id)
                elif slide['type'] == 'quiz_end':
                    self.index_quiz_end_slide(slide, module_id)
                elif slide['type'] == 'exam_finish':
                    self.index_exam_finish_slide(slide, module_id)
