from academy_assistant.database.client.modules.AbstractBuilder import AbstractBuilder
slide_text = ['']
import os
slide_text_dir = os.path.join('/home/ec2-user/academy-brain/academy_assistant/database/client/modules/slide_text', 'seo')

# Iterate over all txt files in slide_text_dir
for file in os.listdir(slide_text_dir):
    if file.endswith('.txt'):
        with open(os.path.join(slide_text_dir, file), 'r') as f:
            slide_text.append(f.read())


def get_module():
    builder = AbstractBuilder('mdi-orbit', ['Orbit Types', 'Orbital Mechanics', 'Orbital Maneuvers', 'Space Environment'], 'Intro to Space Commodities', None)

    # From slide 1 to slide 50
    builder.add_slide('ISC_SEO_1', slide_text[1], "https://academy2.selva-research.com/images/seo/Slide1.png")
    builder.add_slide('ISC_SEO_2', slide_text[2], "https://academy2.selva-research.com/images/seo/Slide2.png")
    builder.add_slide('ISC_SEO_3', slide_text[3], "https://academy2.selva-research.com/images/seo/Slide3.png")
    builder.add_slide('ISC_SEO_4', slide_text[4], "https://academy2.selva-research.com/images/seo/Slide4.png")
    builder.add_slide('ISC_SEO_5', slide_text[5], "https://academy2.selva-research.com/images/seo/Slide5.png")
    builder.add_slide('ISC_SEO_6', slide_text[6], "https://academy2.selva-research.com/images/seo/Slide6.png")
    builder.add_slide('ISC_SEO_7', slide_text[7], "https://academy2.selva-research.com/images/seo/Slide7.png")
    builder.add_slide('ISC_SEO_8', slide_text[8], "https://academy2.selva-research.com/images/seo/Slide8.png")
    builder.add_slide('ISC_SEO_9', slide_text[9], "https://academy2.selva-research.com/images/seo/Slide9.png")
    builder.add_slide('ISC_SEO_10', slide_text[10], "https://academy2.selva-research.com/images/seo/Slide10.png")
    builder.add_slide('ISC_SEO_11', slide_text[11], "https://academy2.selva-research.com/images/seo/Slide11.png")
    builder.add_slide('ISC_SEO_12', slide_text[12], "https://academy2.selva-research.com/images/seo/Slide12.png")
    builder.add_slide('ISC_SEO_13', slide_text[13], "https://academy2.selva-research.com/images/seo/Slide13.png")
    builder.add_slide('ISC_SEO_14', slide_text[14], "https://academy2.selva-research.com/images/seo/Slide14.png")
    builder.add_slide('ISC_SEO_15', slide_text[15], "https://academy2.selva-research.com/images/seo/Slide15.png")
    builder.add_slide('ISC_SEO_16', slide_text[16], "https://academy2.selva-research.com/images/seo/Slide16.png")
    builder.add_slide('ISC_SEO_17', slide_text[17], "https://academy2.selva-research.com/images/seo/Slide17.png")
    builder.add_slide('ISC_SEO_18', slide_text[18], "https://academy2.selva-research.com/images/seo/Slide18.png")
    builder.add_slide('ISC_SEO_19', slide_text[19], "https://academy2.selva-research.com/images/seo/Slide19.png")
    builder.add_slide('ISC_SEO_20', slide_text[20], "https://academy2.selva-research.com/images/seo/Slide20.png")
    builder.add_slide('ISC_SEO_21', slide_text[21], "https://academy2.selva-research.com/images/seo/Slide21.png")
    builder.add_slide('ISC_SEO_22', slide_text[22], "https://academy2.selva-research.com/images/seo/Slide22.png")
    builder.add_slide('ISC_SEO_23', slide_text[23], "https://academy2.selva-research.com/images/seo/Slide23.png")
    builder.add_slide('ISC_SEO_24', slide_text[24], "https://academy2.selva-research.com/images/seo/Slide24.png")
    builder.add_slide('ISC_SEO_25', slide_text[25], "https://academy2.selva-research.com/images/seo/Slide25.png")
    builder.add_slide('ISC_SEO_26', slide_text[26], "https://academy2.selva-research.com/images/seo/Slide26.png")
    builder.add_slide('ISC_SEO_27', slide_text[27], "https://academy2.selva-research.com/images/seo/Slide27.png")
    builder.add_slide('ISC_SEO_28', slide_text[28], "https://academy2.selva-research.com/images/seo/Slide28.png")
    builder.add_slide('ISC_SEO_29', slide_text[29], "https://academy2.selva-research.com/images/seo/Slide29.png")
    builder.add_slide('ISC_SEO_30', slide_text[30], "https://academy2.selva-research.com/images/seo/Slide30.png")
    builder.add_slide('ISC_SEO_31', slide_text[31], "https://academy2.selva-research.com/images/seo/Slide31.png")
    builder.add_slide('ISC_SEO_32', slide_text[32], "https://academy2.selva-research.com/images/seo/Slide32.png")
    builder.add_slide('ISC_SEO_33', slide_text[33], "https://academy2.selva-research.com/images/seo/Slide33.png")
    builder.add_slide('ISC_SEO_34', slide_text[34], "https://academy2.selva-research.com/images/seo/Slide34.png")
    builder.add_slide('ISC_SEO_35', slide_text[35], "https://academy2.selva-research.com/images/seo/Slide35.png")
    builder.add_slide('ISC_SEO_36', slide_text[36], "https://academy2.selva-research.com/images/seo/Slide36.png")
    builder.add_slide('ISC_SEO_37', slide_text[37], "https://academy2.selva-research.com/images/seo/Slide37.png")
    builder.add_slide('ISC_SEO_38', slide_text[38], "https://academy2.selva-research.com/images/seo/Slide38.png")
    builder.add_slide('ISC_SEO_39', slide_text[39], "https://academy2.selva-research.com/images/seo/Slide39.png")
    builder.add_slide('ISC_SEO_40', slide_text[40], "https://academy2.selva-research.com/images/seo/Slide40.png")
    builder.add_slide('ISC_SEO_41', slide_text[41], "https://academy2.selva-research.com/images/seo/Slide41.png")
    builder.add_slide('ISC_SEO_42', slide_text[42], "https://academy2.selva-research.com/images/seo/Slide42.png")
    builder.add_slide('ISC_SEO_43', slide_text[43], "https://academy2.selva-research.com/images/seo/Slide43.png")
    builder.add_slide('ISC_SEO_44', slide_text[44], "https://academy2.selva-research.com/images/seo/Slide44.png")
    builder.add_slide('ISC_SEO_45', slide_text[45], "https://academy2.selva-research.com/images/seo/Slide45.png")
    builder.add_slide('ISC_SEO_46', slide_text[46], "https://academy2.selva-research.com/images/seo/Slide46.png")
    builder.add_slide('ISC_SEO_47', slide_text[47], "https://academy2.selva-research.com/images/seo/Slide47.png")
    builder.add_slide('ISC_SEO_48', slide_text[48], "https://academy2.selva-research.com/images/seo/Slide48.png")
    builder.add_slide('ISC_SEO_49', slide_text[49], "https://academy2.selva-research.com/images/seo/Slide49.png")
    builder.add_slide('ISC_SEO_50', slide_text[50], "https://academy2.selva-research.com/images/seo/Slide50.png")




    builder.add_quiz_start_slide()

    builder.add_mc_question(
        'What is the ratio of periods of a GEO orbit to a Molniya orbit?',
        [
            {'text': '2', 'correct': False, 'id': 0},
            {'text': '1', 'correct': False, 'id': 1},
            {'text': 'At least 10', 'correct': False, 'id': 2},
            {'text': 'Need more information', 'correct': True, 'id': 3}
        ],
        '',
        ['Orbit Types'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'X and Y are two circular orbits. The orbit altitude of X is more than that of Y. Which of the following is true?',
        [
            {'text': 'X moves faster than Y', 'correct': False, 'id': 0},
            {'text': 'Y moves faster than X', 'correct': True, 'id': 1},
            {'text': 'The relation between X and Y in terms of orbital velocity can not be determined',
             'correct': False, 'id': 2},
            {'text': 'They are the same speed', 'correct': False, 'id': 3}
        ],
        '',
        ['Orbital Mechanics'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'Given the guideline by the FCC to deorbit a satellite in LEO at the end of life, what is the most fuel efficient way to adhere to it?',
        [
            {'text': 'Lower the perigee to 0km', 'correct': False, 'id': 0},
            {'text': 'Lower the perigee to a value where drag will eventually deorbit the satellite within five years',
             'correct': True, 'id': 1},
            {'text': 'Raise the orbit until it is placed in a graveyard orbit', 'correct': False, 'id': 2},
            {'text': 'Perform a Hohmann transfer to an orbit altitude of 100km', 'correct': False, 'id': 3}
        ],
        '',
        ['Orbital Maneuvers'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'To launch an object into an orbit with an inclination of 51.6 degrees, which launch site would be the best assuming there is enough infrastructure and ignoring geopolitical aspects?',
        [
            {'text': 'A location near the equator such as French Guiana or the Canary Islands', 'correct': False,
             'id': 0},
            {'text': 'A northern location such as Alaska', 'correct': False, 'id': 1},
            {'text': 'It doesn’t matter where it is launched from', 'correct': False, 'id': 2},
            {'text': 'A mid latitude location such as Baikonur or Cape Canaveral', 'correct': True, 'id': 3}
        ],
        '',
        ['Orbital Mechanics'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'Which answer lists orbital maneuvers in order of most fuel expensive to least?',
        [
            {
                'text': 'Inclination change of 10 degrees, 100km perigee raise burning at 45 degrees to velocity, 100km perigee raise burning tangent to velocity',
                'correct': True, 'id': 0},
            {
                'text': '100km perigee raise burning at 45 degrees to velocity, Inclination change of 10 degrees, 100km perigee raise burning tangent to velocity',
                'correct': False, 'id': 1},
            {
                'text': '100km perigee raise burning at 45 degrees to velocity, 100km perigee raise burning tangent to velocity, Inclination change of 10 degrees',
                'correct': False, 'id': 2},
            {'text': 'They are all about the same delta V cost', 'correct': False, 'id': 3}
        ],
        '',
        ['Orbital Maneuvers'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )
    
    builder.add_quiz_end_slide()

    builder.add_mc_question(
        'Starting from a circular orbit, what is the least amount of burns needed to rendez-vous another spacecraft in a larger circular orbit (just to match its orbit, ignoring the detailed proximity operations)?',
        [
            {'text': '1', 'correct': False, 'id': 0},
            {'text': '2', 'correct': True, 'id': 1},
            {'text': '3', 'correct': False, 'id': 2},
            {'text': '4', 'correct': False, 'id': 3}
        ],
        '',
        ['Orbital Maneuvers'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'If launching a satellite, which list goes from least expensive to most expensive orbit to get to?',
        [
            {'text': 'LEO, GEO, MEO', 'correct': False, 'id': 0},
            {'text': 'GEO, MEO, LEO', 'correct': False, 'id': 1},
            {'text': 'LEO, MEO, GEO', 'correct': True, 'id': 2},
            {'text': 'It always depends on the rocket configurations.', 'correct': False, 'id': 3}
        ],
        '',
        ['Orbit Types'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'What is the difference between coronal mass ejections and solar flares?',
        [
            {'text': 'Solar flares are solar radiation but coronal mass ejections come from outside the solar system',
             'correct': False, 'id': 0},
            {'text': 'Coronal mass ejections are made of light whereas solar flares are made of particles',
             'correct': False, 'id': 1},
            {'text': 'Coronal mass ejections are made of ions and electrons whereas solar flares are made of photons',
             'correct': True, 'id': 2},
            {'text': 'Only coronal mass ejections are dangerous', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Environment'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'What are ways that orbital debris can increase mission cost?',
        [
            {'text': 'Make certain orbits nearly unusable', 'correct': False, 'id': 0},
            {'text': 'Need fuel for collision avoidance maneuvers', 'correct': False, 'id': 1},
            {'text': 'Can damage spacecraft', 'correct': False, 'id': 2},
            {'text': 'all of the these are correct', 'correct': True, 'id': 3}
        ],
        '',
        ['Space Environment'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'For which satellite would radiation likely be more of a concern?',
        [
            {'text': 'A small CubeSat in LEO', 'correct': False, 'id': 0},
            {'text': 'A GPS satellite', 'correct': True, 'id': 1},
            {'text': 'Both a and b since they both lie in one of the Van Allen radiation belts', 'correct': False,
             'id': 2},
            {'text': 'A polar weather satellite', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Environment', 'Orbit Types'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'What is a way that geomagnetic storms can create problems for satellites in LEO?',
        [
            {'text': 'They can increase drag', 'correct': True, 'id': 0},
            {'text': 'They can lead to increased outgassing', 'correct': False, 'id': 1},
            {'text': 'They can erode surfaces due to increased atomic oxygen', 'correct': False, 'id': 2},
            {'text': 'All of the above', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Environment'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following materials is more “immune” to erosion by atomic oxygen?',
        [
            {'text': 'Teflon', 'correct': True, 'id': 0},
            {'text': 'Aluminum', 'correct': False, 'id': 1},
            {'text': 'Epoxy', 'correct': False, 'id': 2},
            {'text': 'Mylar', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Environment'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'What is the range of orbital periods in LEO?',
        [
            {'text': '10-12 hours', 'correct': False, 'id': 0},
            {'text': '6-8 hours', 'correct': False, 'id': 1},
            {'text': '3-4 hours', 'correct': False, 'id': 2},
            {'text': '90-100 minutes', 'correct': True, 'id': 3}
        ],
        '',
        ['Orbit Types'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'A satellite will experience more drag(D) if there is _____ ?',
        [
            {'text': 'More atmospheric density', 'correct': False, 'id': 0},
            {'text': 'Higher altitude since that leads to higher velocity', 'correct': False, 'id': 1},
            {'text': 'Larger area perpendicular to the velocity vector', 'correct': False, 'id': 2},
            {'text': 'Both a and c', 'correct': True, 'id': 3}
        ],
        '',
        ['Space Environment'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following is true?',
        [
            {'text': 'The magnetic field of the Earth can be used to rotate the spacecraft without using fuel',
             'correct': True, 'id': 0},
            {'text': 'The magnetic field of the Earth causes radiation to the earth', 'correct': False, 'id': 1},
            {'text': 'The magnetic field lines of the Earth point from the geographic equator to the geographic poles',
             'correct': False, 'id': 2},
            {'text': 'None of the above', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Environment'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of these is the least harmful radiation to a spacecraft?',
        [
            {'text': 'Solar flares', 'correct': False, 'id': 0},
            {'text': 'Galactic cosmic rays', 'correct': False, 'id': 1},
            {'text': 'Earth’s thermal emission', 'correct': True, 'id': 2},
            {'text': 'Van Allen Radiation Belt', 'correct': False, 'id': 3}
        ],
        '',
        ['Space Environment'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following describes the ground track of a general geosynchronous orbit?',
        [
            {'text': 'A circle or ellipse', 'correct': False, 'id': 0},
            {'text': 'A point', 'correct': False, 'id': 1},
            {'text': 'A sinusoidal wave', 'correct': False, 'id': 2},
            {'text': 'An analemma (figure ‘8’)', 'correct': True, 'id': 3}
        ],
        '',
        ['Orbit Types'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which orbit likely has the highest station keeping costs?',
        [
            {'text': 'LEO', 'correct': False, 'id': 0},
            {'text': 'MEO', 'correct': False, 'id': 1},
            {'text': 'GEO', 'correct': True, 'id': 2},
            {'text': 'SSO', 'correct': False, 'id': 3}
        ],
        '',
        ['Orbit Types'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following factors would increase the delta V budget of a spacecraft?',
        [
            {'text': 'Being injected in a slightly different inclination from the required one', 'correct': False,
             'id': 0},
            {'text': 'Having to increase the constantly change the orbit to image other satellites', 'correct': False,
             'id': 1},
            {'text': 'Needing to keep the satellite within a narrower orbital slot', 'correct': False, 'id': 2},
            {'text': 'All of the above', 'correct': True, 'id': 3}
        ],
        '',
        ['Orbital Mechanics'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'What makes sun-synchronous orbits unique?',
        [
            {'text': 'The normal face of the satellite is always pointed towards the sun', 'correct': False, 'id': 0},
            {'text': 'The angle between the orbital plane and the Sun-Earth vector is constant', 'correct': True,
             'id': 1},
            {'text': 'The satellite remains in a fixed position with respect to the Earth', 'correct': False, 'id': 2},
            {'text': 'It is always dawn or dusk local time when the satellite goes over a location', 'correct': False,
             'id': 3}
        ],
        '',
        ['Orbit Types'],
        difficulty=0.5,
        discrimination=10,
        graded=True
    )

    builder.add_exam_finish_slide()

    return builder.get_module()

    












    # builder.add_mc_question(
    #     'Which of the following would be a unique concern with sending a satellite to an orbit with a height of $36000 \mathrm{~km}$?',
    #     [
    #         {'text': 'This height is further than the outermost Earth orbit', 'correct': False, 'id': 0},
    #         {'text': 'The gravitational pull from other planets would affect the Satellite', 'correct': False, 'id': 1},
    #         {'text': 'High orbit traffic', 'correct': True, 'id': 2},
    #         {'text': 'There is little merit in sending a satellite to this height', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'Why does atmospheric density have a significant impact on satellites in low Earth orbit (LEO)?',
    #     [
    #         {'text': 'It affects the amount of solar energy received by the satellite', 'correct': False, 'id': 0},
    #         {'text': 'It disrupts the communication signals between the satellite and the ground', 'correct': False,
    #          'id': 1},
    #         {'text': 'It creates drag that can lead to orbital decay and require corrections', 'correct': True,
    #          'id': 2},
    #         {'text': 'It increases the temperature of the satellite due to friction', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     "What role does Earth's magnetic field have in environmental protection?",
    #     [
    #         {'text': 'The magnetic field deflects solar winds carrying particles from CMEs', 'correct': True, 'id': 0},
    #         {'text': 'The magnetic field absorbs all charged particles in solar winds', 'correct': False, 'id': 1},
    #         {'text': 'The magnetic field directs particles to the magnetic poles, leading them to Earth',
    #          'correct': False, 'id': 2},
    #         {'text': 'The magnetic field does not affect the solar particles', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What causes the photodissociation of $\mathrm{O}_2$?',
    #     [
    #         {'text': 'Light', 'correct': True, 'id': 0},
    #         {'text': 'Aurora', 'correct': False, 'id': 1},
    #         {'text': 'CO2', 'correct': False, 'id': 2},
    #         {'text': 'Orbital dissociation', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What is the lifetime of a CubeSat at $400 \mathrm{~km}$, and at $600 \mathrm{~km}$?',
    #     [
    #         {'text': '1-9 months, over 25 years', 'correct': True, 'id': 0},
    #         {'text': '1-9 years, over 25 years', 'correct': False, 'id': 1},
    #         {'text': 'Over 25 years, 1-9 months', 'correct': False, 'id': 2},
    #         {'text': 'Over 25 years, 1-9 years', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following constitutes a 2-body problem?',
    #     [
    #         {'text': '2 objects in freefall are repelled by each other\'s gravitational field', 'correct': False,
    #          'id': 0},
    #         {'text': '2 objects are parallel to each other in free fall', 'correct': False, 'id': 1},
    #         {
    #             'text': '2 objects are in orbit with each other, and their motion is only affected by forces caused by the other object',
    #             'correct': True, 'id': 2},
    #         {'text': '2 objects in orbit with each other with a third object influencing their motion',
    #          'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'A satellite\'s orbit is an ellipse with a semimajor axis (a) of 10,000 km and an eccentricity (e) of 0.2. How does this orbit compare to a circular orbit with the same semimajor axis?',
    #     [
    #         {'text': 'It is slightly elongated but has a similar overall size as the circular orbit', 'correct': True,
    #          'id': 0},
    #         {'text': 'It is smaller and lies entirely within the circular orbit.', 'correct': False, 'id': 1},
    #         {'text': 'It is larger and encloses the circular orbit.', 'correct': False, 'id': 2},
    #         {'text': 'The comparison cannot be determined without additional information', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What is the primary difference between a closed and an open orbit for a satellite around Earth?',
    #     [
    #         {'text': 'The satellite\'s speed is higher in a closed orbit', 'correct': False, 'id': 0},
    #         {'text': 'In a closed orbit the satellite revolves around the Earth, in an open orbit it does not',
    #          'correct': True, 'id': 1},
    #         {'text': 'The satellite experiences a wider range of temperatures in a closed orbit', 'correct': False,
    #          'id': 2},
    #         {'text': 'Closed orbits are within the Low Earth Orbit range', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What orbit perturbations can a satellite at 300 km experience?',
    #     [
    #         {'text': 'Atmospheric drag', 'correct': False, 'id': 0},
    #         {'text': 'Earth\'s oblateness', 'correct': False, 'id': 1},
    #         {'text': 'Force due to the moon and Sun', 'correct': False, 'id': 2},
    #         {'text': 'all of these', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'When referring to a satellite\'s perigee and apogee, which statement is true?',
    #     [
    #         {'text': 'The apogee represents the closest point of orbit to earth', 'correct': False, 'id': 0},
    #         {'text': 'The perigee is always located on the semi-major axis of the ellipse', 'correct': False, 'id': 1},
    #         {'text': 'The apogee and perigee always lie on the same line passing through the Earth\'s center',
    #          'correct': True, 'id': 2},
    #         {'text': 'The satellite\'s speed is highest at its apogee and lowest at its perigee', 'correct': False,
    #          'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_quiz_end_slide()
    #
    # builder.add_mc_question(
    #     'Outgassing is due to the environment in space being ______.',
    #     [
    #         {'text': 'low gravity', 'correct': False, 'id': 0},
    #         {'text': 'high in radiation', 'correct': False, 'id': 1},
    #         {'text': 'a near vacuum', 'correct': True, 'id': 2},
    #         {'text': 'much hotter than Earth temperatures', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Why is it most important to prevent the effects of outgassing?',
    #     [
    #         {'text': 'It can damage the structural integrity of the spacecraft', 'correct': False, 'id': 0},
    #         {'text': 'It can result in stains that affect solar panels or performance of instruments', 'correct': True,
    #          'id': 1},
    #         {'text': 'It can result in a degradation of the protective material for radiation', 'correct': False,
    #          'id': 2},
    #         {'text': 'It is only important for interplanetary travel', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     "Where is Earth's magnetic field the strongest?",
    #     [
    #         {'text': 'The poles', 'correct': False, 'id': 0},
    #         {'text': '45 degrees North', 'correct': False, 'id': 1},
    #         {'text': 'The equator', 'correct': True, 'id': 2},
    #         {'text': '45 degrees South', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     "Where are the ions controlled by the Earth's magnetic field?",
    #     [
    #         {'text': 'Stratosphere', 'correct': False, 'id': 0},
    #         {'text': 'Ionosphere', 'correct': False, 'id': 1},
    #         {'text': 'Exosphere', 'correct': False, 'id': 2},
    #         {'text': 'Magnetosphere', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'How can Solar Radiation/Geomagnetic storms affect spacecraft and astronauts?',
    #     [
    #         {'text': 'Drag', 'correct': False, 'id': 0},
    #         {'text': 'Spacecraft charging', 'correct': False, 'id': 1},
    #         {'text': 'Radiation poisoning', 'correct': False, 'id': 2},
    #         {'text': 'All of the above', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Space Environment'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following statements accurately describes the relationship between the inclination (i) and the right ascension of the ascending node (RAAN) (Omega) in defining the satellite\'s orbital plane?',
    #     [
    #         {
    #             'text': 'They both represent the same angle between the orbital plane and the Earth\'s equatorial plane, just two different popular notations representing the same thing',
    #             'correct': False, 'id': 0},
    #         {
    #             'text': 'Both i and Omega contribute to defining the plane\'s orientation, but they are not directly related to each other',
    #             'correct': True, 'id': 1},
    #         {
    #             'text': 'Omega defines the tilt of the plane with respect to the equatorial plane, while i represents the "twist" angle from the vernal equinox',
    #             'correct': False, 'id': 2},
    #         {'text': 'Only RAAN (Omega) is necessary to fully define the orientation of the orbital plane',
    #          'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following represents the value of r in the Satellite Velocity equation?',
    #     [
    #         {'text': 'The length of the semimajor axis', 'correct': False, 'id': 0},
    #         {'text': 'The distance from the center of the central body to the satellite', 'correct': True, 'id': 1},
    #         {'text': 'The distance between the satellite and the surface of the central body', 'correct': False,
    #          'id': 2},
    #         {'text': 'The distance between the center of the central body and its surface', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'The satellite\'s velocity in an elliptical orbit?',
    #     [
    #         {'text': 'Remains constant throughout its entire journey', 'correct': False, 'id': 0},
    #         {'text': 'Is directly proportional to its distance from Earth', 'correct': False, 'id': 1},
    #         {'text': 'Depends solely on the satellite\'s mass and the Earth\'s mass', 'correct': False, 'id': 2},
    #         {'text': 'Increases as it approaches Earth and decreases as it moves away', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the period of a satellite in geosynchronous orbit?',
    #     [
    #         {'text': 'Not enough information is given', 'correct': False, 'id': 0},
    #         {'text': '365 days', 'correct': False, 'id': 1},
    #         {'text': '24 hours', 'correct': True, 'id': 2},
    #         {'text': '12 hours', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'If a satellite is in GEO/MEO what is the most suitable deorbit strategy?',
    #     [
    #         {
    #             'text': 'Burn in the opposite direction of velocity to decrease the radius of orbit until there is some drag on a section of the orbit',
    #             'correct': False, 'id': 0},
    #         {
    #             'text': 'Burn in the same direction of velocity to increase the radius of orbit until it is placed in a graveyard orbit',
    #             'correct': True, 'id': 1},
    #         {'text': 'both a and b', 'correct': False, 'id': 2},
    #         {'text': 'neither a or b', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Orbits'],
    #     difficulty=0.75,
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
    # builder.add_exam_finish_slide()
    # return builder.get_module()









