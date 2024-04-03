class AbstractBuilder:

    def __init__(self, icon, topics, course=None, status=None):
        self.icon = icon
        self.topics = topics
        self.course = course
        self.status = status
        self.slides = []

        self.q_counter = 1

    def get_module(self):
        return {
            'slides': self.slides,
            'icon': self.icon,
            'slide_idx': 0,
            'topics': self.topics,
            'course': self.course,
            'status': self.status,
        }




    def add_slide(self, src, context=''):
        self.slides.append({
            'type': 'info',
            'src': src,
            'idx': len(self.slides),
            'context': context.strip()
        })

    def add_quiz_start_slide(self):
        self.slides.append({
            'type': 'quiz_start',
            'idx': len(self.slides),
            'context': 'This slide denotes the beginning of the end of module quiz. You can press the forward arrows to continue.'
        })

    def add_quiz_end_slide(self):
        self.slides.append({
            'type': 'quiz_end',
            'idx': len(self.slides),
            'context': 'This slide denotes the end of the learning module. Please proceed to take the learning module exam.'
        })

    def add_exam_start_slide(self):
        self.slides.append({
            'type': 'exam_start',
            'idx': len(self.slides),
            'context': 'This slide denotes the beginning of the module exam. You can press the forward arrows to continue.'
        })

    def add_exam_end_slide(self):
        self.slides.append({
            'type': 'exam_end',
            'idx': len(self.slides),
            'context': 'This slide denotes the end of the module exam. You can select the mastery page to view your course completion.'
        })

    def add_exam_finish_slide(self):
        self.slides.append({
            'type': 'exam_finish',
            'idx': len(self.slides),
            'context': 'This slide denotes the end of the module exam. If this is the second learning module you have studied, the experiment has finished. Else, select the continue button below to continue to the next stage.'
        })

    def add_tlx_survey_slide(self):
        self.slides.append({
            'type': 'tlx_survey',
            'idx': len(self.slides),
            'context': 'You have completed the module exam. Please alert your proctor, and you will be moved on to a brief survey.'
        })



    ###############################################
    # Context can be extracted in these functions #
    ###############################################

    def add_tf_question(self, text, answer, explanation, topics, difficulty=0.0, discrimination=0.0, graded=False):
        # --> Question Info
        question_info = {
            'type': 'question',
            'answered': False,
            'correct': False,
            'choice_id': -1,
            'idx': len(self.slides),
            'graded': graded
        }

        # --> Question
        q_text = '(T/F) ' + text
        self.q_counter += 1
        choices = [
            {'text': 'A. True', 'correct': True, 'id': 0},
            {'text': 'B. False', 'correct': False, 'id': 1},
        ]
        if answer == False:
            choices = [
                {'text': 'A. True', 'correct': False, 'id': 0},
                {'text': 'B. False', 'correct': True, 'id': 1},
            ]
        question = {
            'topics': topics,
            'text': q_text,
            'choices': choices,
            'explanation': explanation,
            'difficulty': difficulty,
            'discrimination': discrimination,
            'guessing': 0.5
        }

        question_info['question'] = question
        context = 'The user is answering the following question. ' \
                  'Do not provide the answer to it unless it has been graded:\n' + str(question)
        question_info['context'] = context
        self.slides.append(question_info)

    def add_mc_question(self, text, choices, explanation, topics, difficulty=0.0, discrimination=0.0, graded=False):
        # --> Question Info
        question_info = {
            'type': 'question',
            'answered': False,
            'correct': False,
            'choice_id': -1,
            'idx': len(self.slides),
            'graded': graded
        }

        # --> Question
        q_text = text
        self.q_counter += 1

        question = {
            'topics': topics,
            'text': q_text,
            'choices': choices,
            'explanation': explanation,
            'difficulty': difficulty,
            'discrimination': discrimination,
            'guessing': round(float(1.0 / float(len(choices))), 2)
        }

        question_info['question'] = question
        context = 'The user is answering the following question. ' \
                  'Do not provide the answer to it it has been graded:\n' + str(question)
        question_info['context'] = context
        self.slides.append(question_info)
