from academy_assistant.database.client.modules.AbstractBuilder import AbstractBuilder


def get_module():
    builder = AbstractBuilder('mdi-satellite', ['Intro To Space'], 'Intro to Space Commodities', None)

    builder.add_slide('ITSC_1', slide_text[1])
    builder.add_slide('ITSC_2', slide_text[2])
    builder.add_slide('ITSC_3', slide_text[3])
    builder.add_slide('ITSC_4', slide_text[4])
    builder.add_slide('ITSC_5', slide_text[5])
    builder.add_slide('ITSC_6', slide_text[6])
    builder.add_slide('ITSC_7', slide_text[7])
    builder.add_slide('ITSC_8', slide_text[8])
    builder.add_slide('ITSC_9', slide_text[9])
    builder.add_slide('ITSC_10', slide_text[10])
    builder.add_slide('ITSC_11', slide_text[11])
    builder.add_slide('ITSC_12', slide_text[12])
    builder.add_slide('ITSC_13', slide_text[13])
    builder.add_slide('ITSC_14', slide_text[14])
    builder.add_slide('ITSC_15', slide_text[15])
    builder.add_slide('ITSC_16', slide_text[16])
    builder.add_slide('ITSC_17', slide_text[17])
    builder.add_slide('ITSC_18', slide_text[18])
    builder.add_slide('ITSC_19', slide_text[19])
    builder.add_slide('ITSC_20', slide_text[20])
    builder.add_slide('ITSC_21', slide_text[21])
    builder.add_slide('ITSC_22', slide_text[22])
    builder.add_slide('ITSC_23', slide_text[23])
    builder.add_slide('ITSC_24', slide_text[24])
    builder.add_slide('ITSC_25', slide_text[25])
    builder.add_slide('ITSC_26', slide_text[26])
    builder.add_slide('ITSC_27', slide_text[27])
    builder.add_slide('ITSC_28', slide_text[28])
    builder.add_slide('ITSC_29', slide_text[29])

    # builder.add_slide('ITSC_30', slide_text[30])
    # builder.add_slide('ITSC_31', slide_text[31])
    # builder.add_slide('ITSC_32', slide_text[32])
    # builder.add_slide('ITSC_33', slide_text[33])
    # builder.add_slide('ITSC_34', slide_text[34])
    # builder.add_slide('ITSC_35', slide_text[35])
    # builder.add_slide('ITSC_36', slide_text[36])
    # builder.add_slide('ITSC_37', slide_text[37])
    # builder.add_slide('ITSC_38', slide_text[38])
    # builder.add_slide('ITSC_39', slide_text[39])
    # builder.add_slide('ITSC_40', slide_text[40])

    builder.add_quiz_start_slide()

    # Quiz
    # mc 1
    # tf 3
    # mc 10
    # mc 11
    # mc 13

    builder.add_mc_question(
        'Which of the following is not a motivation to go to space?',
        [
            {'text': 'Obtaining Resources', 'correct': False, 'id': 0},
            {'text': 'Local imaging with higher resolution than from the ground', 'correct': True, 'id': 1},
            {'text': 'Space Exploration', 'correct': False, 'id': 2},
            {'text': 'Utilization of Zero Gravity', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )
    builder.add_tf_question(
        'Orbital velocity is the velocity at which the centrifugal force exactly compensates for atmospheric drag.',
        False,
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=False
    )
    builder.add_mc_question(
        'Which of the following is likely to be the best prediction of spacecraft cost?',
        [
            {'text': 'Satellite dry mass', 'correct': False, 'id': 0},
            {'text': 'Satellite power at beginning of life', 'correct': False, 'id': 1},
            {'text': 'Propellant mass', 'correct': False, 'id': 2},
            {'text': 'A complexity index accounting for several factors including all of the above', 'correct': True, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )
    builder.add_mc_question(
        'What is NOT an example of an Earth observation satellite.',
        [
            {'text': 'A satellite that sends data from a user on the ground to another', 'correct': True,
             'id': 0},
            {'text': 'A satellite that maps soil moisture', 'correct': False, 'id': 1},
            {'text': 'A satellite that tracks ground events with unusual thermal signatures', 'correct': False, 'id': 2},
            {'text': 'A satellite that measures sea level height', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.5,
        discrimination=10,
        graded=False
    )
    builder.add_mc_question(
        'What are the three types of payloads discussed in the module',
        [
            {'text': 'Observation, Communications, Navigation', 'correct': True,
             'id': 0},
            {'text': 'Science, Imaging, Navigation', 'correct': False, 'id': 1},
            {'text': 'Science, Communications, Military', 'correct': False, 'id': 2},
            {'text': 'Imaging, Communication, Navigation', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=False
    )

    builder.add_quiz_end_slide()

    # # Exam
    # # 2 mc
    # # 4 mc
    # # 5 mc
    # # 6 mc
    # # 7 mc
    # # 8 tf
    # # 9 mc
    # # 12 mc
    # # 14 mc
    # # 15 mc
    #
    builder.add_mc_question(
        'Why is getting into space so difficult?',
        [
            {'text': 'Necessity of a large amount of Kinetic Energy', 'correct': True,
             'id': 0},
            {'text': 'Strict regulation of propulsion technology', 'correct': False, 'id': 1},
            {'text': 'Radiation present in the ozone layer interferes with rockets', 'correct': False, 'id': 2},
            {'text': 'Companies disrupting the market and raising costs', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What contributes to 90% of the launch weight of rockets?',
        [
            {'text': 'Payload', 'correct': False, 'id': 0},
            {'text': 'Engines', 'correct': False, 'id': 1},
            {'text': 'Propellant', 'correct': True, 'id': 2},
            {'text': 'Structural Frame', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'What is the average cost of access to space?',
        [
            {'text': '$100/kg', 'correct': False,
             'id': 0},
            {'text': '$10/kg', 'correct': True, 'id': 1},
            {'text': '$1M/kg', 'correct': False, 'id': 2},
            {'text': '$100M/kg', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Which of the following components of a space mission’s architecture falls under the ground segment?',
        [
            {'text': 'Mission Control', 'correct': True,
             'id': 0},
            {'text': 'Launch Vehicle', 'correct': False, 'id': 1},
            {'text': 'Payload', 'correct': False, 'id': 2},
            {'text': 'Spacecraft Bus', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Choice of the ______ and ______ drive the design of the spacecraft bus',
        [
            {'text': 'Ground Stations, Orbit', 'correct': False,
             'id': 0},
            {'text': 'Launch Vehicle, Payload', 'correct': False, 'id': 1},
            {'text': 'Communication Requirement, Orbit', 'correct': False, 'id': 2},
            {'text': 'Payload, Orbit', 'correct': True, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_tf_question(
        'The launch segment always consists of a single launch vehicle.',
        False,
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Which of the following is NOT an element of a mission’s ConOps',
        [
            {'text': 'Mission Budget', 'correct': True,
             'id': 0},
            {'text': 'Tasking, Scheduling, Control', 'correct': False, 'id': 1},
            {'text': 'Data Delivery', 'correct': False, 'id': 2},
            {'text': 'Imaging concept', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Which of the following payloads would be present on a communications satellite',
        [
            {'text': 'Antenna', 'correct': True,
             'id': 0},
            {'text': 'Radar', 'correct': False, 'id': 1},
            {'text': 'Spectrometer', 'correct': False, 'id': 2},
            {'text': 'Thermal Imager', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Which of the following types of satellites is more likely to have requirements related to proximity operations?',
        [
            {'text': 'Earth Observation', 'correct': False,
             'id': 0},
            {'text': 'Space Observation', 'correct': True, 'id': 1},
            {'text': 'Navigation', 'correct': False, 'id': 2},
            {'text': 'Communications', 'correct': False, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )
    builder.add_mc_question(
        'Which of the following types of satellites would hold transponders in its payload?',
        [
            {'text': 'Earth Observation', 'correct': False,
             'id': 0},
            {'text': 'Space Observation', 'correct': False, 'id': 1},
            {'text': 'Navigation', 'correct': False, 'id': 2},
            {'text': 'Communications', 'correct': True, 'id': 3}
        ],
        '',
        ['Intro To Space'],
        difficulty=0.25,
        discrimination=10,
        graded=True
    )

    builder.add_exam_finish_slide()


    return builder.get_module()






slide_text = []
slide_text.append("""

""")
slide_text.append("""
Intro to Space Commodities
Module 1: Overview of a Space Mission
Dr. Daniel Selva (Texas A&M University)
Dr. Alejandro Salado (University of Arizona)
""")
slide_text.append("""
Intro to Module 1
In this module, you will get introduced to space missions and the space mission design process. 
The module consists of 4 short lectures:
    Introduction to Space. Why go to space? Why is space expensive? 
    Overview of a Space Mission. Typical elements and concept of operations for a space mission.
    Types of Space Missions and Payloads. Functions of space missions, architectures, payload types
""")
slide_text.append("""
1. Introduction to Space
Why go to space? Why is space expensive?
""")
slide_text.append("""
Why go to space?
Look down – Global perspective
    Weather forecasting
    Surveillance
    Communications and navigation services
Look out – Above the atmosphere
    Astrophysics (look up)
    Atmospheric sounding (look down)
Explore space
    Colonization, expand limits of humanity, or just tourism
    Science: astrobiology, geology, physics, etc.
No gravity – Science
    Microgravity science
    Materials processing
Abundant resources!
    Obtain rare elements and bring them back (gold, platinum)
    In-situ resource utilization
""")
slide_text.append("""
Cost of Earth Observation Satellites
Earth observation mission: $200-$2B
LandSat-8: $857M
Terra: $1.3B
Calipso: $217M
Envisat (ESA): 2.3BEuro
CryoSat (ESA): 
Planetary mission: $1-5B 
Is that a lot? 
To put in perspective: 
US budget: 20 trillion
Joint Strike Fighter: $200B
NASA budget: $20B
Airliner: 50-100$M
Km of road: 1.5$M world average
""")
slide_text.append("""
Space is expensive. Why?
Getting to space (without falling right back) is hard!
Rockets are inefficient
Surviving in space is also hard!
Small markets – unique parts
Labor-intensive
Need for high reliability and “Space Spiral”
Some of this is changing with the recent push for distributed space architectures but still.

Negative Feedback Cycle
    Fewer missions
    Higher reliability
    Longer schedule
    Higher cost
""")
slide_text.append("""
Why is getting to space so hard?
You need a lot of kinetic energy!
Go up at least a few hundreds of km (overcome gravity, atmospheric drag, etc.)
But that is not enough. You also need to accelerate tangentially up to “orbital velocity”, or you would fall back down
Orbital velocity is the velocity at which the centrifugal force pulling the satellite outwards exactly compensates for the gravitational force pulling the satellite inwards 
About 7.5km/s (~16,700mph) + 1-2 km/s more for losses.
Rockets are an inefficient way of getting that energy
A lot of propellant is needed to reach that velocity
Remember Newton’s action-reaction law? the center of mass of the system (rocket + propellant) doesn’t move, so if we want a heavy rocket to go up, a lot of propellant needs to go down
Rockets are about 90% of propellant in weight
Spend most of the energy (propellant) accelerating… the propellant
""")
slide_text.append("""
Example Question
Why is getting into space so difficult?
Answer Choices:
A)Strict regulation of propulsion technology
B)Necessity of a large amount of Kinetic Energy
C)Radiation present in the ozone layer interferes with rockets
D)Companies disrupting the market and raising costs

The correct choice is B. Overcoming the force of Gravity is difficult as well as the need to reach the point of Orbital Velocity.
""")
slide_text.append("""
Cost of access to space
The average launch of a satellite on the order of a few hundreds to a few thousands of kg costs on the order of tens to hundreds of $M
Cost of access to space is about $5k-$20k/kg
Higher end for smaller expendable rockets
Lower end for larger reusable rockets
SpaceX in particular has disrupted this market and is bringing costs down closer to $1k/kg
https://aerospace.csis.org/data/space-launch-to-low-earth-orbit-how-much-does-it-cost/
""")
slide_text.append("""
2. Overview of a Space Mission. 
Typical elements and concept of operations for a space mission.
""")
slide_text.append("""
Elements of a space mission architecture

Space Mission
    Space Segment
        Spacecraft Bus
        Payload
        Orbit
    Launch Segment
        Launch Vehicle
    Ground Segment
        Ground Stations
        Mission Control

Cost distribution between space/launch/ground segment is highly mission-dependent
""")
slide_text.append("""
Space Segment

The space segment consists of one or more spacecraft
Each spacecraft consists of
A payload: the instrument(s) that collect(s) the mission data (e.g., cameras, radars)
A spacecraft bus: the platform that provides power, communications, propulsion, attitude control, and other support to the payload. 

Each spacecraft is put into an orbit, which is the trajectory they follow around a planetary body (e.g., Earth) 

Choice of payload and orbit drive the design of the spacecraft bus and therefore drive space segment cost.
""")
slide_text.append("""
Spacecraft cost drivers

Spacecraft mass is a commonly cited driver for space mission cost
Many cost estimation relationships for space are based on mass
More sophisticated cost models are based on complexity indexes
Combine dozens of complexity factors such as payload and bus mass, power, data rate, lifetime, flight heritage, orbit… 
better predictive power than mass or any other single parameter
""")
slide_text.append("""
Which of the of following is likely to be the best prediction of spacecraft cost?
Answer Choices:
A)Satellite Dry Mass
B)Satellite power at the beginning of life
C)Propellant mass
D)A complexity index accounting for several factors including all of the above

The correct choice is D. Multiple factors have better predictability than one factor alone.
""")
slide_text.append("""
Launch Segment

The launch segment is in charge of putting the spacecraft(s) in their desired orbit(s)
Requires a huge amount of propellant 🡺 large rocket 🡺 so more efficient to separate this from the spacecraft itself
The launch segment consists of one or more launches from the same or different launch vehicles.
Different launch vehicles have different sizes and can carry different amounts of weigh to various orbits
""")
slide_text.append("""
Ground Segment

The ground segment is in charge of operating the spacecraft
Maintaining communications with it (receive data and send commands)
Processing and storing data (telemetry, mission)
Track spacecraft orbital position
Serve as interface between spacecraft and data users
It consists primarily of communications equipment (large antennas, electronics), control centers, and data servers.
""")
slide_text.append("""
Example Question
Choice of the ____ and ____ drive the design of the spacecraft bus
Answer Choices (Select Multiple):
A)Ground Stations
B)Payload
C)Orbit
D)Launch Vehicle

The correct choices are $\mathrm{B}$ and $\mathrm{C}$. The spacecraft bus is an element of the Space segment. Choices $A$ and $D$ belong to the other mission segments.
""")
slide_text.append("""
Mission Concept and ConOps

The mission concept is the highest level description of 
What the mission is
purpose, payload, orbit, number and type of spacecraft (more on this to come)
How the mission is going to work
Often referred to as the Concept of Operations or ConOps.

Elements of a mission ConOps: 
Timeline from launch to reentry
Imaging concept
Tasking, scheduling, control
Communications architecture
Data Delivery
""")
slide_text.append("""
Timeline of an Earth observation mission
Launch (~min to hours): Lift off, first stage separation, upper stage(s), fairing jettisoning, injection. May launch multiple satellites in different orbits.
Orbit insertion (hours to weeks): Detumbling, Deploy antennas and solar panels, perform health tests, transfer to operational orbit
Commissioning (weeks to months): Payload testing and calibration
Nominal operations (~3-10 years): Acquire images, send down to Earth, perform station-keeping maneuvers, software updates. May include nominal orbital changes.
Extended operations (0-10 years): If there is extra funding for ops, extend operations for current or new goals, in same or different orbit.
End of life (deorbiting, hours to weeks): Reentry and burn through Earth’s atmosphere or move intro “graveyard” orbit
""")
slide_text.append("""
Data Delivery

Space vs ground processing
    Instrument raw data is usually in electrical units mV
    Expensive data processing algorithms are done to filter, calibrate, convert to physical units, and bin the data into images.
    Which of those do we do on-board?
Centralized vs distributed processing: All done on one computer or multiple dedicated computers? Decoupling is nice for performance, risk, testing, etc. but may increase cost.
Level of autonomy: from 100% manual to 100% automatic.
All these are inter-related.
""")
slide_text.append("""
Tasking, scheduling, control

Includes 
payload scheduling and control
Spacecraft attitude and orbit control, others
Same trade: Ground vs autonomous?
Typically, attitude control is autonomous but orbit control is from the ground
Payload scheduling is from the ground
""")
slide_text.append("""
3. Types of Space Missions and Payloads.
""")
slide_text.append("""
Types of spacecraft missions and applications

Intent or value added
    Data products vs Technology validation vs Education
Customer context
    Civil vs Military
    Commercial vs Industry vs Government
Type of mission
    Near Earth vs interplanetary
    Robotic vs human
    Remote sensing vs communications vs navigation vs in situ measurements
Focus on this course is on Earth satellites for observation, communication and navigation
""")
slide_text.append("""
Earth Observation

Various purposes
    Weather satellites
    IS&R satellites
    Earth science satellites
Payloads
    Spectral region: optical (visible, infrared) or microwave
    Spectral content: single-band, multi-spectral, hyper-spectral
    Illumination: active (e.g. radars and lidars) or passive (optical imagers)
    Visible imagers offer high resolution (sub-meter) but can’t see during night or through clouds
    Thermal imagers work over night but typically offer reduced spatial resolution (meters to tens of meters)
    Radars have day-night and all weather capability and typically have resolutions of tens-hundreds of meters (synthetic aperture radar)
""")
slide_text.append("""
Space Observation
Similar to Earth observation but used for on-orbit servicing, surveillance, monitoring orbital debris, etc.
Agile satellites capable of proximity operations, with cooperative or uncooperative targets
Payloads are adapted for smaller distances and challenging illumination conditions
""")
slide_text.append("""
Communications

Provide communications services between users on the ground, air, or space.
Different types of services
    Real-time audio
    Real-time video
    Mission data
    Telemetry and Control
Payloads: Antennas and transponders
    RF (L, S, C, X, Ku, K, or Ka bands) or optical
    Single-access (1 user at a time) or multiple-access (multiple users at a time)
    High vs low bandwidth/gain
""")
slide_text.append("""
Navigation

Provide position, navigation, and timing (PNT) services to users on the ground, air and space
Variable accuracy on the order of cm to meters.
Payload is a set of L-band antennas
The most common example is the GPS constellation of ~24 satellites orbiting Earth at around ~20,000km altitude
""")
slide_text.append("""
Example Question
Which of the following types of Satellites would be agile for proximity operations and can face challenging visibility?
Answer Choices (Select Multiple):
A)Earth Observation
B)Navigation
C)Space Observation
D)Communications

The correct choice is C. Space observation satellites may be tasked with imaging other objects within its own orbit or closer to it than the Earth.
""")
slide_text.append("""
Summary
The space missions and their design process can be summarized into the following topics:
Introduction to Space
 There are many motivations for space missions in the realms of exploration and science. There lies a challenge in reaching space with the large amount of kinetic energy required and in consequence the cost of launch.
 Overview of space missions
Space mission are divided into 3 segments: launch, ground, and space. Each segment consists of physical parameters or parts help the segment perform its function.
Space missions and Payloads
The type of spacecraft mission can depend on the intent/goal, customer context, or mission context. From this, an appropriate payload can be chosen. The types of satellites focused on in this module is Earth observation, space observation, communications, and navigation.
""")




#
#
# slide_text.append("""
# Apollo project cost
# Apollo project cost $147B in today’s dollars over 11 years
# 11 crewed missions🡺 $13B/mission
# """)
# slide_text.append("""
# International Space Station cost
# $171 billion over 30 years (1985-2015)
# Including $58B for 36 Shuttle flights to build it
# $28B from international partners
# """)
#
#
# slide_text.append("""
# Example Space Mission WBS and Cost Breakdown
# <image of level 2 cost WBS, no further information>
# """)
#
#
#
# slide_text.append("""
# ConOps for NASA SMAP mission
# """)
# slide_text.append("""
# Communications architecture
# Example ground networks:
#     Near Earth Network (NEN)
#     Space Network/TDRSS
#     Deep Space Network (DSN)
#     Air Force Satellite Control network (AFSCN)
#     Commercial (Amazon, KSAT, …)
# Most NASA LEO missions use the NEN
# Most NASA deep space missions use DSN
# Human Spaceflight (ISS) uses SN-TDRSS, plus a few other LEO missions
#
# Example costs: NEN: 557$ per pass (<30 min per pass); SN: SA: $130/min, MA: $12-21/min
# """)
#
# slide_text.append("""
# Mass of Earth Observation Satellites
# <image depicting mass of different earth observing satellites>
# """)
#
# slide_text.append("""
# 4. Space Mission Design Process.
# Typical phases and milestone of the mission development process.
# """)
# slide_text.append("""
# The Space Mission Life Cycle
#
# Phases
# Key Decision Points
# Technical Reviews
# <image of different phases and key decision points in the space mission life cycle>
# Image: NASA SEH
# """)
# slide_text.append("""
# Pre-Phase A: Concept studies
# Developed continuously and with multiple projects in parallel
# Goals
#     To produce a broad spectrum of ideas and alternatives for missions from which new programs/projects can be selected.
#     Study feasibility of desired system
#     Develop mission concepts
#     Identify potential technology needs.
# Outcomes
#     Mission concepts
#     Draft system-level requirements
# Reviews
#     Mission Concept Review (MCR)
# """)
# slide_text.append("""
# Phase A – Concept and Technology development
# Part of formulation (i.e., before approval)
# Goals
#     To determine the feasibility and desirability of a suggested new major system and establish an initial baseline compatibility with NASA’s strategic plans.
#     Develop final mission concept, system-level requirements, and needed system structure technology developments.
#     Initiate technology developments
# Outcomes
#     Mission Architecture and Conops
#     Top-level Requirements
#     Work Breakdown Structure
#     Systems Engineering Management Plan
#     Technologies
# Reviews
#     Systems Requirements Review (SRR), halfway through
#     Mission/System Definition Review (MDR/SDR)
# """)
# slide_text.append("""
# Why is Phase A important?
#
# Architectural decisions commit most of lifecycle cost and determine ability of the system to deliver value
#     i.e. satisfy stakeholder needs
# Cost of correcting defects is lowest in the architecture phase
# Architectural decisions determine most of system–ilities
#     Flexibility
#     Scalability
#     Robustness
#     …
# Source: INCOSE systems engineering handbook
# """)
# slide_text.append("""
# Phase B – Preliminary Design and Technology Completion
#
# Goals
#     To define the project in enough detail to establish an initial baseline capable of meeting mission needs.
#     Develop system structure end product (and enabling product) requirements
#     And generate a preliminary design for each system structure end product
#     Finalize technology development
# Outcomes
#     Baseline design
#     Interface Control Documents
#     Updated requirements
#     Science/operations plan
#     Technologies
#     Reviews
#     Preliminary Design Review (PDR), for the system and for lower level items as appropriate
# """)
# slide_text.append("""
# Phase C: Final Design and Fabrication
# Goals
#     To complete the detailed design of the system (and its associated subsystems, including its operations systems)
#     Fabricate hardware
#     Code software.
#     Generate final designs for each system structure end product.
#     Plan integration and testing
# Outcomes
#     Finalized designs and components
#     Integration plan and procedures
#     V&V procedures
#     Operations plan
#     Reviews
#     Critical Design Review (CDR), half-way through Phase C
#     System Integration Review (SIR)
# """)
# slide_text.append("""
# Phase D: System Assembly, Integration and Test, Launch
# Goals
#     To assemble and integrate the products to create the system, while developing confidence that it will be able to meet the system requirements.
#     Put the system in launch/flight configuration
#     Launch and prepare for operations.
#     Perform system end product implementation, assembly, integration and test, and transition to use
# Outcomes
#     Integrated and validated system
#     Operational procedures
# Reviews
#     Various test readiness reviews (TRR) at all levels
#     System Acceptance Review (SAR, human only), before shipping to launch site
#     Operational Readiness Review (ORR), system not in launch configuration, weeks to a few months before launch
#     Flight Readiness Review (FRR), system in launch configuration, a few days before launch
# """)
# slide_text.append("""
# Phase E: Operations and sustainment
# Goals
#     To conduct the mission and meet the initially identified need
#     And maintain support for that need.
#     Implement the mission operations plan.
# Outcomes
#     Data Products, sample, …, value! (needs satisfied)
#     Ops and maintenance logs
#     Reviews
#     Post Launch Assessment Review (PLAR), a few hours or days after launch
#     Post Flight Assessment Review (PFAR), human only
#     Critical Event Readiness Review (CERR), right before a critical event (such as a burn changing operational phase in conops)
# """)
# slide_text.append("""
# Phase F: Closeout
# Goals
#     To implement the systems decommissioning/disposal plan developed in Phase E
#     And perform analyses of the returned data and any returned samples
# Outcomes
#     System is disposed or in a safe state
#     Archived data
#     Final mission report
#     Lessons learned
#     Reviews
#     Decommissioning Review (DR)
# """)