from academy_assistant.database.client.modules.AbstractBuilder import AbstractBuilder
slide_text = ['']
import os
# slide_text_dir = os.path.join('/Users/mahima/Documents/daphne-academy/academy-brain/academy_assistant/database/client/modules/slide_text', 'smo')
base_dir = os.path.dirname(os.path.abspath(__file__))
slide_text_dir = os.path.join(base_dir, 'slide_text', 'smo')
# Iterate over all txt files in slide_text_dir
for file in os.listdir(slide_text_dir):
    if file.endswith('.txt'):
        with open(os.path.join(slide_text_dir, file), 'r') as f:
            slide_text.append(f.read())





def get_module():
    builder = AbstractBuilder('mdi-satellite', ['Space Logistics'], 'Intro to Space Commodities', None)

    # From slide 1 to slide 30
    builder.add_slide('ISC_SMO_1', slide_text[1], "https://academy2.selva-research.com/images/smo/Slide1.png")
    builder.add_slide('ISC_SMO_2', slide_text[2], "https://academy2.selva-research.com/images/smo/Slide2.png")
    builder.add_slide('ISC_SMO_3', slide_text[3], "https://academy2.selva-research.com/images/smo/Slide3.png")
    builder.add_slide('ISC_SMO_4', slide_text[4], "https://academy2.selva-research.com/images/smo/Slide4.png")
    builder.add_slide('ISC_SMO_5', slide_text[5], "https://academy2.selva-research.com/images/smo/Slide5.png")
    builder.add_slide('ISC_SMO_6', slide_text[6], "https://academy2.selva-research.com/images/smo/Slide6.png")
    builder.add_slide('ISC_SMO_7', slide_text[7], "https://academy2.selva-research.com/images/smo/Slide7.png")
    builder.add_slide('ISC_SMO_8', slide_text[8], "https://academy2.selva-research.com/images/smo/Slide8.png")
    builder.add_slide('ISC_SMO_9', slide_text[9], "https://academy2.selva-research.com/images/smo/Slide9.png")
    builder.add_slide('ISC_SMO_10', slide_text[10], "https://academy2.selva-research.com/images/smo/Slide10.png")
    builder.add_slide('ISC_SMO_11', slide_text[11], "https://academy2.selva-research.com/images/smo/Slide11.png")
    builder.add_slide('ISC_SMO_12', slide_text[12], "https://academy2.selva-research.com/images/smo/Slide12.png")
    builder.add_slide('ISC_SMO_13', slide_text[13], "https://academy2.selva-research.com/images/smo/Slide13.png")
    builder.add_slide('ISC_SMO_14', slide_text[14], "https://academy2.selva-research.com/images/smo/Slide14.png")
    builder.add_slide('ISC_SMO_15', slide_text[15], "https://academy2.selva-research.com/images/smo/Slide15.png")
    builder.add_slide('ISC_SMO_16', slide_text[16], "https://academy2.selva-research.com/images/smo/Slide16.png")
    builder.add_slide('ISC_SMO_17', slide_text[17], "https://academy2.selva-research.com/images/smo/Slide17.png")
    builder.add_slide('ISC_SMO_18', slide_text[18], "https://academy2.selva-research.com/images/smo/Slide18.png")
    builder.add_slide('ISC_SMO_19', slide_text[19], "https://academy2.selva-research.com/images/smo/Slide19.png")
    builder.add_slide('ISC_SMO_20', slide_text[20], "https://academy2.selva-research.com/images/smo/Slide20.png")
    builder.add_slide('ISC_SMO_21', slide_text[21], "https://academy2.selva-research.com/images/smo/Slide21.png")
    builder.add_slide('ISC_SMO_22', slide_text[22], "https://academy2.selva-research.com/images/smo/Slide22.png")
    builder.add_slide('ISC_SMO_23', slide_text[23], "https://academy2.selva-research.com/images/smo/Slide23.png")
    builder.add_slide('ISC_SMO_24', slide_text[24], "https://academy2.selva-research.com/images/smo/Slide24.png")
    builder.add_slide('ISC_SMO_25', slide_text[25], "https://academy2.selva-research.com/images/smo/Slide25.png")
    builder.add_slide('ISC_SMO_26', slide_text[26], "https://academy2.selva-research.com/images/smo/Slide26.png")
    builder.add_slide('ISC_SMO_27', slide_text[27], "https://academy2.selva-research.com/images/smo/Slide27.png")
    builder.add_slide('ISC_SMO_28', slide_text[28], "https://academy2.selva-research.com/images/smo/Slide28.png")
    builder.add_slide('ISC_SMO_29', slide_text[29], "https://academy2.selva-research.com/images/smo/Slide29.png")
    builder.add_slide('ISC_SMO_30', slide_text[30], "https://academy2.selva-research.com/images/smo/Slide30.png")

    builder.add_quiz_start_slide()

    # Question 1
    builder.add_mc_question(
        'Why is the cost of access to space so high?',
        [
            {'text': 'Rockets are complex', 'correct': False, 'id': 0},
            {'text': 'Rockets are inefficient', 'correct': False, 'id': 1},
            {'text': 'A lot of kinetic energy is required', 'correct': False, 'id': 2},
            {'text': 'b) and c)', 'correct': True, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 2
    builder.add_mc_question(
        'What are some example applications of space missions?',
        [
            {'text': 'Weather forecasting', 'correct': False, 'id': 0},
            {'text': 'Tourism', 'correct': False, 'id': 1},
            {'text': 'Intelligence, surveillance and reconnaissance', 'correct': False, 'id': 2},
            {'text': 'All of the above', 'correct': True, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 3
    builder.add_mc_question(
        'What factors contribute to the high cost of space missions?',
        [
            {'text': 'Efficient rockets, large markets, low reliability', 'correct': False, 'id': 0},
            {'text': 'Harsh space environment, small markets, labor-intensive', 'correct': True, 'id': 1},
            {'text': 'Low cost parts, frequent missions, complicated schedules', 'correct': False, 'id': 2},
            {'text': 'Abundant resources, high labor costs, complex operations', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 4
    builder.add_mc_question(
        'What is the typical range of costs for government Earth observation missions?',
        [
            {'text': '$10M - $200M', 'correct': False, 'id': 0},
            {'text': '$200M - $2B', 'correct': True, 'id': 1},
            {'text': '$2B - $5B', 'correct': False, 'id': 2},
            {'text': '$5B - $10B', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    # Question 5
    builder.add_mc_question(
        'Why does the mass of a spacecraft significantly impact mission cost?',
        [
            {'text': 'Higher mass requires more fuel to launch into space', 'correct': True, 'id': 0},
            {'text': 'Higher mass reduces reliability', 'correct': False, 'id': 1},
            {'text': 'Higher mass simplifies the design', 'correct': False, 'id': 2},
            {'text': 'Higher mass lowers the launch cost', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )
    
    builder.add_quiz_end_slide()


    # Question 6
    builder.add_mc_question(
        'Which option best explains the concept of "Space Spiral" and its effect on costs.',
        [
            {
                'text': 'Lots of missions lead to economies of scale, which leads to lower costs and thus even more missions',
                'correct': False, 'id': 0},
            {'text': 'Repeated failures of space missions lead to higher and higher costs', 'correct': False, 'id': 1},
            {
                'text': 'High costs lead to few space missions which leads to high reliability requirements, which leads to higher costs, fewer missions, higher reliability requirements, etc.',
                'correct': True, 'id': 2},
            {'text': 'Decreased costs due to mass production have led to an explosion in the number of space missions',
             'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 7
    builder.add_mc_question(
        'What is the average cost per kilogram to launch a satellite into space?',
        [
            {'text': '$500 - $1k', 'correct': False, 'id': 0},
            {'text': '$1k - $5k', 'correct': False, 'id': 1},
            {'text': '$5k - $20k', 'correct': True, 'id': 2},
            {'text': '$20k - $50k', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 8
    builder.add_mc_question(
        'What has been a primary factor behind the recent reduction in cost of access to space?',
        [
            {'text': 'Lean manufacturing and agile development processes', 'correct': False, 'id': 0},
            {'text': 'Cheaper materials and more efficient rocket engines', 'correct': False, 'id': 1},
            {'text': 'Reusable rockets', 'correct': True, 'id': 2},
            {'text': 'Smaller rockets, which are naturally more affordable on a per kg basis', 'correct': False,
             'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 9
    builder.add_mc_question(
        'What is the purpose of a spacecraft bus in a space mission?',
        [
            {'text': 'To transport astronauts or cargo in space', 'correct': False, 'id': 0},
            {'text': 'To provide power, communications, and other support to the payload', 'correct': True, 'id': 1},
            {'text': 'To launch the spacecraft', 'correct': False, 'id': 2},
            {'text': 'To control the mission from Earth', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 10
    builder.add_mc_question(
        'What role does the ground segment play in a space mission?',
        [
            {'text': 'Launching the spacecraft', 'correct': False, 'id': 0},
            {'text': 'Manufacturing the spacecraft components', 'correct': False, 'id': 1},
            {'text': 'Operating the spacecraft', 'correct': True, 'id': 2},
            {'text': 'Providing funding for the mission', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 11
    builder.add_mc_question(
        'Orbital velocity is…?',
        [
            {'text': 'The velocity that exactly balances lift and drag', 'correct': False, 'id': 0},
            {'text': 'The velocity that exactly balances centrifugal and gravitational forces at a given point',
             'correct': True, 'id': 1},
            {'text': 'Any non-zero velocity at a point above the atmosphere', 'correct': False, 'id': 2},
            {'text': 'The velocity needed to escape the Earth’s gravitational well', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 12
    builder.add_mc_question(
        'What are the elements that make up a space mission architecture?',
        [
            {'text': 'Launch segment, ground segment, space segment', 'correct': True, 'id': 0},
            {'text': 'Research, development, operations', 'correct': False, 'id': 1},
            {'text': 'Bus, payload, launch vehicle', 'correct': False, 'id': 2},
            {'text': 'Imaging concept, data delivery, command and control', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 13
    builder.add_mc_question(
        'What is the most common independent variable in space missions’ CERs?',
        [
            {'text': 'Mass', 'correct': True, 'id': 0},
            {'text': 'Power', 'correct': False, 'id': 1},
            {'text': 'Orbit altitude', 'correct': False, 'id': 2},
            {'text': 'Data rate', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 14
    builder.add_mc_question(
        'Which of the factors below is less likely to drive cost for an Earth observation mission?',
        [
            {'text': 'Throughput of the onboard computer', 'correct': True, 'id': 0},
            {'text': 'Aperture size for the imaging system', 'correct': False, 'id': 1},
            {'text': 'Amount of flight heritage in the payload and bus', 'correct': False, 'id': 2},
            {'text': 'Spacecraft mass', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 15
    builder.add_mc_question(
        'How does the choice of payload and orbit influence the cost of the mission?',
        [
            {'text': 'They have a relatively small impact on cost', 'correct': False, 'id': 0},
            {'text': 'They mostly influence launch segment costs', 'correct': False, 'id': 1},
            {'text': 'They drive the design of the spacecraft bus and thus overall mission cost', 'correct': True,
             'id': 2},
            {'text': 'Payload has a large impact but orbit has a small impact on mission cost', 'correct': False,
             'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 16
    builder.add_mc_question(
        'What are the typical phases in the operational timeline of an Earth observation mission?',
        [
            {'text': 'Launch, orbit insertion, commissioning, nominal operations, extended operations, end of life',
             'correct': True, 'id': 0},
            {'text': 'Design, manufacturing, integration, testing, launch, operations, end of life', 'correct': False,
             'id': 1},
            {'text': 'Research, development, launch, operations, decommissioning', 'correct': False, 'id': 2},
            {'text': 'Planning, launch, orbit stabilization, data collection, mission end', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 17
    builder.add_mc_question(
        'What is the main difference between centralized and distributed data processing in space missions?',
        [
            {'text': 'Centralized uses one computer, distributed uses multiple computers', 'correct': True, 'id': 0},
            {'text': 'Centralized occurs on the spacecraft, distributed occurs on Earth', 'correct': False, 'id': 1},
            {'text': 'Centralized is more costly, distributed is cost-effective', 'correct': False, 'id': 2},
            {'text': 'Centralized is slower, distributed is faster', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 18
    builder.add_mc_question(
        'Which option best explains the significance of tasking, scheduling, and control in the operation of a space mission?',
        [
            {'text': 'It ensures the mission stays within schedule and budget', 'correct': False, 'id': 0},
            {'text': 'It manages payload operations and spacecraft orientation', 'correct': True, 'id': 1},
            {'text': 'It attempts to optimize the spacecraft\'s mass', 'correct': False, 'id': 2},
            {'text': 'It plans the launch vehicle trajectory and controls it during the launch', 'correct': False,
             'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 19
    builder.add_mc_question(
        'What types of payloads are commonly used for Earth observation missions?',
        [
            {'text': 'Optical imagers, radars, spectrometers, lidars', 'correct': True, 'id': 0},
            {'text': 'Antennas and transceivers', 'correct': False, 'id': 1},
            {'text': 'Solar panels, batteries, thrusters, reaction wheels', 'correct': False, 'id': 2},
            {'text': 'Astronauts', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    # Question 20
    builder.add_mc_question(
        'What are some major cost drivers for the launch segment of a space mission?',
        [
            {'text': 'Spacecraft launch mass, weather conditions, reliability', 'correct': False, 'id': 0},
            {'text': 'Spacecraft launch mass, target orbit, reusability', 'correct': True, 'id': 1},
            {'text': 'Propellant type, mission trajectory', 'correct': False, 'id': 2},
            {'text': 'Launch site location, operator training, ground control setup', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Logistics'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )
    
    builder.add_exam_finish_slide()

    return builder.get_module()
    
    
    

    # builder.add_mc_question(
    #     "What constitutes most of a rocket's weight?",
    #     [
    #         {'text': 'Propellant', 'correct': True, 'id': 0},
    #         {'text': 'Communications Systems', 'correct': False, 'id': 1},
    #         {'text': 'Payload', 'correct': False, 'id': 2},
    #         {'text': 'Engine', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     "What is the main consequence of Newton's third law for rocket propulsion?",
    #     [
    #         {'text': 'It requires a constant thrust force to maintain orbital velocity', 'correct': False, 'id': 0},
    #         {'text': 'It limits the maximum payload capacity of a rocket', 'correct': False, 'id': 1},
    #         {'text': 'Heavier rockets require a proportionally larger amount of propellant', 'correct': True, 'id': 2},
    #         {'text': 'It creates a drag force that slows down the rocket launch', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     "In-situ resource utilization (ISRU) may refer to the use of resources available in space for:",
    #     [
    #         {'text': 'Obtaining rare elements to bring back to Earth', 'correct': False, 'id': 0},
    #         {'text': 'Measuring astronaut health', 'correct': False, 'id': 1},
    #         {'text': 'Conducting microgravity experiments on board spacecraft', 'correct': False, 'id': 2},
    #         {'text': 'Building and maintaining permanent human settlements on the Moon or Mars', 'correct': True,
    #          'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     "Define ConOps.",
    #     [
    #         {'text': 'Constraints Objectives and Operations', 'correct': False, 'id': 0},
    #         {'text': 'Concept of Operations', 'correct': True, 'id': 1},
    #         {'text': 'Confidence of Operations', 'correct': False, 'id': 2},
    #         {'text': 'Create Orbit and Optimization', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     "Which could be a part of the ConOps for a Satellite?",
    #     [
    #         {'text': 'Extensive size specifications', 'correct': False, 'id': 0},
    #         {'text': 'Calculations for the amount of fuel required', 'correct': False, 'id': 1},
    #         {'text': 'Expected orbit placement', 'correct': True, 'id': 2},
    #         {'text': 'Explanation of how individual instruments perform their measurements', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # # Question 1
    # builder.add_mc_question(
    #     'Which of the following applications does NOT utilize Earth observation satellites looking "down"?',
    #     [
    #         {'text': 'Weather Forecasting', 'correct': False, 'id': 0},
    #         {'text': 'Astrophysics', 'correct': True, 'id': 1},
    #         {'text': 'Surveillance', 'correct': False, 'id': 2},
    #         {'text': 'Communication/Navigation', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # # Question 2
    # builder.add_mc_question(
    #     'Which of the following are within the Space Segment of a Space Mission? Select all that apply: i) Spacecraft Bus, ii) Payload, iii) Launch Vehicle, iv) Mission Control',
    #     [
    #         {'text': 'Only i', 'correct': False, 'id': 0},
    #         {'text': 'i and ii', 'correct': True, 'id': 1},
    #         {'text': 'Only ii', 'correct': False, 'id': 2},
    #         {'text': 'iii and iv', 'correct': False, 'id': 3},
    #         {'text': 'ii and iii', 'correct': False, 'id': 4}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # # Question 3
    # builder.add_mc_question(
    #     'The ground segment is responsible for ALL of the following EXCEPT:',
    #     [
    #         {'text': 'Tracking spacecraft position', 'correct': False, 'id': 0},
    #         {'text': 'Processing and storing mission data', 'correct': False, 'id': 1},
    #         {'text': 'Attitude Control', 'correct': True, 'id': 2},
    #         {'text': 'Sending commands to the spacecraft', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # # Question 4
    # builder.add_mc_question(
    #     'What part of the Mission Architecture stores propellant?',
    #     [
    #         {'text': 'ConOps', 'correct': False, 'id': 0},
    #         {'text': 'Payload', 'correct': False, 'id': 1},
    #         {'text': 'Ground Segment', 'correct': False, 'id': 2},
    #         {'text': 'Launch Segment', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # # Question 5
    # builder.add_mc_question(
    #     'What type of spacecraft application would a satellite for TV services be?',
    #     [
    #         {'text': 'Exploration', 'correct': False, 'id': 0},
    #         {'text': 'Resource Utilization', 'correct': False, 'id': 1},
    #         {'text': 'Communications and Navigation', 'correct': True, 'id': 2},
    #         {'text': 'Education', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_quiz_end_slide()
    #
    # builder.add_mc_question(
    #     'What type of Satellite provides PNT services?',
    #     [
    #         {'text': 'Space Observation', 'correct': False, 'id': 0},
    #         {'text': 'Communication', 'correct': False, 'id': 1},
    #         {'text': 'Navigation', 'correct': True, 'id': 2},
    #         {'text': 'Earth Observation', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.75,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following does NOT occur during detumbling?',
    #     [
    #         {'text': 'Deploy antennas', 'correct': False, 'id': 0},
    #         {'text': 'Payload testing', 'correct': True, 'id': 1},
    #         {'text': 'Perform health tests', 'correct': False, 'id': 2},
    #         {'text': 'Transfer to operational orbit', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.75,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What type of satellite would perform on-orbit servicing?',
    #     [
    #         {'text': 'Space Observation', 'correct': True, 'id': 0},
    #         {'text': 'Communications', 'correct': False, 'id': 1},
    #         {'text': 'Earth Observation', 'correct': False, 'id': 2},
    #         {'text': 'a & b', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.75,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'How is orbital velocity defined?',
    #     [
    #         {'text': 'The velocity where centrifugal force is equal to gravitational force', 'correct': True, 'id': 0},
    #         {'text': 'The velocity required to exit Earth\'s atmosphere', 'correct': False, 'id': 1},
    #         {'text': 'The maximum velocity of the rocket', 'correct': False, 'id': 2},
    #         {'text': 'The velocity once the propellant has run out', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.75,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which statement about orbital velocity is not accurate?',
    #     [
    #         {'text': 'It balances gravitational pull inwards with centrifugal force outwards', 'correct': False,
    #          'id': 0},
    #         {'text': 'It is approximately 7.5 km/s for low Earth orbit', 'correct': False, 'id': 1},
    #         {'text': 'Additional velocity is required to overcome energy losses during launch', 'correct': False,
    #          'id': 2},
    #         {'text': 'It allows the satellite to maintain a constant altitude above Earth', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Space Logistics'],
    #     difficulty=0.75,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following is an ACTIVE illumination system?',
    #     [
    #         {'text': 'Thermal Control Surfaces', 'correct': False, 'id': 0},
    #         {'text': 'Communication Antennas', 'correct': False, 'id': 1},
    #         {'text': 'Solar Panels', 'correct': False, 'id': 2},
    #         {'text': 'Radar', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What considerations are necessary when determining data delivery systems?',
    #     [
    #         {'text': 'Space vs Ground processing', 'correct': False, 'id': 0},
    #         {'text': 'Centralized vs Distributed Processing', 'correct': False, 'id': 1},
    #         {'text': 'Level of autonomy', 'correct': False, 'id': 2},
    #         {'text': 'All of the above', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What task is usually performed from the ground?',
    #     [
    #         {'text': 'Payload scheduling', 'correct': True, 'id': 0},
    #         {'text': 'Attitude control', 'correct': False, 'id': 1},
    #         {'text': 'Data acquisition', 'correct': False, 'id': 2},
    #         {'text': 'Low-level Signal Processing', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What are CubeSat satellites most commonly used for?',
    #     [
    #         {'text': 'Military', 'correct': False, 'id': 0},
    #         {'text': 'Navigation', 'correct': False, 'id': 1},
    #         {'text': 'Education', 'correct': True, 'id': 2},
    #         {'text': 'Tourism', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the difference between centralized and distributed processing?',
    #     [
    #         {
    #             'text': 'Centralized can only be used in communication satellites, distributed can be used among any satellite',
    #             'correct': False, 'id': 0},
    #         {'text': 'Centralized is based on Earth, distributed is in space', 'correct': False, 'id': 1},
    #         {'text': 'Centralized is completely autonomous, distributed is completely manual', 'correct': False,
    #          'id': 2},
    #         {'text': 'Centralized uses one computer, distributed uses multiple', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['System Architecture'],
    #     difficulty=0.5,  # Adjust difficulty as needed
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
    # builder.add_exam_finish_slide()
    # return builder.get_module()












