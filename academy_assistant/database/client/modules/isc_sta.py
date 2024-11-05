from academy_assistant.database.client.modules.AbstractBuilder import AbstractBuilder
slide_text = ['']
import os
slide_text_dir = os.path.join('/home/ec2-user/academy-brain/academy_assistant/database/client/modules/slide_text', 'sta')

# Iterate over all txt files in slide_text_dir
for file in os.listdir(slide_text_dir):
    if file.endswith('.txt'):
        with open(os.path.join(slide_text_dir, file), 'r') as f:
            slide_text.append(f.read())

def get_module():
    builder = AbstractBuilder('mdi-satellite-variant', ['Power', 'Thermal', 'ADCS', 'Propulsion', 'Avionics', 'Communications', 'Structures'], 'Intro to Space Commodities', None)

    # From slide 1 to slide 114
    builder.add_slide('ISC_STA_1', slide_text[1], "https://academy2.selva-research.com/images/sta/Slide1.png")
    builder.add_slide('ISC_STA_2', slide_text[2], "https://academy2.selva-research.com/images/sta/Slide2.png")
    builder.add_slide('ISC_STA_3', slide_text[3], "https://academy2.selva-research.com/images/sta/Slide3.png")
    builder.add_slide('ISC_STA_4', slide_text[4], "https://academy2.selva-research.com/images/sta/Slide4.png")
    builder.add_slide('ISC_STA_5', slide_text[5], "https://academy2.selva-research.com/images/sta/Slide5.png")
    builder.add_slide('ISC_STA_6', slide_text[6], "https://academy2.selva-research.com/images/sta/Slide6.png")
    builder.add_slide('ISC_STA_7', slide_text[7], "https://academy2.selva-research.com/images/sta/Slide7.png")
    builder.add_slide('ISC_STA_8', slide_text[8], "https://academy2.selva-research.com/images/sta/Slide8.png")
    builder.add_slide('ISC_STA_9', slide_text[9], "https://academy2.selva-research.com/images/sta/Slide9.png")
    builder.add_slide('ISC_STA_10', slide_text[10], "https://academy2.selva-research.com/images/sta/Slide10.png")
    builder.add_slide('ISC_STA_11', slide_text[11], "https://academy2.selva-research.com/images/sta/Slide11.png")
    builder.add_slide('ISC_STA_12', slide_text[12], "https://academy2.selva-research.com/images/sta/Slide12.png")
    builder.add_slide('ISC_STA_13', slide_text[13], "https://academy2.selva-research.com/images/sta/Slide13.png")
    builder.add_slide('ISC_STA_14', slide_text[14], "https://academy2.selva-research.com/images/sta/Slide14.png")
    builder.add_slide('ISC_STA_15', slide_text[15], "https://academy2.selva-research.com/images/sta/Slide15.png")
    builder.add_slide('ISC_STA_16', slide_text[16], "https://academy2.selva-research.com/images/sta/Slide16.png")
    builder.add_slide('ISC_STA_17', slide_text[17], "https://academy2.selva-research.com/images/sta/Slide17.png")
    builder.add_slide('ISC_STA_18', slide_text[18], "https://academy2.selva-research.com/images/sta/Slide18.png")
    builder.add_slide('ISC_STA_19', slide_text[19], "https://academy2.selva-research.com/images/sta/Slide19.png")
    builder.add_slide('ISC_STA_20', slide_text[20], "https://academy2.selva-research.com/images/sta/Slide20.png")
    builder.add_slide('ISC_STA_21', slide_text[21], "https://academy2.selva-research.com/images/sta/Slide21.png")
    builder.add_slide('ISC_STA_22', slide_text[22], "https://academy2.selva-research.com/images/sta/Slide22.png")
    builder.add_slide('ISC_STA_23', slide_text[23], "https://academy2.selva-research.com/images/sta/Slide23.png")
    builder.add_slide('ISC_STA_24', slide_text[24], "https://academy2.selva-research.com/images/sta/Slide24.png")
    builder.add_slide('ISC_STA_25', slide_text[25], "https://academy2.selva-research.com/images/sta/Slide25.png")
    builder.add_slide('ISC_STA_26', slide_text[26], "https://academy2.selva-research.com/images/sta/Slide26.png")
    builder.add_slide('ISC_STA_27', slide_text[27], "https://academy2.selva-research.com/images/sta/Slide27.png")
    builder.add_slide('ISC_STA_28', slide_text[28], "https://academy2.selva-research.com/images/sta/Slide28.png")
    builder.add_slide('ISC_STA_29', slide_text[29], "https://academy2.selva-research.com/images/sta/Slide29.png")
    builder.add_slide('ISC_STA_30', slide_text[30], "https://academy2.selva-research.com/images/sta/Slide30.png")
    builder.add_slide('ISC_STA_31', slide_text[31], "https://academy2.selva-research.com/images/sta/Slide31.png")
    builder.add_slide('ISC_STA_32', slide_text[32], "https://academy2.selva-research.com/images/sta/Slide32.png")
    builder.add_slide('ISC_STA_33', slide_text[33], "https://academy2.selva-research.com/images/sta/Slide33.png")
    builder.add_slide('ISC_STA_34', slide_text[34], "https://academy2.selva-research.com/images/sta/Slide34.png")
    builder.add_slide('ISC_STA_35', slide_text[35], "https://academy2.selva-research.com/images/sta/Slide35.png")
    builder.add_slide('ISC_STA_36', slide_text[36], "https://academy2.selva-research.com/images/sta/Slide36.png")
    builder.add_slide('ISC_STA_37', slide_text[37], "https://academy2.selva-research.com/images/sta/Slide37.png")
    builder.add_slide('ISC_STA_38', slide_text[38], "https://academy2.selva-research.com/images/sta/Slide38.png")
    builder.add_slide('ISC_STA_39', slide_text[39], "https://academy2.selva-research.com/images/sta/Slide39.png")
    builder.add_slide('ISC_STA_40', slide_text[40], "https://academy2.selva-research.com/images/sta/Slide40.png")
    builder.add_slide('ISC_STA_41', slide_text[41], "https://academy2.selva-research.com/images/sta/Slide41.png")
    builder.add_slide('ISC_STA_42', slide_text[42], "https://academy2.selva-research.com/images/sta/Slide42.png")
    builder.add_slide('ISC_STA_43', slide_text[43], "https://academy2.selva-research.com/images/sta/Slide43.png")
    builder.add_slide('ISC_STA_44', slide_text[44], "https://academy2.selva-research.com/images/sta/Slide44.png")
    builder.add_slide('ISC_STA_45', slide_text[45], "https://academy2.selva-research.com/images/sta/Slide45.png")
    builder.add_slide('ISC_STA_46', slide_text[46], "https://academy2.selva-research.com/images/sta/Slide46.png")
    builder.add_slide('ISC_STA_47', slide_text[47], "https://academy2.selva-research.com/images/sta/Slide47.png")
    builder.add_slide('ISC_STA_48', slide_text[48], "https://academy2.selva-research.com/images/sta/Slide48.png")
    builder.add_slide('ISC_STA_49', slide_text[49], "https://academy2.selva-research.com/images/sta/Slide49.png")
    builder.add_slide('ISC_STA_50', slide_text[50], "https://academy2.selva-research.com/images/sta/Slide50.png")
    builder.add_slide('ISC_STA_51', slide_text[51], "https://academy2.selva-research.com/images/sta/Slide51.png")
    builder.add_slide('ISC_STA_52', slide_text[52], "https://academy2.selva-research.com/images/sta/Slide52.png")
    builder.add_slide('ISC_STA_53', slide_text[53], "https://academy2.selva-research.com/images/sta/Slide53.png")
    builder.add_slide('ISC_STA_54', slide_text[54], "https://academy2.selva-research.com/images/sta/Slide54.png")
    builder.add_slide('ISC_STA_55', slide_text[55], "https://academy2.selva-research.com/images/sta/Slide55.png")
    builder.add_slide('ISC_STA_56', slide_text[56], "https://academy2.selva-research.com/images/sta/Slide56.png")
    builder.add_slide('ISC_STA_57', slide_text[57], "https://academy2.selva-research.com/images/sta/Slide57.png")
    builder.add_slide('ISC_STA_58', slide_text[58], "https://academy2.selva-research.com/images/sta/Slide58.png")
    builder.add_slide('ISC_STA_59', slide_text[59], "https://academy2.selva-research.com/images/sta/Slide59.png")
    builder.add_slide('ISC_STA_60', slide_text[60], "https://academy2.selva-research.com/images/sta/Slide60.png")
    builder.add_slide('ISC_STA_61', slide_text[61], "https://academy2.selva-research.com/images/sta/Slide61.png")
    builder.add_slide('ISC_STA_62', slide_text[62], "https://academy2.selva-research.com/images/sta/Slide62.png")
    builder.add_slide('ISC_STA_63', slide_text[63], "https://academy2.selva-research.com/images/sta/Slide63.png")
    builder.add_slide('ISC_STA_64', slide_text[64], "https://academy2.selva-research.com/images/sta/Slide64.png")
    builder.add_slide('ISC_STA_65', slide_text[65], "https://academy2.selva-research.com/images/sta/Slide65.png")
    builder.add_slide('ISC_STA_66', slide_text[66], "https://academy2.selva-research.com/images/sta/Slide66.png")
    builder.add_slide('ISC_STA_67', slide_text[67], "https://academy2.selva-research.com/images/sta/Slide67.png")
    builder.add_slide('ISC_STA_68', slide_text[68], "https://academy2.selva-research.com/images/sta/Slide68.png")
    builder.add_slide('ISC_STA_69', slide_text[69], "https://academy2.selva-research.com/images/sta/Slide69.png")
    builder.add_slide('ISC_STA_70', slide_text[70], "https://academy2.selva-research.com/images/sta/Slide70.png")
    builder.add_slide('ISC_STA_71', slide_text[71], "https://academy2.selva-research.com/images/sta/Slide71.png")
    builder.add_slide('ISC_STA_72', slide_text[72], "https://academy2.selva-research.com/images/sta/Slide72.png")
    builder.add_slide('ISC_STA_73', slide_text[73], "https://academy2.selva-research.com/images/sta/Slide73.png")
    builder.add_slide('ISC_STA_74', slide_text[74], "https://academy2.selva-research.com/images/sta/Slide74.png")
    builder.add_slide('ISC_STA_75', slide_text[75], "https://academy2.selva-research.com/images/sta/Slide75.png")
    builder.add_slide('ISC_STA_76', slide_text[76], "https://academy2.selva-research.com/images/sta/Slide76.png")
    builder.add_slide('ISC_STA_77', slide_text[77], "https://academy2.selva-research.com/images/sta/Slide77.png")
    builder.add_slide('ISC_STA_78', slide_text[78], "https://academy2.selva-research.com/images/sta/Slide78.png")
    builder.add_slide('ISC_STA_79', slide_text[79], "https://academy2.selva-research.com/images/sta/Slide79.png")
    builder.add_slide('ISC_STA_80', slide_text[80], "https://academy2.selva-research.com/images/sta/Slide80.png")
    builder.add_slide('ISC_STA_81', slide_text[81], "https://academy2.selva-research.com/images/sta/Slide81.png")
    builder.add_slide('ISC_STA_82', slide_text[82], "https://academy2.selva-research.com/images/sta/Slide82.png")
    builder.add_slide('ISC_STA_83', slide_text[83], "https://academy2.selva-research.com/images/sta/Slide83.png")
    builder.add_slide('ISC_STA_84', slide_text[84], "https://academy2.selva-research.com/images/sta/Slide84.png")
    builder.add_slide('ISC_STA_85', slide_text[85], "https://academy2.selva-research.com/images/sta/Slide85.png")
    builder.add_slide('ISC_STA_86', slide_text[86], "https://academy2.selva-research.com/images/sta/Slide86.png")
    builder.add_slide('ISC_STA_87', slide_text[87], "https://academy2.selva-research.com/images/sta/Slide87.png")
    builder.add_slide('ISC_STA_88', slide_text[88], "https://academy2.selva-research.com/images/sta/Slide88.png")
    builder.add_slide('ISC_STA_89', slide_text[89], "https://academy2.selva-research.com/images/sta/Slide89.png")
    builder.add_slide('ISC_STA_90', slide_text[90], "https://academy2.selva-research.com/images/sta/Slide90.png")
    builder.add_slide('ISC_STA_91', slide_text[91], "https://academy2.selva-research.com/images/sta/Slide91.png")
    builder.add_slide('ISC_STA_92', slide_text[92], "https://academy2.selva-research.com/images/sta/Slide92.png")
    builder.add_slide('ISC_STA_93', slide_text[93], "https://academy2.selva-research.com/images/sta/Slide93.png")
    builder.add_slide('ISC_STA_94', slide_text[94], "https://academy2.selva-research.com/images/sta/Slide94.png")
    builder.add_slide('ISC_STA_95', slide_text[95], "https://academy2.selva-research.com/images/sta/Slide95.png")
    builder.add_slide('ISC_STA_96', slide_text[96], "https://academy2.selva-research.com/images/sta/Slide96.png")
    builder.add_slide('ISC_STA_97', slide_text[97], "https://academy2.selva-research.com/images/sta/Slide97.png")
    builder.add_slide('ISC_STA_98', slide_text[98], "https://academy2.selva-research.com/images/sta/Slide98.png")
    builder.add_slide('ISC_STA_99', slide_text[99], "https://academy2.selva-research.com/images/sta/Slide99.png")
    builder.add_slide('ISC_STA_100', slide_text[100], "https://academy2.selva-research.com/images/sta/Slide100.png")
    builder.add_slide('ISC_STA_101', slide_text[101], "https://academy2.selva-research.com/images/sta/Slide101.png")
    builder.add_slide('ISC_STA_102', slide_text[102], "https://academy2.selva-research.com/images/sta/Slide102.png")
    builder.add_slide('ISC_STA_103', slide_text[103], "https://academy2.selva-research.com/images/sta/Slide103.png")
    builder.add_slide('ISC_STA_104', slide_text[104], "https://academy2.selva-research.com/images/sta/Slide104.png")
    builder.add_slide('ISC_STA_105', slide_text[105], "https://academy2.selva-research.com/images/sta/Slide105.png")
    builder.add_slide('ISC_STA_106', slide_text[106], "https://academy2.selva-research.com/images/sta/Slide106.png")
    builder.add_slide('ISC_STA_107', slide_text[107], "https://academy2.selva-research.com/images/sta/Slide107.png")
    builder.add_slide('ISC_STA_108', slide_text[108], "https://academy2.selva-research.com/images/sta/Slide108.png")
    builder.add_slide('ISC_STA_109', slide_text[109], "https://academy2.selva-research.com/images/sta/Slide109.png")
    builder.add_slide('ISC_STA_110', slide_text[110], "https://academy2.selva-research.com/images/sta/Slide110.png")
    builder.add_slide('ISC_STA_111', slide_text[111], "https://academy2.selva-research.com/images/sta/Slide111.png")
    builder.add_slide('ISC_STA_112', slide_text[112], "https://academy2.selva-research.com/images/sta/Slide112.png")
    builder.add_slide('ISC_STA_113', slide_text[113], "https://academy2.selva-research.com/images/sta/Slide113.png")
    builder.add_slide('ISC_STA_114', slide_text[114], "https://academy2.selva-research.com/images/sta/Slide114.png")
    builder.add_slide('ISC_STA_115', slide_text[115], "https://academy2.selva-research.com/images/sta/Slide115.png")
    builder.add_slide('ISC_STA_116', slide_text[116], "https://academy2.selva-research.com/images/sta/Slide116.png")
    builder.add_slide('ISC_STA_117', slide_text[117], "https://academy2.selva-research.com/images/sta/Slide117.png")
    builder.add_slide('ISC_STA_118', slide_text[118], "https://academy2.selva-research.com/images/sta/Slide118.png")
    builder.add_slide('ISC_STA_119', slide_text[119], "https://academy2.selva-research.com/images/sta/Slide119.png")
    builder.add_slide('ISC_STA_120', slide_text[120], "https://academy2.selva-research.com/images/sta/Slide120.png")
    builder.add_slide('ISC_STA_121', slide_text[121], "https://academy2.selva-research.com/images/sta/Slide121.png")
    builder.add_slide('ISC_STA_122', slide_text[122], "https://academy2.selva-research.com/images/sta/Slide122.png")
    builder.add_slide('ISC_STA_123', slide_text[123], "https://academy2.selva-research.com/images/sta/Slide123.png")
    builder.add_slide('ISC_STA_124', slide_text[124], "https://academy2.selva-research.com/images/sta/Slide124.png")
    builder.add_slide('ISC_STA_125', slide_text[125], "https://academy2.selva-research.com/images/sta/Slide125.png")
    builder.add_slide('ISC_STA_126', slide_text[126], "https://academy2.selva-research.com/images/sta/Slide126.png")
    builder.add_slide('ISC_STA_127', slide_text[127], "https://academy2.selva-research.com/images/sta/Slide127.png")
    builder.add_slide('ISC_STA_128', slide_text[128], "https://academy2.selva-research.com/images/sta/Slide128.png")
    builder.add_slide('ISC_STA_129', slide_text[129], "https://academy2.selva-research.com/images/sta/Slide129.png")

    builder.add_quiz_start_slide()

    # Question 1
    builder.add_mc_question(
        'What is likely the most important cost driver for the electrical power system?',
        [
            {'text': 'Power budget', 'correct': False, 'id': 0},
            {'text': 'Spacecraft launch mass', 'correct': True, 'id': 1},
            {'text': 'Orbit inclination', 'correct': False, 'id': 2},
            {'text': 'Lifetime', 'correct': False, 'id': 3}
        ],
        '',
        ['Power'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 2
    builder.add_mc_question(
        'Which of the following actions would likely decrease the EPS mass.',
        [
            {'text': 'Decrease the theoretical solar cell efficiency', 'correct': False, 'id': 0},
            {'text': 'Move to an orbit with fewer and shorter eclipses', 'correct': True, 'id': 1},
            {'text': 'Increase the spacecraft design lifetime', 'correct': False, 'id': 2},
            {'text': 'All of the above', 'correct': False, 'id': 3}
        ],
        '',
        ['Power'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 3
    builder.add_mc_question(
        'For which orbit would you expect a greater Depth of Discharge (DOD)?',
        [
            {'text': 'LEO', 'correct': False, 'id': 0},
            {'text': 'MEO', 'correct': False, 'id': 1},
            {'text': 'SSO', 'correct': False, 'id': 2},
            {'text': 'GEO', 'correct': True, 'id': 3}
        ],
        '',
        ['Power'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 4
    builder.add_mc_question(
        'Which of the following are the main cost drivers for the ADCS?',
        [
            {'text': 'Drift and pointing accuracy', 'correct': False, 'id': 0},
            {'text': 'Agility and pointing accuracy', 'correct': True, 'id': 1},
            {'text': 'Drift and Agility', 'correct': False, 'id': 2},
            {'text': 'Range and Drift', 'correct': False, 'id': 3}
        ],
        '',
        ['ADCS'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 5
    builder.add_mc_question(
        'Which of the following sensors would be expected to be the most expensive?',
        [
            {'text': 'Sun sensor', 'correct': False, 'id': 0},
            {'text': 'Star sensor/tracker', 'correct': True, 'id': 1},
            {'text': 'Horizon sensor', 'correct': False, 'id': 2},
            {'text': 'Magnetometer', 'correct': False, 'id': 3}
        ],
        '',
        ['ADCS'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )
    
    builder.add_quiz_end_slide()

    # Question 6
    builder.add_mc_question(
        'What actuator would you use for a mission that requires a torque of several Nm?',
        [
            {'text': 'Reaction wheels', 'correct': False, 'id': 0},
            {'text': 'Magnetic torquers', 'correct': False, 'id': 1},
            {'text': 'Control Moment Gyros', 'correct': True, 'id': 2},
            {'text': 'Momentum wheels', 'correct': False, 'id': 3}
        ],
        '',
        ['ADCS'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 7
    builder.add_mc_question(
        'Which of the following would you not expect to see in a delta V budget?',
        [
            {'text': 'Station keeping', 'correct': False, 'id': 0},
            {'text': 'Collision avoidance', 'correct': False, 'id': 1},
            {'text': 'Deorbiting', 'correct': False, 'id': 2},
            {'text': 'Communications', 'correct': True, 'id': 3}
        ],
        '',
        ['Propulsion'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 8
    builder.add_mc_question(
        'What is the significance of the minimum impulse bit?',
        [
            {'text': 'The smallest delta V needed for a mission', 'correct': False, 'id': 0},
            {'text': 'The smallest fuel efficiency at a point during the mission', 'correct': False, 'id': 1},
            {'text': 'The smallest amount of delta V a system can provide', 'correct': True, 'id': 2},
            {'text': 'The smallest burn time if executed on time', 'correct': False, 'id': 3}
        ],
        '',
        ['Propulsion'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 9
    builder.add_mc_question(
        'Which is a key difference between electric propulsion and chemical propulsion?',
        [
            {'text': 'Electric propulsion is more reliable', 'correct': False, 'id': 0},
            {'text': 'Electric propulsion is more fuel-efficient', 'correct': True, 'id': 1},
            {'text': 'Electric propulsion is more efficient with respect to electrical power', 'correct': False,
             'id': 2},
            {'text': 'Electric propulsion produces more thrust', 'correct': False, 'id': 3}
        ],
        '',
        ['Propulsion'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 10
    builder.add_mc_question(
        'Which one best describes a space radiator?',
        [
            {'text': 'A heat exchanger on the outer surface to radiate excess heat into space', 'correct': True,
             'id': 0},
            {'text': 'A heat exchanger that radiates heat to colder internal components', 'correct': False, 'id': 1},
            {'text': 'A layer of thermal insulation on the outside of a spacecraft', 'correct': False, 'id': 2},
            {'text': 'None of the above', 'correct': False, 'id': 3}
        ],
        '',
        ['Thermal'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 11
    builder.add_mc_question(
        'Which of the following is not a way a spacecraft in space receives heat?',
        [
            {'text': 'Direct solar irradiance', 'correct': False, 'id': 0},
            {'text': 'Reflected sunlight (albedo)', 'correct': False, 'id': 1},
            {'text': 'Thermal emission from earth', 'correct': False, 'id': 2},
            {'text': 'Convection', 'correct': True, 'id': 3}
        ],
        '',
        ['Thermal'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 12
    builder.add_mc_question(
        'Which of the following is not a passive thermal control technology?',
        [
            {'text': 'Doubler', 'correct': False, 'id': 0},
            {'text': 'Heater', 'correct': True, 'id': 1},
            {'text': 'MLI', 'correct': False, 'id': 2},
            {'text': 'Paint', 'correct': False, 'id': 3}
        ],
        '',
        ['Thermal'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 13
    builder.add_mc_question(
        'What factor below is more likely to drive TT&C cost?',
        [
            {'text': 'Downlink data rate', 'correct': True, 'id': 0},
            {'text': 'A/D conversion', 'correct': False, 'id': 1},
            {'text': 'Modulation', 'correct': False, 'id': 2},
            {'text': 'Channel coding', 'correct': False, 'id': 3}
        ],
        '',
        ['Communications'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 14
    builder.add_mc_question(
        'What does the bit error rate depend on?',
        [
            {'text': 'signal to noise ratio', 'correct': False, 'id': 0},
            {'text': 'the modulation and data coding schemes chosen', 'correct': False, 'id': 1},
            {'text': 'both a and b', 'correct': True, 'id': 2},
            {'text': 'A and B minus the coding schemes', 'correct': False, 'id': 3}
        ],
        '',
        ['Communications'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 15
    builder.add_mc_question(
        'Which antenna type is likely more appropriate for a LEO imaging satellite?',
        [
            {'text': 'An isotropic antenna', 'correct': False, 'id': 0},
            {'text': 'A dipole antenna', 'correct': False, 'id': 1},
            {'text': 'A patch antenna', 'correct': True, 'id': 2},
            {'text': 'A ~3-meter parabolic antenna', 'correct': False, 'id': 3}
        ],
        '',
        ['Communications'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 16
    builder.add_mc_question(
        'Which of the following is not a requirement for structures, mechanisms and configurations?',
        [
            {'text': 'Avoid thermal deformations', 'correct': False, 'id': 0},
            {'text': 'Manufacturability and accessibility', 'correct': False, 'id': 1},
            {'text': 'shielding from the space environment', 'correct': False, 'id': 2},
            {'text': 'all of them are', 'correct': True, 'id': 3}
        ],
        '',
        ['Structures'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 17
    builder.add_mc_question(
        'What is most likely to be the main cost driver for the spacecraft structure?',
        [
            {'text': 'Mass', 'correct': True, 'id': 0},
            {'text': 'Spacecraft power', 'correct': False, 'id': 1},
            {'text': 'Communications data rate', 'correct': False, 'id': 2},
            {'text': 'Delta V', 'correct': False, 'id': 3}
        ],
        '',
        ['Structures'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 18
    builder.add_mc_question(
        'What is the significance of fundamental frequency?',
        [
            {'text': 'It is important that it does not lie close to the fundamental frequencies of the launch vehicle',
             'correct': True, 'id': 0},
            {'text': 'It can be used to predict what the best frequency is to transmit data.', 'correct': False,
             'id': 1},
            {'text': 'It is used to determine the frequency of vibrations of a launch vehicle.', 'correct': False,
             'id': 2},
            {'text': 'Is the minimum sampling frequency in A/D conversion', 'correct': False, 'id': 3}
        ],
        '',
        ['Structures'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 19
    builder.add_mc_question(
        'Which accurately describes hard real-time processing?',
        [
            {
                'text': 'requires precise timing of commands to achieve correct results – missing a time boundary has severe consequences',
                'correct': True, 'id': 0},
            {
                'text': 'requires that the tasks be performed in a timely manner –missing a time boundary results in degraded but continuous performance',
                'correct': False, 'id': 1},
            {
                'text': 'requires that tasks be completed within a certain specified time which can be large (e.g., within a day)',
                'correct': False, 'id': 2},
            {
                'text': 'requires processing the mission data as it is received, but it has no implications for computer throughput or input/output speed.',
                'correct': False, 'id': 3}
        ],
        '',
        ['Avionics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 20
    builder.add_mc_question(
        'How much radiation hardening is expected of a computer that will go in a LEO vs a GEO satellite?',
        [
            {'text': 'At least 10 krad in GEO, 100krad in LEO', 'correct': False, 'id': 0},
            {'text': 'At least 10 krad in LEO, 100krad in GEO', 'correct': True, 'id': 1},
            {'text': 'At least 1 krad in LEO, several Mrad for GEO', 'correct': False, 'id': 2},
            {'text': 'At least 1 krad in GEO, several Mrad for LEO', 'correct': False, 'id': 3}
        ],
        '',
        ['Avionics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 21
    builder.add_mc_question(
        'Which of the actions below is less likely in general to increase the reliability of the avionics system?',
        [
            {'text': 'Centralize all functions in a single larger computer', 'correct': True, 'id': 0},
            {'text': 'Use dedicated computers for certain functions', 'correct': False, 'id': 1},
            {'text': 'Use redundant computers', 'correct': False, 'id': 2},
            {'text': 'Use radiation-hardened computers', 'correct': False, 'id': 3}
        ],
        '',
        ['Avionics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_exam_finish_slide()

    return builder.get_module()

    


















    # builder.add_mc_question(
    #     'Which of the following are components of the electrical power system',
    #     [
    #         {'text': 'Power generation', 'correct': False, 'id': 0},
    #         {'text': 'Energy storage', 'correct': False, 'id': 1},
    #         {'text': 'Power regulation, and control power distribution', 'correct': False, 'id': 2},
    #         {'text': 'All of the above', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'You are responsible for deciding which power generation method to use on a satellite. Which of the following is the best power source if you want the satellite to record science data on a distant star?',
    #     [
    #         {'text': 'Solar', 'correct': False, 'id': 0},
    #         {'text': 'Hydroelectric', 'correct': False, 'id': 1},
    #         {'text': 'Flywheels', 'correct': False, 'id': 2},
    #         {'text': 'Nuclear', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What is the cheapest material for solar cells?',
    #     [
    #         {'text': 'Silicon', 'correct': True, 'id': 0},
    #         {'text': 'Gallium Arsenide', 'correct': False, 'id': 1},
    #         {'text': 'Semiconductors', 'correct': False, 'id': 2},
    #         {'text': 'Aluminum', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What units are used to measure the output and input power density?',
    #     [
    #         {'text': '$\\frac{1}{s^2}$', 'correct': False, 'id': 0},
    #         {'text': '$\\frac{W}{\\pi^2}$', 'correct': True, 'id': 1},
    #         {'text': '$\\frac{1}{\\pi \\pi^2}$', 'correct': False, 'id': 2},
    #         {'text': '$\\frac{S}{k g^2}$', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following is not a valid comparison between Silicon and triple junction solar arrays?',
    #     [
    #         {'text': 'Silicon\'s performance degrades quicker than multi-junction', 'correct': False, 'id': 0},
    #         {'text': 'Multi-junction arrays are much more expensive than Silicon', 'correct': False, 'id': 1},
    #         {'text': 'Multi-junction arrays have better solar cell efficiency than silicon', 'correct': False, 'id': 2},
    #         {'text': 'Silicon is a state of the art technology, while Multi-junction has significant heritage',
    #          'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What is the attitude of a satellite?',
    #     [
    #         {'text': 'The orientation in space along some reference frame', 'correct': True, 'id': 0},
    #         {'text': 'The distance a satellite is from the earth', 'correct': False, 'id': 1},
    #         {'text': 'The angle the satellite makes with the sun', 'correct': False, 'id': 2},
    #         {'text': 'The accuracy with which the spacecraft can determine or control its attitude', 'correct': False,
    #          'id': 3}
    #     ],
    #     '',
    #     ['ADCS'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'Which is not a downside of a satellite with low agility?',
    #     [
    #         {'text': 'Difficulty in maintaining communication links', 'correct': False, 'id': 0},
    #         {'text': 'Lower cost', 'correct': True, 'id': 1},
    #         {'text': 'Increased Risk of collision', 'correct': False, 'id': 2},
    #         {'text': 'Limited observation capability', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['ADCS'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What are some causes of disturbance torques?',
    #     [
    #         {'text': 'Atmospheric Drag', 'correct': False, 'id': 0},
    #         {'text': 'Magnetic Field', 'correct': False, 'id': 1},
    #         {'text': 'Solar Radiation', 'correct': False, 'id': 2},
    #         {'text': 'All of the above', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['ADCS'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What is the benefit of continuously spinning a satellite?',
    #     [
    #         {'text': 'High Accuracy measurements', 'correct': False, 'id': 0},
    #         {'text': 'Increased agility', 'correct': False, 'id': 1},
    #         {'text': 'Decrease effects of disturbance torques', 'correct': True, 'id': 2},
    #         {'text': 'Produce extra energy through mechanical motion', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['ADCS'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'You are an engineer creating a spin-stabilized satellite that requires 0.05-degree accuracy, what attitude control method is most viable?',
    #     [
    #         {'text': '3-axis stabilization', 'correct': True, 'id': 0},
    #         {'text': 'Momentum wheels', 'correct': False, 'id': 1},
    #         {'text': 'Pure-spin stabilization', 'correct': False, 'id': 2},
    #         {'text': 'Passive magnetic', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['ADCS'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What information is typically downlinked from a satellite?',
    #     [
    #         {'text': 'Mission Commands', 'correct': False, 'id': 0},
    #         {'text': 'Navigation information', 'correct': False, 'id': 1},
    #         {'text': 'Science Data', 'correct': True, 'id': 2},
    #         {'text': 'Dietary suggestions for astronauts', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'How is data transmitted from a satellite to the ground station through modulations?',
    #     [
    #         {
    #             'text': 'By changing some property of a high-frequency carrier signal in a way that encodes the information in the message',
    #             'correct': True, 'id': 0},
    #         {'text': 'By reflecting low frequency signals off the ionosphere', 'correct': False, 'id': 1},
    #         {'text': 'Through a digital connection system similar to the internet', 'correct': False, 'id': 2},
    #         {'text': 'Instantaneously through high-frequency signals', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What is Phase Shift Keying?',
    #     [
    #         {'text': 'A modulation technique that uses an encrypted language system to hide communications',
    #          'correct': False, 'id': 0},
    #         {'text': 'A modulation system that uses binary data representation to encode data', 'correct': True,
    #          'id': 1},
    #         {'text': 'A propulsion system using an electromagnetic power source', 'correct': False, 'id': 2},
    #         {'text': 'A strategy of determining the most efficient way to switch orbits', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following most directly causes Bit Error Rate to increase?',
    #     [
    #         {'text': 'The signal to noise ratio', 'correct': False, 'id': 0},
    #         {'text': 'The channel capacity', 'correct': False, 'id': 1},
    #         {'text': 'The modulation chosen', 'correct': False, 'id': 2},
    #         {'text': 'All of the above', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What equation links together the requirements with the main design parameters of both the satellite and the ground segment?',
    #     [
    #         {'text': 'Shannon Limit', 'correct': False, 'id': 0},
    #         {'text': 'RF Link Budget', 'correct': True, 'id': 1},
    #         {'text': '$\\Delta V$ Budget', 'correct': False, 'id': 2},
    #         {'text': 'System Noise Temperature', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # builder.add_quiz_end_slide()
    #
    # builder.add_mc_question(
    #     'Which of the following does not go into determining BOL power density?',
    #     [
    #         {'text': 'Required power during eclipse periods ( $P$ )', 'correct': True, 'id': 0},
    #         {'text': 'Distance to the sun (AU)', 'correct': False, 'id': 1},
    #         {'text': 'Solar cell efficiency $(\\eta)$', 'correct': False, 'id': 2},
    #         {'text': 'Inherent degradation $(I_d)$', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the purpose of secondary batteries?',
    #     [
    #         {'text': 'To power the launch vehicle', 'correct': False, 'id': 0},
    #         {'text': 'For energy storage', 'correct': True, 'id': 1},
    #         {'text': 'To power communication systems', 'correct': False, 'id': 2},
    #         {'text': 'To power low-power usage instruments', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the Depth of Discharge of a battery?',
    #     [
    #         {'text': 'The maximum capacity of charge after decay over time', 'correct': False, 'id': 0},
    #         {'text': 'The power required by the satellite at a given point in time', 'correct': False, 'id': 1},
    #         {'text': 'The amount of charge-discharge cycles a battery can withstand', 'correct': False, 'id': 2},
    #         {'text': 'The percentage of capacity used after a discharge', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Fault protection is one aspect of power distribution and management. What does fault protection consist of?',
    #     [
    #         {'text': 'Ensuring voltage and current levels are constant over time', 'correct': False, 'id': 0},
    #         {'text': 'Disposing of excess power generated by solar arrays', 'correct': False, 'id': 1},
    #         {'text': 'Wiring needed to bring power to equipment', 'correct': False, 'id': 2},
    #         {'text': 'Isolating power lines of components', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Power'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the relationship between emissivity and heat released by a system?',
    #     [
    #         {'text': 'Direct', 'correct': True, 'id': 0},
    #         {'text': 'Inverse', 'correct': False, 'id': 1},
    #         {'text': 'Negative Inverse', 'correct': False, 'id': 2},
    #         {'text': 'Negative Direct', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Thermal'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Why is slewing necessary in a satellite?',
    #     [
    #         {'text': 'To enhance the accuracy of the thrusters', 'correct': False, 'id': 0},
    #         {'text': 'To focus on a specific target', 'correct': True, 'id': 1},
    #         {'text': 'To switch orbits', 'correct': False, 'id': 2},
    #         {'text': 'To apply torque on the spacecraft', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['ADCS'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following is an example of a force actuator?',
    #     [
    #         {'text': 'Momentum Wheel', 'correct': False, 'id': 0},
    #         {'text': 'Reaction Wheel', 'correct': False, 'id': 1},
    #         {'text': 'Magnetorquers', 'correct': False, 'id': 2},
    #         {'text': 'Thruster', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['ADCS'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the significance of a delta $\mathrm{V}$ budget for a mission?',
    #     [
    #         {'text': 'It is the main requirement for determining propulsion system requirements', 'correct': True,
    #          'id': 0},
    #         {'text': 'It determines what communication system the satellite uses', 'correct': False, 'id': 1},
    #         {'text': 'delta $\mathrm{V}$ is not an important aspect of satellite design', 'correct': False, 'id': 2},
    #         {'text': 'It determines the power requirements', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Propulsion'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following most accurately defines Specific impulse?',
    #     [
    #         {'text': 'The smallest amount of delta $\mathrm{V}$ the system can provide (a measure of controllability)',
    #          'correct': False, 'id': 0},
    #         {'text': 'a measure of agility, which dictates how quickly a maneuver can be performed.', 'correct': False,
    #          'id': 1},
    #         {
    #             'text': 'A measure of fuel efficiency of the propulsion system, namely the thrust it can provide for a given propellant burn rate $m^*$',
    #             'correct': True, 'id': 2},
    #         {'text': 'For a given delta $V$, the amount of propellant needed', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Propulsion'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is a positive of using a chemical propulsion system?',
    #     [
    #         {'text': 'It provides higher thrust than electrical propulsion', 'correct': True, 'id': 0},
    #         {'text': 'It has a lower Delta $\mathrm{V}$ requirement', 'correct': False, 'id': 1},
    #         {'text': 'It provides less thrust than electric propulsion', 'correct': False, 'id': 2},
    #         {'text': 'It is more efficient than electric propulsion', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Propulsion'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following factors is higher frequency better for than lower frequency communications?',
    #     [
    #         {'text': 'Bandwidth', 'correct': True, 'id': 0},
    #         {'text': 'Ran attenuation', 'correct': False, 'id': 1},
    #         {'text': 'Free space loss', 'correct': False, 'id': 2},
    #         {'text': 'Cost', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following are requirements for determining satellite structure design?',
    #     [
    #         {'text': 'Manufacturability', 'correct': False, 'id': 0},
    #         {'text': 'Shielding from space environment', 'correct': False, 'id': 1},
    #         {'text': 'Withstand static and dynamic loads', 'correct': False, 'id': 2},
    #         {'text': 'All of the above', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the deflection of a beam in reference to buckling?',
    #     [
    #         {'text': 'The bending moment', 'correct': False, 'id': 0},
    #         {'text': 'The moment of inertia', 'correct': False, 'id': 1},
    #         {'text': 'The vertical displacement', 'correct': True, 'id': 2},
    #         {'text': 'The frequency a beam emits', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following is not a function of the avionics subsystem?',
    #     [
    #         {'text': 'Executing Commands', 'correct': False, 'id': 0},
    #         {'text': 'Storing Data', 'correct': False, 'id': 1},
    #         {'text': 'Running Flight Software', 'correct': False, 'id': 2},
    #         {'text': 'Switching the Satellite\'s Orbit', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'How is throughput measured in an avionics system?',
    #     [
    #         {'text': '$\\mathrm{b} / \\mathrm{s}$', 'correct': True, 'id': 0},
    #         {'text': '$\\mathrm{kg}^* \\mathrm{~m} 2 / \\mathrm{s}^{\\wedge} 2$', 'correct': False, 'id': 1},
    #         {'text': 'Joules', 'correct': False, 'id': 2},
    #         {'text': '$\\mathrm{Hz}$', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Avionics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # builder.add_exam_finish_slide()
    # return builder.get_module()









