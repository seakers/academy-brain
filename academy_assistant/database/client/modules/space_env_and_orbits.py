from academy_assistant.database.client.modules.AbstractBuilder import AbstractBuilder


def get_module():
    builder = AbstractBuilder('mdi-orbit', ['Intro To Space'], 'Intro to Space Commodities', None)

    builder.add_slide('JD2_1', slide_text[1])
    builder.add_slide('JD2_2', slide_text[2])
    builder.add_slide('JD2_3', slide_text[3])
    builder.add_slide('JD2_4', slide_text[4])
    builder.add_slide('JD2_5', slide_text[5])
    builder.add_slide('JD2_6', slide_text[6])
    builder.add_slide('JD2_7', slide_text[7])
    builder.add_slide('JD2_8', slide_text[8])
    builder.add_slide('JD2_9', slide_text[9])
    builder.add_slide('JD2_10', slide_text[10])
    builder.add_slide('JD2_11', slide_text[11])
    builder.add_slide('JD2_12', slide_text[12])
    builder.add_slide('JD2_13', slide_text[13])
    builder.add_slide('JD2_14', slide_text[14])
    builder.add_slide('JD2_15', slide_text[15])
    builder.add_slide('JD2_16', slide_text[16])
    builder.add_slide('JD2_17', slide_text[17])
    builder.add_slide('JD2_18', slide_text[18])
    builder.add_slide('JD2_19', slide_text[19])
    builder.add_slide('JD2_20', slide_text[20])
    builder.add_slide('JD2_21', slide_text[21])
    builder.add_slide('JD2_22', slide_text[22])
    builder.add_slide('JD2_23', slide_text[23])
    builder.add_slide('JD2_24', slide_text[24])
    builder.add_slide('JD2_25', slide_text[25])
    builder.add_slide('JD2_26', slide_text[26])
    builder.add_slide('JD2_27', slide_text[27])
    builder.add_slide('JD2_28', slide_text[28])
    builder.add_slide('JD2_29', slide_text[29])
    builder.add_slide('JD2_30', slide_text[30])
    builder.add_slide('JD2_31', slide_text[31])
    builder.add_slide('JD2_32', slide_text[32])

    builder.add_quiz_start_slide()

    builder.add_mc_question(
        'Which of the following constitutes a 2-body problem?',
        [
            {'text': '2 objects in freefall are repelled by each other’s gravitational field', 'correct': False,
             'id': 0},
            {'text': '2 objects are parallel to each other in free fall', 'correct': False, 'id': 1},
            {
                'text': '2 objects are in orbit with each other, and their motion is only affected by forces caused by the other object',
                'correct': True, 'id': 2},
            {'text': '2 objects in orbit with each other with a third object influencing their motion',
             'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )
    builder.add_mc_question(
        'A satellite\'s orbit is an ellipse with a semimajor axis (a) of 10,000 km and an eccentricity (e) of 0.2. How does this orbit compare to a circular orbit with the same semimajor axis?',
        [
            {'text': 'It is slightly elongated but has a similar overall size as the circular orbit', 'correct': True,
             'id': 0},
            {'text': 'It is smaller and lies entirely within the circular orbit.', 'correct': False, 'id': 1},
            {'text': 'It is larger and encloses the circular orbit.', 'correct': False, 'id': 2},
            {'text': 'The comparison cannot be determined without additional information', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )
    builder.add_mc_question(
        'What is the primary difference between a closed and an open orbit for a satellite around Earth?',
        [
            {'text': 'The satellite\'s speed is higher in a closed orbit', 'correct': False, 'id': 0},
            {'text': 'In a closed orbit the satellite revolves around the Earth, in an open orbit it does not',
             'correct': True, 'id': 1},
            {'text': 'The satellite experiences a wider range of temperatures in a closed orbit', 'correct': False,
             'id': 2},
            {'text': 'Closed orbits are within the Low Earth Orbit range', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )
    builder.add_mc_question(
        'What information is not required to calculate the position of a satellite within its orbit?',
        [
            {'text': 'Apogee', 'correct': False, 'id': 0},
            {'text': 'Perigee', 'correct': False, 'id': 1},
            {'text': 'Eccentricity', 'correct': False, 'id': 2},
            {'text': 'Velocity', 'correct': True, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )
    builder.add_mc_question(
        'When referring to a satellite\'s perigee and apogee, which statement is true?',
        [
            {'text': 'They represent the two farthest points from Earth in an elliptical orbit', 'correct': False,
             'id': 0},
            {'text': 'The perigee is always located on the major axis of the ellipse', 'correct': False, 'id': 1},
            {'text': 'The apogee and perigee always lie on the same line passing through the Earth\'s center',
             'correct': True, 'id': 2},
            {'text': 'The satellite\'s speed is highest at its perigee and lowest at its apogee', 'correct': True,
             'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )




    builder.add_quiz_end_slide()

    builder.add_mc_question(
        'Which of the following statements accurately describes the relationship between the inclination (i) and the right ascension of the ascending node (RAAN) (Ω) in defining the satellite\'s orbital plane?',
        [
            {'text': 'They both represent the angle between the orbital plane and the Earth\'s equatorial plane',
             'correct': False, 'id': 0},
            {
                'text': 'Both i and Ω contribute to defining the plane\'s orientation, but they are not directly related to each other',
                'correct': True, 'id': 1},
            {'text': 'Ω defines the "twist" of the plane, while i represents the "tilt" angle from the ascending node',
             'correct': False, 'id': 2},
            {'text': 'Only RAAN (Ω) is necessary to fully define the orientation of the orbital plane',
             'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following represents the value of r in the Satellite Velocity equation?',
        [
            {'text': 'The length of the semimajor axis', 'correct': False, 'id': 0},
            {'text': 'The distance from the center of the central body to the satellite', 'correct': True, 'id': 1},
            {'text': 'The distance between the satellite and the surface of the central body', 'correct': False,
             'id': 2},
            {'text': 'The distance between the center of the central body and its surface', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'The vis-viva equation demonstrates that the satellite\'s velocity in an elliptical orbit:',
        [
            {'text': 'Remains constant throughout its entire journey', 'correct': False, 'id': 0},
            {'text': 'Is directly proportional to its distance from Earth', 'correct': False, 'id': 1},
            {'text': 'Depends solely on the satellite\'s mass and the Earth\'s mass', 'correct': False, 'id': 2},
            {'text': 'Increases as it approaches Earth and decreases as it moves away', 'correct': True, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What is the period of a satellite in geosynchronous orbit?',
        [
            {'text': 'Not enough information is given', 'correct': False, 'id': 0},
            {'text': '365 days', 'correct': False, 'id': 1},
            {'text': '24 hours', 'correct': True, 'id': 2},
            {'text': '12 hours', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Which of the following would be a unique concern with sending a satellite to an orbit with a height of 36000km?',
        [
            {'text': 'This height is further than the outermost Earth orbit', 'correct': False, 'id': 0},
            {'text': 'The gravitational pull from other planets would affect the Satellite', 'correct': False, 'id': 1},
            {'text': 'High orbit traffic', 'correct': True, 'id': 2},
            {'text': 'There is little merit in sending a satellite to this height', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Why is a Sun Synchronous Orbit optimal for gathering certain weather and agricultural data?',
        [
            {'text': 'Consistent lighting conditions', 'correct': True, 'id': 0},
            {'text': 'Proximity to Earth', 'correct': False, 'id': 1},
            {'text': 'Cost efficient launching', 'correct': False, 'id': 2},
            {'text': 'Sun Synchronous Orbit is not optimal for gathering weather or agricultural data',
             'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What type of satellite would not be used often in the Molniya Orbit?',
        [
            {'text': 'Communication', 'correct': False, 'id': 0},
            {'text': 'Navigation', 'correct': False, 'id': 1},
            {'text': 'Military', 'correct': False, 'id': 2},
            {'text': 'Weather Observation', 'correct': True, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What orbit would be best for a global coverage weather satellite?',
        [
            {'text': 'GEO', 'correct': True, 'id': 0},
            {'text': 'Sun-Synchronous', 'correct': False, 'id': 1},
            {'text': 'Molniya', 'correct': False, 'id': 2},
            {'text': 'Low Earth Orbit', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'How is the orbital period calculated?',
        [
            {'text': 'Using Kepler’s Laws', 'correct': True, 'id': 0},
            {'text': 'Using Newton’s Laws', 'correct': False, 'id': 1},
            {'text': 'Using Planck’s Laws', 'correct': False, 'id': 2},
            {'text': 'Using Hubble’s Laws', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What distance is represented when theta=0 in the satellite distance equation?',
        [
            {'text': 'Apogee', 'correct': False, 'id': 0},
            {'text': 'Semimajor-axis', 'correct': False, 'id': 1},
            {'text': 'True Anomaly', 'correct': False, 'id': 2},
            {'text': 'Perigee', 'correct': True, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'At which point(s) does the orbital plane intersect the Earth\'s equatorial plane?',
        [
            {'text': 'Ascending and Descending Nodes', 'correct': True, 'id': 0},
            {'text': 'North and South Poles', 'correct': False, 'id': 1},
            {'text': 'Vernal Equinox', 'correct': False, 'id': 2},
            {'text': 'Argument of the Perigee', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'How is the orbital velocity (V) related to the orbital period (T)?',
        [
            {'text': 'Direct', 'correct': False, 'id': 0},
            {'text': 'Inverse', 'correct': True, 'id': 1},
            {'text': 'Quadratic', 'correct': False, 'id': 2},
            {'text': 'None of the above', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Despite being in "free fall," objects in orbit do not experience true weightlessness due to:',
        [
            {'text': 'The absence of air resistance', 'correct': False, 'id': 0},
            {'text': 'The orbital velocity: the spacecraft is moving at a high velocity', 'correct': False, 'id': 1},
            {'text': 'Residual gravitational force', 'correct': True, 'id': 2},
            {'text': 'Drag', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Why does atmospheric density have a significant impact on satellites in low Earth orbit (LEO)?',
        [
            {'text': 'It affects the amount of solar energy received by the satellite', 'correct': False, 'id': 0},
            {'text': 'It disrupts the communication signals between the satellite and the ground', 'correct': False,
             'id': 1},
            {'text': 'It creates drag that can lead to orbital decay and require corrections', 'correct': True,
             'id': 2},
            {'text': 'It increases the temperature of the satellite due to friction', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What role does Earth’s magnetic field have in environmental protection?',
        [
            {'text': 'The magnetic field deflects solar winds carrying particles from CMEs', 'correct': True, 'id': 0},
            {'text': 'The magnetic field absorbs all charged particles in solar winds', 'correct': False, 'id': 1},
            {'text': 'The magnetic field directs particles to the magnetic poles, leading them to Earth',
             'correct': False, 'id': 2},
            {'text': 'The magnetic field does not affect the solar particles', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What material is best to prevent outgassing?',
        [
            {'text': 'Aluminum', 'correct': True, 'id': 0},
            {'text': 'Zinc', 'correct': False, 'id': 1},
            {'text': 'Cadmium', 'correct': False, 'id': 2},
            {'text': 'Magnesium', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'If thrust is applied to an object in orbit in the direction of its orbital velocity, how is the orbit affected?',
        [
            {'text': 'The satellite will completely change orbits', 'correct': False, 'id': 0},
            {'text': 'The satellite will remain in the same plane but with a larger orbit', 'correct': True, 'id': 1},
            {'text': 'The satellite will slow down due to drag, causing the thrust to have no effect', 'correct': False,
             'id': 2},
            {'text': 'Satellites cannot change trajectory once placed in an orbit', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_tlx_survey_slide()
    builder.add_exam_finish_slide()

    return builder.get_module()




    #
    #
    #
    #
    #
    # builder.add_mc_question(
    #     'Which of these are NOT a potential consequence for astronauts living in a low gravity environment?',
    #     [
    #         {'text': 'Bone density loss', 'correct': False, 'id': 0},
    #         {'text': 'Decrease in height', 'correct': True, 'id': 1},
    #         {'text': 'Cardiovascular problems', 'correct': False, 'id': 2},
    #         {'text': 'Muscle loss', 'correct': False,
    #          'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    # builder.add_mc_question(
    #     'For a spacecraft in a circular orbit, what point is the orbital velocity the greatest?',
    #     [
    #         {'text': 'Periapsis', 'correct': False, 'id': 0},
    #         {'text': 'Ascending Node', 'correct': False, 'id': 1},
    #         {'text': 'Apoapsis', 'correct': False, 'id': 2},
    #         {'text': 'The velocity is constant throughout the orbit', 'correct': True,
    #          'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    # builder.add_mc_question(
    #     'The orbital plane of a satellite around Earth',
    #     [
    #         {'text': 'Stays fixed in space', 'correct': False, 'id': 0},
    #         {'text': 'Rotates slowly', 'correct': True, 'id': 1},
    #         {'text': 'Increases in eccentricity over time', 'correct': False, 'id': 2},
    #         {'text': 'Decreases in eccentricity over time', 'correct': False,
    #          'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    # builder.add_mc_question(
    #     'If the altitude of a circular orbit increases, the orbital velocity _______.',
    #     [
    #         {'text': 'Increases', 'correct': False, 'id': 0},
    #         {'text': 'Does not change', 'correct': False, 'id': 1},
    #         {'text': 'Decreases', 'correct': True, 'id': 2},
    #         {'text': 'None of the above', 'correct': False,
    #          'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    # builder.add_mc_question(
    #     'Why is the density of the atmosphere that a spacecraft encounters important?',
    #     [
    #         {'text': 'As density decreases, the buoyancy force affecting the spacecraft increases', 'correct': False, 'id': 0},
    #         {'text': 'Density decreases the efficiency of engines', 'correct': False, 'id': 1},
    #         {'text': 'We do not care about density', 'correct': False, 'id': 2},
    #         {'text': 'The drag force that impacts the satellite and produces orbital perturbations increases with density', 'correct': True,
    #          'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    #
    #
    # builder.add_quiz_end_slide()
    #
    # # # mc
    # # # mc
    # # # tf
    # # # mc
    # # # tf
    # # # mc
    # # # mc
    # # # mc
    # # # mc
    # # # tf
    # # # mc
    # #
    # builder.add_mc_question(
    #     'When the velocity of a spacecraft is increased by a factor of 4, by what factor will the drag force change if all other variables are kept constant?',
    #     [
    #         {'text': '1/4', 'correct': False, 'id': 0},
    #         {'text': '4', 'correct': False, 'id': 1},
    #         {'text': '8', 'correct': False, 'id': 2},
    #         {'text': '1/16', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_mc_question(
    #     'Outgassing is due to the environment in space being ______.',
    #     [
    #         {'text': 'a near vacuum', 'correct': True, 'id': 0},
    #         {'text': 'high in radiation', 'correct': False, 'id': 1},
    #         {'text': 'low gravity', 'correct': False, 'id': 2},
    #         {'text': 'much hotter than Earth temperatures', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_tf_question(
    #     'The minimum magnetic field intensity is found at the poles.',
    #     False,
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.25,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_mc_question(
    #     'What does “impulsive” describe about a maneuver?',
    #     [
    #         {'text': 'Maneuvers are made impulsively by the onboard computer that decreases computing time when hundreds of maneuvers need to be made', 'correct': False, 'id': 0},
    #         {'text': 'The burn time of the maneuver is assumed to be very short compared to the period of the orbit', 'correct': True, 'id': 1},
    #         {'text': 'The maneuvers are performed in many consecutive, smaller pulses throughout the orbit instead of a continuous burn until the desired conditions are reached', 'correct': False, 'id': 2},
    #         {'text': 'None of the above', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_tf_question(
    #     'The Van Allen Belts contain the safest environment for a satellite.',
    #     False,
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.25,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_mc_question(
    #     'Which of these is the least impactful source of radiation to a spacecraft?',
    #     [
    #         {'text': 'Solar flares', 'correct': False, 'id': 0},
    #         {'text': 'Galactic cosmic rays', 'correct': False, 'id': 1},
    #         {'text': 'Earth-generated infrared radiation', 'correct': True, 'id': 2},
    #         {'text': 'Van Allen Radiation Belt', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_mc_question(
    #     'Consider a spacecraft in an equatorial orbit (i.e. inclination 0 degrees) around Earth at a moment when the Sun, Earth and Spacecraft are aligned. Looking at the Earth-spacecraft-sun system from above, what is the order of the Earth, Sun, and Spacecraft when the spacecraft is at Perigee from left to right?',
    #     [
    #         {'text': 'Sun - Earth - Spacecraft', 'correct': False, 'id': 0},
    #         {'text': 'Earth - Sun - Spacecraft', 'correct': False, 'id': 1},
    #         {'text': 'Sun - Spacecraft - Earth', 'correct': False, 'id': 2},
    #         {'text': 'Too little information', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_mc_question(
    #     'Which of the following are not possible shapes for a spacecraft’s orbit?',
    #     [
    #         {'text': 'Dot (i.e., spacecraft hovering in space, not moving)', 'correct': True, 'id': 0},
    #         {'text': 'Circle', 'correct': False, 'id': 1},
    #         {'text': 'Parabola', 'correct': False, 'id': 2},
    #         {'text': 'Ellipse', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_mc_question(
    #     'Open orbits follow a path defined by a _______ or a ________ (conic sections).',
    #     [
    #         {'text': 'Circle, Parabola', 'correct': False, 'id': 0},
    #         {'text': 'Parabola, Hyperbola', 'correct': True, 'id': 1},
    #         {'text': 'Hyperbola, Ellipse', 'correct': False, 'id': 2},
    #         {'text': 'Circle, Ellipse', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_tf_question(
    #     'The Earth or larger body always sits at one of the foci of an orbit.',
    #     False,
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.25,
    #     discrimination=10,
    #     graded=True
    # )
    # builder.add_mc_question(
    #     'For a value of the true anomaly θ is 90°, which of the following describes the line that connects the center of mass of the system and the satellite in an elliptical orbit.',
    #     [
    #         {'text': 'Perpendicular to the semi major axis, passing through one of the foc', 'correct': True, 'id': 0},
    #         {'text': 'Perpendicular to the semi minor axis, passing though one of the foci', 'correct': False, 'id': 1},
    #         {'text': 'Parallel to the semi minor axis, passing through the center of the ellipse', 'correct': False, 'id': 2},
    #         {'text': 'Parallel to the semi major axis, passing through the center of the ellipse', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Intro To Space'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    #
    #
    #
    # builder.add_exam_finish_slide()
    # return builder.get_module()




slide_text = []
slide_text.append("""

""")
slide_text.append("""
Intro to Space Commodities
Module 2: Space Environment and Orbits
Dr. Daniel Selva (Texas A&M University)
Dr. Alejandro Salado (University of Arizona)
""")
slide_text.append("""
Intro to Module 2
- In this module, you will get introduced to space missions and the space mission design process.
- The module consists of 4 short lectures:
1. Space environment. What makes space a harsh environment? How does it affect humans and spacecraft?
2. Introduction to orbits. What is an orbit and why is it important?
3. Types of orbits. What types of orbits are there? How does orbit selection affect spacecraft design?
4. Orbital maneuvers. How do different types of maneuvers work in space? Implications on spacecraft design.
""")
slide_text.append("""
1. Space environment
""")
slide_text.append("""
"Microgravity"
- Objects are in "free fall", not absence of gravity!
- Gravity compensated by centrifugal force due to orbital speed
- Near absence of gravity $\left(\sim 10^{-6} \mathrm{~g}\right)$ means that:
- Objects don't fall
- Particles don't settle in a solution
- No convection (eliminates an important heat transfer mechanism!)
- This presents challenges, mostly for astronauts...
- Bone loss
- Muscle loss
- Cardiovascular problems
- Immune system
- ...but also opportunities
- Formation of large crystals
- The effects on traditional Earth satellites are relatively benign (e.g., lower structural stresses when in orbit)
""")
slide_text.append("""
Atmospheric drag - Orbit/attitude disturbance
-We care about atmospheric density mostly because it affects the drag force (D) experienced by the satellite, which may lead to orbital decay and disturbance torques
$$
D=\frac{1}{2} \rho V^2 C_D A
$$
- $\rho\left(\frac{k g}{m^3}\right)$ is the atmospheric density (varies exponentially but very small in orbit)
- $C_D$ is the unitless drag coefficient ( $\sim 2-4$ are typical values for a spacecraft)
- $V\left(\frac{m}{s}\right)$ is the orbital velocity
- $A(m)$ is the drag area
- Atmospheric drag is strong up to $\sim 500 \mathrm{~km}$, negligible after that
""")
slide_text.append("""
Atomic Oxygen - Erosion
- In the upper layers of the atmosphere the predominant constituent is atomic oxygen (O), formed by photodissociation of $\mathrm{O} 2$
$$
\mathrm{O}_2+\text { light } \rightarrow \mathrm{O}+\mathrm{O}
$$
- Highly reactive and energetic
- It erodes satellite surfaces (Teflon, epoxies, Mylar)
- Surfaces can be protected by coating them with something that is "immune" to $\mathrm{O}$ :
- Silicon dioxide
- Aluminum
""")
slide_text.append("""
Vacuum - Outgassing
- Outgassing is the release of gas that was trapped in some material
- adhesives, insulators, thermal coating, electrical shields
- Vacuum facilitates outgassing due to decreased sublimation and evaporation points.
- Outgassed material tends to condense onto cooler surfaces.
- Optical elements, radiators, solar cells
- Reaction with UV radiation results in dark stains that may affect performance of instruments or solar panels.
- Some materials outgas more than others in vacuum (e.g., $\mathrm{Cd}, \mathrm{Zn}$, $\mathrm{Mg}$, paints, etc.)
""")
slide_text.append("""
Earth's magnetic field
- The Earth has a magnetic field
- Protects us from solar radiation
- Generates forces that rotate spacecraft (can be leveraged using magnetic torquers)
- Magnetic field lines points from magnetic south to north
- Different from geographic equator and poles
- Max at the magnetic poles, $\min$ at the magnetic equator
- Protects us from radiation
""")
slide_text.append("""
Electromagnetic Radiation
- Electromagnetic radiation is carried by waves and massless particles (named photons) that travel at the speed of light
- Waves are periodic
- Wavelength is the distance between consecutive peaks
- Frequency is the inverse of the time interval between consecutive peaks
- Frequency $f(1 / \mathrm{sec})$ and wavelength $\lambda(m)$ are related by the speed of light $c$
$$
f=\frac{c}{\lambda}
$$
- The energy of a photon $E(J)$ is proportional to its frequency through the Planck constant $h$
$$
E=h f=\frac{h c}{\lambda}
$$
- Where $c=3 \cdot 10^8 \frac{\mathrm{m}}{\mathrm{s}}$ and $h=6.63$ $\cdot 10^{-34} \frac{\mathrm{J}}{\mathrm{s}}$
""")
slide_text.append("""
Example Question
- Which of the following statements are true?
1. Frequency is inversely proportional to wavelength
2. Frequency is directly proportional to wavelength
3. Energy is directly proportional to frequency
4. Energy is directly proportional to wavelength
- Clearly, 1 and 3 are true, 2 and 4 ar false.
""")
slide_text.append("""
Solar Radiation - Light, matter, and fields
- Explosions in the Sun's atmosphere produce both
- light (photons)
- matter (charged particles)
- This becomes radiation from the Sun
- Solar flares are huge bursts of photons in all wavelengths
- Coronal Mass Ejections (CME) are made of charged particles (ions and electrons) ejected at very high speeds
""")
slide_text.append("""
Van Allen Radiation Belts
- The Van Allen Belts are 2 regions of trapped fast charged particles (electrons and protons)
- Inner belt: $1,000-6,000 \mathrm{~km}$ altitude
- Outer belt: $13,000-60,000 \mathrm{~km}$
- Many satellites are in low orbits $(400-800 \mathrm{~km})$ below the inner belt, but many others are in higher orbits $(20000-36,000 \mathrm{~km})$ and thus are affected by the outer belt.
- The South Atlantic Anomaly is a region where the Earth's magnetic field is weaker and thus radiation is worse. Leads to more radiationrelated spacecraft failures.
""")
slide_text.append("""
2. Introduction to orbits
""")
slide_text.append("""
What are orbits?
- Orbits are the trajectories that spacecraft follow around the Earth due to gravitational forces
- Any two objects under each other's gravitational force will "orbit each other"
- This is called the 2-body problem
- The two objects orbit the center of mass of the system
- When one's mass is much larger than the other's (e.g., a satellite vs Earth, or the Earth vs the Sun) the motion of the large object is largely unaffected, and it all happens as if the small object rotates around the large object
""")
slide_text.append("""
Shape of orbits
- Satellite orbits are generally ellipses
- The center of mass of the system sits in one of the focus points
- An ellipse is defined by 2 parameters:
- The semimajor axis $a$ is half the length of the longer axis
Increasing a makes the orbit "bigger", further from Earth
- The eccentricity $e$ tells us how elongated the ellipse is
- When $e=0$, the ellipse becomes a perfect circle
- As e approaches 1 , it becomes more elongated
- Together, $a$ and e define the shape of the orbit
""")
slide_text.append("""
Conic sections, open vs closed orbits
- More generally, orbital trajectories can follow the shape of any conic section (circle, ellipse, parabola, or hyperbola)
- Circular and elliptical orbits $(0 \leq e<1)$ are "closed orbits" around the Earth
- A satellite with sufficient energy $(e \geq 1)$ will escape Earth and follow an interplanetary trajectory that never comes back (i.e., "open orbits")
- When $e=1$, it follows a parabolic trajectory
- When $e>1$ it follows a hyperbolic trajectory
""")
slide_text.append("""
Position of a satellite within its orbit
- The true anomaly $\theta$ is an angle that defines where within the orbit the satellite is at a given point in time
- There are two special points:
- the perigee is the point where it is closest to the Earth
- The apogee is the point where it is farthest from the Earth
- Given $a, e$ and $\theta$ we can compute the satellite position $r$, i.e., the distance between the satellite and Earth:
$$
r(\theta)=\frac{a\left(1-e^2\right)}{1+e \cos \theta}
$$
- For example, the distance to the perigee $\left(\theta=0^{\circ}\right)$ is $r_p=a(1-e)$
- The distance to the apogee and apogee $\left(\theta=180^{\circ}\right)$ is $r_a=a(1+c)$
""")
slide_text.append("""
Example Question
- For an orbit with a semi-major axis of $1000 \mathrm{~km}$ and an ecentricity of 0.5 , what is the distance between the satellite and the Earth when the true anomaly is $60^{\circ}$ ?
- The distance between the satellite and the Earth is
$$
r(\theta)=\frac{a\left(1-e^2\right)}{1+e \cos \theta}=\frac{10^6\left(1-0.5^2\right)}{1+0.5 \cos 60^0}=6 \cdot 10^5 \mathrm{~m}=600 \mathrm{~km}
$$
- The true anomaly is only $60^{\circ}$; therefore, the satellite is generally close to perigee. Therefore, the position or altitude above the Earth is much smaller than the semi-major axis of the orbit
""")
slide_text.append("""
Orientation of the orbit and orbital plane
- The orbit lies on a plane called the orbital plane that intersects the Earth's equatorial plane (i.e. at 0 degrees latitude) at two points called the nodes:
- Ascending node: where the satellite is going up (north)
- Descending node: where it is going down (south)
- The orientation of the orbit (the ellipse) within the orbital plane is defined by an angle called the argument of the perigee
- Angle from the ascending node to the perigee from the Earth center, $\omega$
- The orientation of the orbital plane with respect to the Earth is defined by two angles:
- The inclination $i$ is the "tilt" angle between the orbital plane and the equatorial plane
- The right ascension of the ascending node (a.k.a. the RAAN), $\Omega$ is the "twist" angle of the orbital plane, from the Vernal equinox (a fixed direction in space) to the ascending node
""")
slide_text.append("""
Orbital Period
- Together the 6 orbital $a, e, i, \omega, \Omega, \theta$ parameters fully define the trajectory of the satellite
- From these 6 parameters we can calculate anything: the satellite position, velocity, etc.
- For example, from Kepler's laws, we can calculate the orbital period, i.e., the time it takes the satellite to go around its orbit once:
$$
T=2 \pi \sqrt{\frac{a^3}{G M}}
$$
- Where is the gravitational constant $G=6.67 \cdot 10^{-11} \frac{\mathrm{Nm}^2}{\mathrm{~kg}^2}$ and $M$ $=5.97 \cdot 10^{24} \mathrm{~kg}$ is the mass of the Earth
- Note that period only depends on the semimajor axis!
""")
slide_text.append("""
Orbital velocity
- Similarly, using the vis-viva equation (conservation of energy), we can compute the velocity of the satellite:
$$
V=\sqrt{G M\left(\frac{2}{r}-\frac{1}{a}\right)}
$$
- For a general elliptical orbit, we see that as predicted by Kepler's laws, the satellite will move faster the closer it gets to Earth, and will slow down as it gets farther from Earth
- For a circular orbit, $r=a=R_E+h$ where $R_E=6370 \mathrm{~km}$ is the radius of the Earth and $h$ is the orbit altitude. In this case, the velocity is constant:
$$
V=\sqrt{\frac{G M}{R_E+h}}
$$
""")
slide_text.append("""
Example Question
- What is the orbital period and velocity of a satellite in a circular orbit around Earth at $600 \mathrm{~km}$ ?
- The orbital period is
$$
T=2 \pi \sqrt{\frac{a^3}{G M}}=2 \pi \sqrt{\frac{(6378000+600000)^3}{6.67 \cdot 10^{-11} \cdot 5.97 \cdot 10^{24}}}=5803 \mathrm{sec}=96.7 \mathrm{~min}
$$
- The orbital velocity is
$$
v=\sqrt{\frac{G M}{R_E+h}}=\sqrt{\frac{6.67 \cdot 10^{-11} \cdot 5.97 \cdot 10^{24}}{(6378000+600000)}}=7.56 \frac{\mathrm{km}}{\mathrm{s}}
$$
- In general, satellites in low Earth orbits (400-800 km altitudes) have periods of $\sim 92-100 \mathrm{~min}$ and velocities of $\sim 7.4-7.7 \mathrm{~km} / \mathrm{s}$
- Period increases with altitude whereas velocity decreases with it
- The special altitude that leads to a period of $24 \mathrm{~h}$ is about $36,000 \mathrm{~km}$. This is called a geosynchronous orbit.
""")
slide_text.append("""
Ground tracks
- The ground track is the projection of the position of satellite on the Earth's surface (lat,lon) over time
- They are a useful visualization of an orbit since they show which regions are "seen"
- Can infer orbital parameters from ground tracks
- Inclination from max latitude
- Period (and thus semimajor axis) from equatorial orbit shift between consecutive tracks
""")
slide_text.append("""
Orbital Precession
- In the absence of perturbations, the orbital plane would remain fix in space forever.
- However, because of the oblate shape (pear-like) of the Earth, the gravitational force of the Earth on a satellite does not pull directly downwards into the center of the Earth
- This creates a torque that causes the nodes of a spacecraft's orbit to move - i.e., a slow rotation of the orbital plane over time
- This movement is called nodal precession
""")
slide_text.append("""
3. Types of orbits
""")
slide_text.append("""
Types of Earth orbits
- Orbit selection is the most important decision in a space mission after payload selection
- Orbit affects the design of all key spacecraft subsystems and drives payload performance
- There are many different types of orbits. For example:
- By altitude:
- Low Earth Orbit (LEO): $h<3000 \mathrm{~km}$ (most $<800 \mathrm{~km}$ )
- Medium Earth Orbit (MEO): $3000 \mathrm{~km}<\mathrm{h}<36000 \mathrm{~km}$
- Geosynchronous (GEO): $h=36000 \mathrm{~km}$
- By inclination:
- Prograde: $0<i<90^{\circ}$
- Retrograde: $90^{\circ}<i<180^{\circ}$
- Polar: $i=90^{\circ}$
- Sun-synchronous: $i(h), 90^{\circ}<i<100^{\circ}$
- Tropical: $i \sim 20^{\circ}-30^{\circ}$
- Equatorial: $i \sim 0^{\circ}$
""")
slide_text.append("""
GEO orbit
: Geosynchronous: Period is exactly equal to 1 Earth's day
- Geostationary: Geosynchronous + equatorial $(1=0)$
- A geostationary satellite maintains nearly fixed position with respect to Earth (stays above a given region)
- For geostationary, the ground track is a point.
- For geosynchronous with $i, e>0$ it is an analemma (a figure " 8 ").
- Applications: communications, regional weather, IS\&R
- Very special and thus very congested orbit
""")
slide_text.append("""
Sun-synchronous orbit
- In Sun-synchronous orbits, $a$ and $i$ are carefully chosen so that nodal precession matches the Earth rotation around the Sun
- For SSO orbits, the local time of the Earth right below where the satellite is passing is approximately constant 
- Consequently, for a given latitude, observations are all made at the same local solar time increasing the quality of observations due to constant illumination conditions
""")
slide_text.append("""
4. Orbital maneuvers
""")
slide_text.append("""
What are spacecraft maneuvers?
- Spacecraft are never "stopped". They are always moving in space at very fast speeds.
- Spacecraft maneuvers are changes to the spacecraft speed and direction that result in a new spacecraft orbit (i.e. new orbital parameters)
- Orbital maneuvers are necessary for many operational reasons:
- Station keeping (e.g, raise altitude to compensate for atmospheric drag, stay within your allotted GEO slot)
- Observe a region of Earth sooner or more frequently
- Provide better coverage (e.g., comms) of a given region
- To do an orbital maneuver, a thruster applies a certain amount of force (thrust) for a certain duration (burn time) in a certain direction.
""")
slide_text.append("""
Delta V
- Consider an impulsive maneuver: a maneuver with a short burn time compared to the orbital period (typical assumption for analysis, realistic in many cases)
- It all happens as if:
\begin{tabular}{|c|c|c|}
\hline \multirow{2}{*}{\begin{tabular}{l} 
Position: $\boldsymbol{r}_1$ \\
Velocity: $\boldsymbol{V}_1$
\end{tabular}} & Impulsive maneuver & \multirow{2}{*}{\begin{tabular}{c} 
Position: $\boldsymbol{r}_1$ \\
Velocity: $\boldsymbol{V}_2=\boldsymbol{V}_1+\Delta \boldsymbol{V}$
\end{tabular}} \\
\hline & Force $\mathrm{F}$ for short time & \\
\hline
\end{tabular}
- The difference in velocities $\Delta \boldsymbol{V}$ dictates the new orbit
- Ex: If one burns in the direction of the current direction of travel, the orbit gets bigger (increase in semi-major axis and eccentricity) but the orbital plane stays the same
- In any case, the spacecraft always returns to the point where the last maneuver was made
- The change in velocity $\Delta \boldsymbol{V}$ is typically called "delta- $\boldsymbol{V}$ ".
- It is a measure of the cost of an orbital maneuver since higher $\Delta V$ means more fuel needed to perform the maneuver
- The sum of the magnitudes of delta-V for all the maneuvers throughout the spacecraft's lifetime is called the Delta-V budget
- Delta-V budget can be an important cost driver
- More on this to come
""")
slide_text.append("""
Types of orbital maneuvers
- In-plane maneuvers:
- $\Delta V$ in the orbital plane
- Typically to raise $a$ can also change $e$ and $\omega$
- Burn in the direction of $\vec{V}$ (tangential) for max efficiency
- Examples: Hohmann transfer from $400 \mathrm{~km}$ to $800 \mathrm{~km}$ requires $\Delta V=217 \frac{\mathrm{m}}{\mathrm{s}}$
- Out-of-plane maneuvers:
- $\Delta V$ has a component outside of the orbital plane
- Typically to change $i$ or $\Omega$
- Examples: Plane change from a $600 \mathrm{~km}$ polar (i $\left.=90^{\circ}\right)$ from a $600 \mathrm{~km} \mathrm{SSO}\left(\mathrm{i}=98.6^{\circ}\right)$ requires $\Delta V=217 \frac{\mathrm{m}}{\mathrm{s}}$
- As shown through the $\Delta V$ required for the in-plane and out-of-plane maneuver, out-of-plane maneuvers are usually much more expensive than in-plane maneuvers
""")














#
#
#
# slide_text.append("""
# Intro to Module 2
# In this module, you will get introduced to space missions and the space mission design process.
# The module consists of 4 short lectures:
#     Space environment. What makes space a harsh environment? How does it affect humans and spacecraft?
#     Introduction to orbits. What is an orbit and why is it important?
#     Types of orbits. What types of orbits are there? How does orbit selection affect spacecraft design?
#     Orbital maneuvers. How do different types of maneuvers work in space? Implications on spacecraft design.
# """)
# slide_text.append("""
# 1. Space Environment
# """)
# slide_text.append("""
# “Microgravity”
# Objects are in “free fall”, not absence of gravity!
#     Gravity compensated by centrifugal force due to orbital speed
# Near absence of gravity (~10-6 g) means that:
#     Objects don’t fall
#     Bubbles don’t rise
#     Particles don’t settle in a solution
#     No convection (eliminates an important heat transfer mechanism!)
# This presents challenges, mostly for astronauts…
#     Bone loss
#     Muscle loss
#     Cardiovascular problems
#     Immune system
# …but also opportunities
#     Formation of large crystals
# The effects on traditional Earth satellites are relatively benign (e.g., lower structural stresses when in orbit)
# """)
# slide_text.append("""
# Atmospheric drag – Orbit/attitude disturbance
# - We care about atmospheric density mostly because it affects the drag force (D) experienced by the satellite, which may lead to orbital decay and disturbance torques
# $$
# D=\frac{1}{2} \rho V^2 C_D A
# $$
# - $\rho\left(\frac{\mathrm{kg}}{\mathrm{m}^3}\right)$ is the atmospheric density (varies exponentially but very small in orbit)
# - $C_D$ is the unitless drag coefficient ( 2-4 are typical values for a spacecraft)
# - $V\left(\frac{m}{s}\right)$ is the orbital velocity
# - $A(m)$ is the drag area
# - Atmospheric drag is strong up to $\sim 500 \mathrm{~km}$, negligible after that
# """)
# slide_text.append("""
# Atomic Oxygen – Erosion
# In the upper layers of the atmosphere the predominant constituent is atomic oxygen (O), formed by photodissociation of O2
#  - O_2 + light = O + O
# Highly reactive and energetic
# It erodes satellite surfaces (teflon, epoxies, Mylar)
# Surfaces can be protected by coating them with something that is "immune" to O:
#  - silicon dioxide
#  - aluminum
# Source: http://esmat.esa.int/Atox_on_metals.PDF
# """)
# slide_text.append("""
# Vacuum – Outgassing
# Outgassing is the release of gas that was trapped in some material
#  - adhesives, insulators, thermal coating, electrical shields
# Vacuum facilitates outgassing due to decreased sublimation and evaporation points.
# Outgassed material tends to condense onto cooler surfaces.
#  - Optical elements, radiators, solar cells
# Reaction with UV radiation results in dark stains that may affect performance of instruments or solar panels.
# Some materials outgas more than others in vacuum (e.g., Cd, Zn, Mg, paints, etc.)
# """)
# slide_text.append("""
# Earth’s magnetic field
# The Earth has a magnetic field
#  - Protects us from radiation
#  - Generates forces that rotate spacecraft (can be leveraged using magnetic torquers)
# Magnetic field lines points from magnetic south to north
#  - Different from geographic equator and poles
# Intensity decreases with distance as 1/r^3
# Max at the magnetic equator, min at the magnetic poles
# """)
# slide_text.append("""
# Electromagnetic radiation
# Electromagnetic radiation is carried by waves and massless particles (named photons) that travel at the speed of light
# Waves are periodic:
#  - Wavelength is the distance between consecutive peaks
#  - Frequence is the time interval between consecutive peaks
# Frequency 'f' and wavelength 'lambda' are related to the speed of light 'c'
#  - f = c / lambda
# Energy of a photon is proportional to its frequency through the Planck constant h
#  - E = h*f = (h*c) / lambda
# """)
# slide_text.append("""
# -Which of the following statements are true?
# 1. Frequency is inversely proportional to wavelength
# 2. Frequency is directly proportional to wavelength
# 3. Energy is directly proportional to frequency
# 4. Energy is directly proportional to wavelength
# - Clearly, 1 and 3 are true, 2 and 4 ar false.
# """)
# slide_text.append("""
# Solar Radiation - Light, matter, and fields
# - Explosions in the Sun's atmosphere produce both
# - light (photons)
# - And matter (charged particles, such as ions and electrons)
# - This becomes radiation from the Sun
# - Solar flares are huge bursts of photons in all wavelengths but mostly X-rays and extreme UV (EUV)
# - $E \sim 10^{25} \mathrm{~J}$
# - Coronal Mass Ejections (CME) are made of particles (ions and electrons) ejected at very high speeds (solar wind)
# - From 0.2-3 CME/day
# - $\sim 500 \mathrm{~km} / \mathrm{s}$ ( $\sim 3$ days to get to Earth)
# - $\sim 10$ protons $/ \mathrm{cm} 3$
# """)
# slide_text.append("""
# Van Allen Radiation Belts
# The Van Allen Belts are 2 regions of trapped fast charged particles (electrons and protons)
#  - Inner belt: 1,000-6,000km altitude
#  - Outer belt: 13,000-60,000km
#  - Many satellites are in low orbits $(400-800 \mathrm{~km})$ below the inner belt, but many others are in higher orbits $(20000-36,000 \mathrm{~km})$ and thus are affected by the outer belt.
# The South Atlantic Anomaly is a range of longitudes where the Earth’s magnetic field is weaker and thus radiation is worse. Leads to more radiation-related spacecraft failures.
# """)
# slide_text.append("""
# 2. Introduction to orbits
# """)
# slide_text.append("""
# What are orbits?
# - Orbits are the trajectories that spacecraft follow around the Earth due to gravitational forces
# - Any two objects under each other's gravitational force will "orbit each other"
# - This is called the 2-body problem
# - The two objects orbit the center of mass of the system
# - When one's mass is much larger than the other's (e.g., a satellite vs Earth, or the Earth vs the Sun) the motion of the large object is largely unaffected, and it all happens as if the small object rotates around the large object
# """)
# slide_text.append("""
# Shape of orbits
# - Satellite orbits are generally ellipses
# - The center of mass of the system sits in one of the focus points
# - An ellipse is defined by 2 parameters:
# - The semimajor axis $a$ is half the length of the longer axis
# - Increasing $a$ makes the orbit "bigger", further from Earth
# - The eccentricity $e$ tells us how elongated the ellipse is
# - When $e=0$, the ellipse becomes a perfect circle
# - As e approaches 1 , it becomes more elongated
# - Together, $a$ and $e$ define the shape of the orbit
# """)
# slide_text.append("""
# Conic sections, open vs closed orbits
# More generally, orbital trajectories can follow the shape of any conic section (circle, ellipse, parabola, or hyperbola)
# Circular and elliptical orbits (0 <= eccentricity < 1) are "closed orbits" around earth
# A satellite with sufficient energy (eccentricity >= 1) will escape earth and follow an interplanetary trajectory that never comes back (i.e. open orbits)
#  - when eccentricity = 1, it follows a parabolic trajectory
#  - when eccentricity > 1 it follows a hyperbolic trajectory
# """)
# slide_text.append("""
# Position of a satellite within its orbit
# The true anomaly 'theta' is an angle that defines where within the orbit the satellite is at a given point in time.
# There are two special points:
#  - the perigee is the point where it is closest to the earth
#  - the apogee is the point where it is farthest from earth
# Given semi-major axis (a), eccentricity (e), and theta, we can compute the satellite position r, i.e. the distance betwseen the satellite and earth
#  - r(theta) = (a*(1-e^2))/(1+e*cos(theta))
#  - For example, the distance to the perigee $\left(\theta=0^{\circ}\right)$ is $r_p=a(1-e)$
#  - The distance to the apogee and apogee $\left(\theta=180^{\circ}\right)$ is $r_a=a(1+e)$
# """)
# slide_text.append("""
# Example Question
# - For an orbit with a semi-major axis of $1000 \mathrm{~km}$ and an ecentricity of 0.5 , what is the distance between the satellite and the Earth when the true anomaly is $60^{\circ}$ ?
# - The distance between the satellite and the Earth is
# $$
# r(\theta)=\frac{a\left(1-e^2\right)}{1+e \cos \theta}=\frac{10^6\left(1-0.5^2\right)}{1+0.5 \cos 60^0}=6 \cdot 10^5 \mathrm{~m}=600 \mathrm{~km}
# $$
# - The true anomaly is only $60^{\circ}$; therefore, the satellite is generally close to perigee. Therefore, the position or altitude above the Earth is much smaller than the semi-major axis of the orbit
# """)
# slide_text.append("""
# Orientation of the orbit and orbital plane
# - The orbit lies on a plane called the orbital plane that intersects the Earth's equatorial plane (i.e. at 0 degrees latitude) at two points called the nodes:
# - Ascending node: where the satellite is going up (north)
# - Descending node: where it is going down (south)
# - The orientation of the orbit (the ellipse) within the orbital plane is defined by an angle called the argument of the perigee
# - Angle from the ascending node to the perigee from the Earth center, $\omega$
# - The orientation of the orbital plane with respect to the Earth is defined by two angles:
# - The inclination $i$ is the "tilt" angle between the orbital plane and the equatorial plane
# - The right ascension of the ascending node (a.k.a. the RAAN), $\Omega$ is the "twist" angle of the orbital plane, from the Vernal equinox (a fixed direction in space) to the ascending node
# """)
# slide_text.append("""
# Orbital Period
# - Together the 6 orbital $a, e, i, \omega, \Omega, \theta$ parameters fully define the trajectory of the satellite
# - From these 6 parameters we can calculate anything: the satellite position, velocity, etc.
# - For example, from Kepler's laws, we can calculate the orbital period, i.e., the time it takes the satellite to go around its orbit once:
# $$
# T=2 \pi \sqrt{\frac{a^3}{G M}}
# $$
# - Where is the gravitational constant $G=6.67 \cdot 10^{-11} \frac{\mathrm{Nm}^2}{\mathrm{~kg}^2}$ and $M$ $=5.97 \cdot 10^{24} \mathrm{~kg}$ is the mass of the Earth
# - Note that period only depends on the semimajor axis!
# """)
# slide_text.append("""
# Orbital velocity
# - Similarly, using the vis-viva equation (conservation of energy), we can compute the velocity of the satellite:
# $$
# V=\sqrt{G M\left(\frac{2}{r}-\frac{1}{a}\right)}
# $$
# - For a general elliptical orbit, we see that as predicted by Kepler's laws, the satellite will move faster the closer it gets to Earth, and will slow down as it gets farther from Earth
# - For a circular orbit, $r=a=R_E+h$ where $R_E=6370 \mathrm{~km}$ is the radius of the Earth and $h$ is the orbit altitude. In this case, the velocity is constant:
# $$
# V=\sqrt{\frac{G M}{R_E+h}}
# $$
# """)
# slide_text.append("""
# Example Question
# - What is the orbital period and velocity of a satellite in a circular orbit around Earth at $600 \mathrm{~km}$ ?
# - The orbital period is
# $$
# T=2 \pi \sqrt{\\frac{a^3}{G M}}=2 \pi \sqrt{\\frac{(6378000+600000)^3}{6.67 \cdot 10^{-11} \cdot 5.97 \cdot 10^{24}}}=5803 \mathrm{sec}=96.7 \mathrm{~min}
# $$
# - The orbital velocity is
# $$
# v=\sqrt{\\frac{G M}{R_E+h}}=\sqrt{\\frac{6.67 \cdot 10^{-11} \cdot 5.97 \cdot 10^{24}}{(6378000+600000)}}=7.56 \\frac{\mathrm{km}}{\mathrm{s}}
# $$
# - In general, satellites in low Earth orbits (400-800 km altitudes) have periods of $\sim 92-100 \mathrm{~min}$ and velocities of $\sim 7.4-7.7 \mathrm{~km} / \mathrm{s}$
# - Period increases with altitude whereas velocity decreases with it
# - The special altitude that leads to a period of $24 \mathrm{~h}$ is about $36,000 \mathrm{~km}$. This is called a geosynchronous orbit.
# """)
# slide_text.append("""
# Ground tracks
# The ground track is the projection of the position of satellite on the Earth’s surface (lat,lon) over time
#  - They are a useful visualization of an orbit since they show which regions are “seen”
# Can infer orbital parameters from ground tracks
#  - Inclination from max latitude
#  - Period (and thus semimajor axis) from equatorial orbit shift between consecutive tracks
# """)
# slide_text.append("""
# Orbital Precession
# In the absence of perturbations, the orbital plane would remain fix in space forever.
# However, because of the oblate shape (pear-like) of the Earth, the gravitational force of the Earth on a satellite does not pull directly downwards into the center of the Earth
# This creates a torque that causes the nodes of a spacecraft’s orbit to move - i.e., a slow rotation of the orbital plane over time
# This movement is called nodal precession
# """)
# slide_text.append("""
# 3. Types of orbits
# """)
# slide_text.append("""
# Types of Earth orbits
# - Orbit selection is the most important decision in a space mission after payload selection
# - Orbit affects the design of all key spacecraft subsystems and drives payload performance
# - There are many different types of orbits. For example:
# - By altitude:
# - Low Earth Orbit (LEO): $h<3000 \mathrm{~km}$ (most $<800 \mathrm{~km}$ )
# - Medium Earth Orbit (MEO): $3000 \mathrm{~km}<\mathrm{h}<36000 \mathrm{~km}$
# - Geosynchronous (GEO): $h=36000 \mathrm{~km}$
# - By inclination:
# - Prograde: $0<i<90^{\circ}$
# - Retrograde: $90^{\circ}<i<180^{\circ}$
# - Polar: $i=90^{\circ}$
# - Sun-synchronous: $i(h), 90^{\circ}<i<100^{\circ}$
# - Tropical: $i \sim 20^{\circ}-30^{\circ}$
# - Equatorial: $i \sim 0^{\circ}$
# """)
# slide_text.append("""
# GEO orbit
# - Geosynchronous: Period is exactly equal to 1 Earth's day
# - Geostationary: Geosynchronous + equatorial $(\mathrm{i}=0)$
# - A geostationary satellite maintains nearly fixed position with respect to Earth (stays above a given region)
# - For geostationary, the ground track is a point.
# - For geosynchronous with $i, e>0$ it is an analemma (a figure " 8 ").
# - Applications: communications, regional weather, IS\&R
# - Very special and thus very congested orbit
# """)
# slide_text.append("""
# Sun-synchronous orbit
# - In Sun-synchronous orbits, $a$ and $i$ are carefully chosen so that nodal precession matches the Earth rotation around the Sun
# - For SSO orbits, the local time of the Earth right below where the satellite is passing is approximately constant
# - Consequently, for a given latitude, observations are all made at the same local solar time increasing the quality of observations due to constant illumination conditions
# """)
# slide_text.append("""
# 4. Orbital maneuvers
# """)
# slide_text.append("""
# What are spacecraft maneuvers?
# Spacecraft are never “stopped”. They are always moving in space at very fast speeds.
# Spacecraft maneuvers are changes to the spacecraft speed and direction that result in a new spacecraft orbit (i.e. new orbital parameters)
# Orbital maneuvers are necessary for many operational reasons:
# Station keeping (e.g, raise altitude to compensate for atmospheric drag, stay within your allotted GEO slot)
# Observe a region of Earth sooner or more frequently
# Provide better coverage (e.g., comms) of a given region
# To do an orbital maneuver, a thruster applies a certain amount of force (thrust) for a certain duration (burn time) in a certain direction.
# """)
# slide_text.append("""
# Delta V
# - Consider an impulsive maneuver: a maneuver with a short burn time compared to the orbital period (typical assumption for analysis, realistic in many cases)
# - The difference in velocities $\Delta \boldsymbol{V}$ dictates the new orbit
# - Ex: If one burns in the direction of the current direction of travel, the orbit gets bigger (increase in semi-major axis and eccentricity) but the orbital plane stays the same
# - In any case, the spacecraft always returns to the point where the last maneuver was made
# - The change in velocity $\Delta \boldsymbol{V}$ is typically called "delta- $V^{\prime \prime}$.
# - It is a measure of the cost of an orbital maneuver since higher $\Delta V$ means more fuel needed to perform the maneuver
# - The sum of the magnitudes of delta-V for all the maneuvers throughout the spacecraft's lifetime is called the Delta-V budget
# - Delta-V budget can be an important cost driver
# - More on this to come
# """)
# slide_text.append("""
# Types of orbital maneuvers
# - In-plane maneuvers:
# - $\Delta V$ in the orbital plane
# - Typically to raise $a$ can also change $e$ and $\omega$
# - Burn in the direction of $\\vec{V}$ (tangential) for max efficiency
# - Examples: Hohmann transfer from $400 \mathrm{~km}$ to $800 \mathrm{~km}$ requires $\Delta V=217 \\frac{\mathrm{m}}{\mathrm{s}}$
# - Out-of-plane maneuvers:
# - $\Delta V$ has a component outside of the orbital plane
# - Typically to change $i$ or $\Omega$
# - Examples: Plane change from a $600 \mathrm{~km}$ polar (i $\left.=90^{\circ}\\right)$ from a $600 \mathrm{~km} \mathrm{SSO}\left(\mathrm{i}=98.6^{\circ}\\right)$ requires $\Delta V=217 \\frac{\mathrm{m}}{\mathrm{s}}$
# - As shown through the $\Delta V$ required for the in-plane and out-of-plane maneuver, out-of-plane maneuvers are usually much more expensive than in-plane maneuvers
# """)
#
#




# slide_text.append("""
# Key space environment factors affecting spacecraft (and humans!)
#     Microgravity
#     Vacuum
#     Radiation
#     Atmospheric Drag
#     Atomic oxygen
#     Extreme Temperatures
#     Space Debris
# """)
# slide_text.append("""
# Atmosphere layers
# Troposphere (0-10km)
#     Where we are (weather, pollution)
# Stratosphere (10-50km)
#     Where airplanes and balloons are
#     Stratospheric chemistry
#     Ozone layer absorbs UV
# Mesosphere (50-80km)
#     Where suborbital flights go
# Thermosphere (80-400km)
#     Where very low earth satellites are
#     Atomic oxygen absorbs radiation
#     Ions
# Exosphere (>400km)
#     Where most satellites are
# """)
# slide_text.append("""
# Earth’s magnetosphere
# Magnetosphere is the region around Earth in which ions are controlled by the Earth’s magnetic field
# It protects us from solar and other radiation up to certain levels of energy
# """)
#
# slide_text.append("""
# Solar Radiation – Geomagnetic storms
# Geomagnetic storms are temporary disturbances in the Earth magnetosphere due to interaction with solar radiation
# They create: Solar energetic particle events, Geomagnetically induced currents, Ionospheric disturbances, Auroras
# This creates multiple problems for spacecraft and astronauts
#  - Drag
#  - Spacecraft charging
#  - Radiation poisoning
# And even affect Earth’s infrastructure such as power grids!
# """)
# slide_text.append("""
# Solar Cycle
# - Average total solar irradiance (energy per unit time and area) is about $1366 \mathrm{~W} / \mathrm{m}^2$
# - However, there are periodic variations on the order of $\pm 0.5 \mathrm{~W} / \mathrm{m}^2$
# - These fluctuations have a period of -11 years (solar cycle)
# - Can be observed through variations in solar spots
# - Thus, timing of launch within solar cycle affects atmospheric drag and amount of radiation
# """)
# slide_text.append("""
# Galactic Cosmic Rays
# - Galactic Cosmic Rays (GCR) are radiation from outside the solar system
# - From supernovae, black holes, etc
# - Much more energetic than solar radiation (GeV-PeV, where $1 \mathrm{eV}=1.6 \cdot 10^{-19} \mathrm{~J} ; G, T, P=$ $10^9, 10^{12}, 10^{15}$ respectively)
# - Protons or heavier ions traveling at relativistic speeds
# - Larger threat, especially for interplanetary missions
# - GCR is max at solar cycle minimum
# - Create Single Event Phenomena (SEP): Single particle can destroy an electronic component.
# """)
# slide_text.append("""
# Spacecraft Charging
# - As a result of charged particles looming around in space, a positive or negative charge can accumulate in a spacecraft's surface
# - Like when you walk on carpet
# - This can lead to very damaging electrostatic discharges
# - when you touch the doorknob
# - Spacecraft have to be carefully designed to mitigate this risk
# """)
# slide_text.append("""
# Radiation and shielding
# - In summary, the total dose of radiation comes from:
# - Sunlight (mostly UV photons)
# - Solar flares (EUV and X-rays)
# - Solar wind (low energy protons)
# - CME (medium-high energy protons)
# - Radiation belt (protons and electrons)
# - Galactic Cosmic Rays (relativistic heavy nuclei)
# - Spacecraft must shield against this radiation
# - Ex: Thick layer of aluminum, or water for human spaceflight.
# - The more total radiation dose expected during the mission's lifetime, the thicker the layer of aluminum must be.
# """)
# slide_text.append("""
# Orbital debris and meteoroids
# - Any non-operational object in orbit is considered debris
# - Includes mission-related debris, such as
# - Pieces of dead satellites
# - Pieces of launch vehicles (fairings, inter-stage adapters)
# - Others (e.g., Ed White's glove from Gemini 4 mission)
# - And naturally occurring debris
# - Micrometeoroids
# - Asteroid particles
# - Mostly concentrated around most populated orbits (e.g., GPS and GEO orbits)
# """)
# slide_text.append("""
# Orbital debris and meteroids
# - Can cause collisions that destroy [parts of] spacecraft
# - All objects above $10 \mathrm{~cm}$ are visible from Earth and are currently being monitored and carefully catalogued
# """)
# slide_text.append("""
# Spacecraft Thermal Environment
# - Spacecraft receive heat from
#     - the Sun (direct and reflected off Earth),
#     - the Earth,
#     - internal sources (e.g. electronics)
# - Variations in these contributions along a spacecraft's orbit can result in fast and extreme temperature changes
#     - When a spacecraft has large surface areas directly exposed to the Stun, it can get pretty hot
#     - When a spacecraft is behind Earth (there is no stunlight), we say it is in eclipse -it gets cold pretty quickly
# - To manage this heat, spacecraft rely primarily on radiation
#     - No convection in space (e.g. heat doesn't rise)
# - To control radiation, spacecraft often use coatings such as paints and thermal instulators with radiative properties specially designed for the mission
#     - More on this in the spacecraft subsystems modtule!
# """)



# slide_text.append("""
# Orbit perturbations - Effect of J2
# - In the absence of any perturbations, the orbital parameters $a, e, I, \omega, \Omega$ would stay constant over time
# - The orientation of the orbital plane would stay "fixed" independent of the motion of the Earth
# - In reality, the plane rotates over time primarily because the Earth is not a perfect sphere.
# - This is nodal precession, a change in $\operatorname{RAAN}$ over time $\dot{\Omega} \neq 0$
# - The Earth's shape is modeled using spherical harmonics with many coefficients terms
# - The largest coefficient is the ablateness of the Earth which is captured by the so-called $\mathbf{J}_2$ parameter
# - Rate of nodal precession is different for different orbits:
# $$
# \dot{\Omega}=-\frac{3}{2\left(1-e^2\right)^2} n J_2\left(\frac{R_{\mathrm{E}}}{a}\right)^2 \cos i
# $$
# - Where $n=\frac{2 \pi}{T}$ is called the mean motion
# - J2 also causes the argument of the perigee to rotate within the orbital plane $\dot{\omega} \neq 0$, which is called apsidal precession
# """)
#
#
#
#
#
# slide_text.append("""
# Atmosphere layers
# Troposphere (0-10km)
#     Where we are (weather, pollution)
# Stratosphere (10-50km)
#     Where airplanes and balloons are
#     Stratospheric chemistry
#     Ozone layer absorbs UV
# Mesosphere (50-80km)
#     Where suborbital flights go
# Thermosphere (80-400km)
#     Where very low earth satellites are
#     Atomic oxygen absorbs radiation
#     Ions
# Exosphere (>400km)
#     Where most satellites are
# """)
#
# slide_text.append("""
# Solar Radiation – Light, matter, and fields
# Explosions in the Sun's atmosphere produce both: light (photons), and matter (charged particles such as ions and electrons)
# This becomes radiation from the Sun
# Solar flares are huge bursts of photons in all wavelengths, but mostly x-rays and extreme UV (EUV): E ~ 10^25 J
# Coronal Mass Ejections (CME) are made of particles (ions and electrons) ejected at very high speeds (solar wind)
#  - from 0.2-3 CME/day
#  - ~500km/s (~3days to reach earth)
#  - ~10 protons/cm^3
# """)
#
# slide_text.append("""
# Solar cycle
# Average total solar irradiance (energy per unit time and area) is about 1366 W/m^2
# However, there are periodic variations on the order of +- 0.5W/m^2
# These fluctuations have a period of ~11 years (solar cycle)
# Can be observed through variations in solar spots
# Thus, timing of launch within solar cycle affects atmospheric drag and amount of radiation
# """)
# slide_text.append("""
# Galactic Cosmic Rays
# Galactic Cosmic Rays (GCR) are radiation from outside the solar system
#  - from supernovae, black holes, etc
# Much more energtic than solar radiation (GeV-PeV, where 1eV = 1.6*10^(-19); G, T, P = 10^9, 10^12, 10^15 respectively)
#  - Protons or heavier ions travelling at relativistic speeds
# Larger threat, especially for interplanetary missions
# GCR is max at solar cycle minumum
# Create Single Event Phenomena (SEP): Single particle can destroy an electronic component.
# """)
#
# slide_text.append("""
# Spacecraft charging
# As a result of charged particles looming around in space, a positive or negative charge can accumulate in a spacecraft’s surface
#  - Like when you walk on carpet
# This can lead to very damaging electrostatic discharges
#  - when you touch the doorknob
# Spacecraft have to be carefully designed to mitigate this risk
# """)
# slide_text.append("""
# Radiation and shielding
# In summary, the total dose of radiation comes from:
#  - Sunlight (mostly UV photons)
#  - Solar flares (EUV and X-rays)
#  - Solar wind (low energy protons)
#  - CME (medium-high energy protons)
#  - Radiation belt (protons and electrons)
#  - Galactic Cosmic Rays (relativistic heavy nuclei)
# Spacecraft must shield against this radiation
#  - Ex: Thick layer of aluminum, or water for human spaceflight.
# The more total radiation dose expected during the mission’s lifetime, the thicker the layer of aluminum must be.
# """)
# slide_text.append("""
# Orbital debris and meteoroids
# Any non-operational object in orbit is considered debris
# Includes mission-related debris, such as
#  - Pieces of dead satellites
#  - Pieces of launch vehicles (fairings, inter-stage adapters)
#  - Others (e.g., Ed White’s glove from Gemini 4 mission)
# And naturally occurring debris
#  - Micrometeoroids
#  - Asteroid particles
# Mostly concentrated around most populated orbits (e.g., GPS and GEO orbits)
# """)
# slide_text.append("""
# Orbital debris and meteoroids
# Can cause collisions that destroy [parts of] spacecraft
# All objects above 10cm are visible from Earth and are currently being monitored and carefully catalogued
# """)
# slide_text.append("""
# Spacecraft Thermal Environment
# Spacecraft receive heat from
#  - the Sun (direct and reflected off Earth),
#  - the Earth,
#  - internal sources (e.g., electronics)
# Variations in these contributions along a spacecraft’s orbit can result in fast and extreme temperature changes
#  - When a spacecraft has large surface areas directly exposed to the Sun, it can get pretty hot
#  - When a spacecraft is behind Earth (there is no sunlight), we say it is in eclipse – it gets cold pretty quickly
# To manage this heat, spacecraft rely primarily on radiation
#  - No convection in space (e.g., heat doesn’t rise)
# To control radiation, spacecraft often use coatings such as paints and thermal insulators with radiative properties specially designed for the mission
#  - More on this in the spacecraft subsystems module!
# """)
#
# slide_text.append("""
# Orientation of the orbit and orbital plane
# The orbit lies on a plane called the orbital plane that intersects the Earth's equatorial plane (i.e. at 0 degrees latitude) at two points called the nodes:
#  - Ascending node: where the satellite is going north
#  - Descending node: where it is going south
# The orientation of the orbit (the ellipse) within the orbital plane is defined by an angle called the argument of perigee
#  - Angle from the ascending node to the perigee from the earth center, 'w'
# The orientation of the orbital plane with respect to the Earth is defined by two angles:
#  - the inclination 'i' is the tilt angle between the orbital plane and the equatorial plane
#  - the right ascension of the ascending node (called RAAN) 'omega' is the twist angle of the orbital plane, from the vernal equinox (a fixed direction in space) to the ascending node.
# """)
# slide_text.append("""
# Orbital parameters, period
# Together, the 6 orbital parameters semi-major axis (a), eccentricity (e), inclination (i), argument of perigee (w), right ascension of the ascending node (omega), and true anomaly (theta) fully define the trajectory of the satellite
#  - from these 6 parameters, we can calculate anything: the satellite position, velocity, etc.
# For example, from kepler's laws, we can calculate the orbital period (T), aka the time it takes the satellite to go around its orbit once:
#  - T = (1/2*pi) * sqrt(a^3 / G*M)
# Where G = 6.67*10^(-11) (Newton * meter^2 / kilogram^2) is the gravitational constant and M = 5.97*10^24 kg is the mass of earth
# Note that it only depends on the semi-major axis!
# """)
# slide_text.append("""
# Orbital velocity
# Similarly, using the vis-viva equation (conservation of energy), we can compute the velocity of the satellite:
#  - V = sqrt(G*M*(2/r - 1/a)) where r is distance from earth and a is semi-major axis
# For a general elliptical orbit, we see that as predicted by Kepler's laws, the satellite will move faster the closer it gets to Earth, and will slow down as it gets farther from Earth
# For a circular orbit, r = a = R_e + h, where R_e = 6370km is the radius of earth and h is the orbit altitude. In this case, the velocity is constant:
#  - V = sqrt(G*M*(1/(R_e + h)))
# """)
# slide_text.append("""
# Example: What is the orbital period and velocity of a satellite in a circular orbit around Earth at 600km altitude?
# The orbital period is:
#  - T = (1/2pi) * sqrt(a^3/(G*M)) = 96.7min
# The orbital velocity is:
#  - V = sqrt((G*M)/(R_e + h)) = 7.56km/s
# In general, satellites in low Earth orbits (400-800km altitudes) have periods of ~92-100 minutes and velocities of ~7.4-7.7 km/s
# Period increases with altitude whereas velocity decreases with it
# The special altitude that leads to a period of 24h is about 36,000km, this is called a geosynchronous orbit
# """)
# slide_text.append("""
# Orbit perturbations – Effect of J2
# In the absence of any peturbations, the orbital parameters a, e, i, w, omega would stay constant over time
#  - The orientation of the orbital plane would stay fixed, independent of the motion of earth
# In reality, the plane rotates over time primarily because the earth is not a perfect sphere.
#  - This is nodal precession, a change in RAAN over time
#  - The earth's shape is modeled using spherical harmonics with many coefficients terms
#  - The largest coefficient is the ablateness of the earth, which is captured by the so-called J_2 parameter
# Rate of nodal precession is different for different orbits:
#  - precission_rate = -3/(2(1-e^2)^2) * n * J_2 * (R_e/a)^2 * cos(i), where n= 2pi / T
# J2 also causes the argument of the perigee to rotate within the orbital plane, which is called apsidal precession
# """)
# slide_text.append("""
# Orbit perturbations
# Another major orbit perturbation for very low Earth orbits is atmospheric drag which creates orbital decay below 600km
# There are several other sources of orbit perturbations:
#  - 3rd body effects (Moon and Sun) Solar radiation pressure
#  - Other harmonics (J4, J6), other planets, albedo, tidal effects, ...
# Magnitude of each depends strongly on altitude, but J2 is often strongest
# Example:
#  - For a satellite at 300km, drag is as strong as J2 (really dominates)
#  - At 800km, J2 dominates
#  - At 36,000km, the Sun/Moon effects are as strong as J2
# Because of all these perturbations, spacecraft use propellant to keep their orbit parameters constant
#  - This is called station-keeping
# """)
# slide_text.append("""
# Ground tracks
# The ground track is the projection of the position of satellite on the Earth’s surface (lat,lon) over time
#  - They are a useful visualization of an orbit since they show which regions are “seen”
# Can infer orbital parameters from ground tracks
#  - Inclination from max latitude
#  - Period (and thus semimajor axis) from equatorial orbit shift between consecutive tracks
# """)
# slide_text.append("""
#
# """)
# slide_text.append("""
#
# """)
# slide_text.append("""
#
# """)
# slide_text.append("""
#
# """)
#
# slide_text.append("""
#
# """)
# slide_text.append("""
#
# """)
# slide_text.append("""
#
# """)
#
#
#
#
#
#
























