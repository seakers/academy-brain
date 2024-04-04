
slide_text = []

slide_text.append("""Slide 1
Intro to Space Commodities
Module 1: Overview of a Space Mission
Dr. Daniel Selva (Texas A&M University)
Dr. Alejandro Salado (University of Arizona)
""")
slide_text.append("""Slide 2
In this module, you will get introduced to space missions and the space mission design process. 
The module consists of 4 short lectures:
    Introduction to Space. Why go to space? Why is space expensive? 
    Overview of a Space Mission. Typical elements and concept of operations for a space mission.
    Types of Space Missions and Payloads. Functions of space missions, architectures, payload types
    Space Mission Design Process. Phases of the mission development process.
""")
slide_text.append("""Slide 3
1. Introduction to Space
Why go to space? Why is space expensive?
""")
slide_text.append("""Slide 4
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
slide_text.append("""Slide 5
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
slide_text.append("""Slide 6
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
slide_text.append("""Slide 7
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
slide_text.append("""Slide 8
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
slide_text.append("""Slide 9
Example Question
Why is getting into space so difficult?
Answer Choices:
A)Strict regulation of propulsion technology
B)Necessity of a large amount of Kinetic Energy
C)Radiation present in the ozone layer interferes with rockets
D)Companies disrupting the market and raising costs

The correct choice is B. Overcoming the force of Gravity is difficult as well as the need to reach the point of Orbital Velocity.

""")
slide_text.append("""Slide 10
Cost of access to space
The average launch of a satellite on the order of a few hundreds to a few thousands of kg costs on the order of tens to hundreds of $M
Cost of access to space is about $5k-$20k/kg
Higher end for smaller expendable rockets
Lower end for larger reusable rockets
SpaceX in particular has disrupted this market and is bringing costs down closer to $1k/kg
https://aerospace.csis.org/data/space-launch-to-low-earth-orbit-how-much-does-it-cost/
""")
slide_text.append("""Slide 11
2. Overview of a Space Mission. 
Typical elements and concept of operations for a space mission.
""")
slide_text.append("""Slide 12
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
slide_text.append("""Slide 13
Example Space Mission WBS and Cost Breakdown
<image of level 2 cost WBS, no further information>
""")
slide_text.append("""Slide 14
Space Segment

The space segment consists of one or more spacecraft
Each spacecraft consists of
A payload: the instrument(s) that collect(s) the mission data (e.g., cameras, radars)
A spacecraft bus: the platform that provides power, communications, propulsion, attitude control, and other support to the payload. 

Each spacecraft is put into an orbit, which is the trajectory they follow around a planetary body (e.g., Earth) 

Choice of payload and orbit drive the design of the spacecraft bus and therefore drive space segment cost.
""")
slide_text.append("""Slide 15
Spacecraft cost drivers

Spacecraft mass is a commonly cited driver for space mission cost
Many cost estimation relationships for space are based on mass
More sophisticated cost models are based on complexity indexes
Combine dozens of complexity factors such as payload and bus mass, power, data rate, lifetime, flight heritage, orbit… 
better predictive power than mass or any other single parameter
""")
slide_text.append("""Slide 16
Which of the of following is likely to be the best prediction of spacecraft cost?
Answer Choices:
A)Satellite Dry Mass
B)Satellite power at the beginning of life
C)Propellant mass
D)A complexity index accounting for several factors including all of the above

The correct choice is D. Multiple factors have better predictability than one factor alone.
""")
slide_text.append("""Slide 17
Launch Segment

The launch segment is in charge of putting the spacecraft(s) in their desired orbit(s)
Requires a huge amount of propellant 🡺 large rocket 🡺 so more efficient to separate this from the spacecraft itself
The launch segment consists of one or more launches from the same or different launch vehicles.
Different launch vehicles have different sizes and can carry different amounts of weigh to various orbits
""")
slide_text.append("""Slide 18
Ground Segment

The ground segment is in charge of operating the spacecraft
Maintaining communications with it (receive data and send commands)
Processing and storing data (telemetry, mission)
Track spacecraft orbital position
Serve as interface between spacecraft and data users
It consists primarily of communications equipment (large antennas, electronics), control centers, and data servers.
""")
slide_text.append("""Slide 19
Example Question
Choice of the ____ and ____ drive the design of the spacecraft bus
Answer Choices (Select Multiple):
A)Ground Stations
B)Payload
C)Orbit
D)Launch Vehicle

The correct choices are $\mathrm{B}$ and $\mathrm{C}$. The spacecraft bus is an element of the Space segment. Choices $A$ and $D$ belong to the other mission segments.
""")
slide_text.append("""Slide 20
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
slide_text.append("""Slide 21
Timeline of an Earth observation mission
Launch (~min to hours): Lift off, first stage separation, upper stage(s), fairing jettisoning, injection. May launch multiple satellites in different orbits.
Orbit insertion (hours to weeks): Detumbling, Deploy antennas and solar panels, perform health tests, transfer to operational orbit
Commissioning (weeks to months): Payload testing and calibration
Nominal operations (~3-10 years): Acquire images, send down to Earth, perform station-keeping maneuvers, software updates. May include nominal orbital changes.
Extended operations (0-10 years): If there is extra funding for ops, extend operations for current or new goals, in same or different orbit.
End of life (deorbiting, hours to weeks): Reentry and burn through Earth’s atmosphere or move intro “graveyard” orbit
""")
slide_text.append("""Slide 22
Data Delivery

Space vs ground processing
    Instrument raw data is usually in electrical units mV
    Expensive data processing algorithms are done to filter, calibrate, convert to physical units, and bin the data into images.
    Which of those do we do on-board?
Centralized vs distributed processing: All done on one computer or multiple dedicated computers? Decoupling is nice for performance, risk, testing, etc. but may increase cost.
Level of autonomy: from 100% manual to 100% automatic.
All these are inter-related.

""")
slide_text.append("""Slide 23
Tasking, scheduling, control

Includes 
payload scheduling and control
Spacecraft attitude and orbit control, others
Same trade: Ground vs autonomous?
Typically, attitude control is autonomous but orbit control is from the ground
Payload scheduling is from the ground
""")
slide_text.append("""Slide 24
3. Types of Space Missions and Payloads.
""")
slide_text.append("""Slide 25
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
slide_text.append("""Slide 26
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
slide_text.append("""Slide 27
Space Observation
Similar to Earth observation but used for on-orbit servicing, surveillance, monitoring orbital debris, etc.
Agile satellites capable of proximity operations, with cooperative or uncooperative targets
Payloads are adapted for smaller distances and challenging illumination conditions
""")
slide_text.append("""Slide 28
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
slide_text.append("""Slide 29
Navigation

Provide position, navigation, and timing (PNT) services to users on the ground, air and space
Variable accuracy on the order of cm to meters.
Payload is a set of L-band antennas
The most common example is the GPS constellation of ~24 satellites orbiting Earth at around ~20,000km altitude
""")
slide_text.append("""Slide 30
Example Question
Which of the following types of Satellites would be agile for proximity operations and can face challenging visibility?
Answer Choices (Select Multiple):
A)Earth Observation
B)Navigation
C)Space Observation
D)Communications

The correct choice is C. Space observation satellites may be tasked with imaging other objects within its own orbit or closer to it than the Earth.
""")
slide_text.append("""Slide 31
Summary
The space missions and their design process can be summarized into the following topics:
Introduction to Space
 There are many motivations for space missions in the realms of exploration and science. There lies a challenge in reaching space with the large amount of kinetic energy required and in consequence the cost of launch.
 Overview of space missions
Space mission are divided into 3 segments: launch, ground, and space. Each segment consists of physical parameters or parts help the segment perform its function.
Space missions and Payloads
The type of spacecraft mission can depend on the intent/goal, customer context, or mission context. From this, an appropriate payload can be chosen. The types of satellites focused on in this module is Earth observation, space observation, communications, and navigation.
""")