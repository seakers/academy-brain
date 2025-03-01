from academy_assistant.database.client.modules.AbstractBuilder import AbstractBuilder



def get_module():
    builder = AbstractBuilder('mdi-tag-arrow-up', ['Work Breakdown Structure'], 'Cost Estimation')

    builder.add_slide('AERO401Slide6')
    builder.add_slide('AERO401Slide7')
    builder.add_slide('AERO401Slide30')

    return builder.get_module()




slides = [
    {
        'type': 'info',
        'src': 'AERO401Slide6',
        'idx': 0
    },
    {
            'type': 'question',
            'answered': False,
            'correct': False,
            'choice_id': -1,
            'idx': 1,
            'question': {
                'topics': ['Work Breakdown Structure'],
                'text': 'Q1. Which of these components should be accounted for in a Work Breakdown Structure?',
                'choices': [
                    {'text': 'A. Satellite OBC', 'correct': False, 'id': 0},
                    {'text': 'B. ADCS Sensors', 'correct': False, 'id': 1},
                    {'text': 'C. Solar Arrays', 'correct': False, 'id': 2},
                    {'text': 'D. All of the above', 'correct': True, 'id': 3}
                ],
                'explanation': 'A complete Work Breakdown Structure will contain all of these components. The correct answer id D',
                'difficulty': 0.0,
                'discrimination': 0.0,
                'guessing': 0.25
            }
    },
    {
        'type': 'info',
        'src': 'AERO401Slide7',
        'idx': 2
    },
    {
            'type': 'question',
            'answered': False,
            'correct': False,
            'choice_id': -1,
            'idx': 3,
            'question': {
                'topics': ['Work Breakdown Structure'],
                'text': 'Q1. Which of these components should be accounted for in a Work Breakdown Structure?',
                'choices': [
                    {'text': 'A. Satellite OBC', 'correct': False, 'id': 0},
                    {'text': 'B. ADCS Sensors', 'correct': False, 'id': 1},
                    {'text': 'C. Solar Arrays', 'correct': False, 'id': 2},
                    {'text': 'D. All of the above', 'correct': True, 'id': 3}
                ],
                'explanation': 'A complete Work Breakdown Structure will contain all of these components. The correct answer id D',
                'difficulty': 0.0,
                'discrimination': 0.0,
                'guessing': 0.25
            }
    },
    {
        'type': 'info',
        'src': 'AERO401Slide30',
        'idx': 4
    },
]


