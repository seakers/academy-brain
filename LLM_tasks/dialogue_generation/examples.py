examples = [

    ##############################
    ### Space Mission Overview ###
    ##############################
    [
        ('user', 'What is the purpose of the communications segment?'),
        ('assistant', '(SpaceMissionOverview) What is the purpose of the communications segment?'),
        ('assistant', 'ANSWER: The purpose of the communications segment is... (SpaceMissionOverview, Slide 29)'),
    ],
    [
        ('user', 'Compare and contrast mission design phases A and B'),
        ('assistant', '(SpaceMissionOverview) What happens during mission design phase A?'),
        ('assistant', '(SpaceMissionOverview) What happens during mission design phase B?'),
        ('assistant', 'ANSWER: Mission design phase A... (SpaceMissionOverview, Slide 34, Slide 35)'),
    ],



    ####################################
    ### Space Environment And Orbits ###
    ####################################
    [
        ('user', 'How is atmospheric drag calculated for a satellite?'),
        ('assistant', '(SpaceEnvironmentAndOrbits) How is atmospheric drag calculated?'),
        ('assistant', 'ANSWER: Atmospheric drag is calculated with... (SpaceEnvironmentAndOrbits, Slide 7)'),
    ],
    [
        ('user', 'What is the difference between the Troposphere and Mesosphere?'),
        ('assistant', '(SpaceEnvironmentAndOrbits) Describe the Troposphere in detail.'),
        ('assistant', '(SpaceEnvironmentAndOrbits) Describe the Mesosphere in detail.'),
        ('assistant', 'ANSWER: The difference between the Troposphere and Mesosphere is... (SpaceEnvironmentAndOrbits, Slide 6)'),
    ],

    #################
    ### User Info ###
    #################

    [
        ('user', 'Summarize this slide for me.'),
        ('assistant', '(UserInfo) Explain the content of the slide the user is viewing.'),
        ('assistant', 'ANSWER: This slide describes the different... (UserInfo, Slide 1)'),
    ],

    [
        ('user', 'What learning modules am I assigned?'),
        ('assistant', '(UserInfo) Which learning modules are assigned to the user?'),
        ('assistant', 'ANSWER: You are assigned the following learning modules... (UserInfo, Slide 1)'),
    ],

]