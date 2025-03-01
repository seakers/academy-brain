slide_text = []


slide_text.append("""Slide 1
Intro to Space Commodities
Module 2: Space Environment and Orbits
Dr. Daniel Selva (Texas A&M University)
Dr. Alejandro Salado (University of Arizona)
""")
slide_text.append("""Slide 2
Intro to Module 2
In this module, you will get introduced to space missions and the space mission design process. 
The module consists of 4 short lectures:
    Space environment. What makes space a harsh environment? How does it affect humans and spacecraft?
    Introduction to orbits. What is an orbit and why is it important? 
    Types of orbits. What types of orbits are there? How does orbit selection affect spacecraft design? 
    Orbital maneuvers. How do different types of maneuvers work in space? Implications on spacecraft design.
""")
slide_text.append("""Slide 3
1. Space Environment
""")
slide_text.append("""Slide 4
Key space environment factors affecting spacecraft (and humans!)
    Microgravity
    Vacuum
    Radiation
    Atmospheric Drag
    Atomic oxygen
    Extreme Temperatures
    Space Debris
""")
slide_text.append("""Slide 5
“Microgravity”
Objects are in “free fall”, not absence of gravity!
    Gravity compensated by centrifugal force due to orbital speed 
Near absence of gravity (~10-6 g) means that:
    Objects don’t fall
    Bubbles don’t rise
    Particles don’t settle in a solution
    No convection (eliminates an important heat transfer mechanism!)
This presents challenges, mostly for astronauts…
    Bone loss
    Muscle loss
    Cardiovascular problems
    Immune system
…but also opportunities
    Formation of large crystals
The effects on traditional Earth satellites are relatively benign (e.g., lower structural stresses when in orbit)
""")
slide_text.append("""Slide 6
Atmosphere layers
Troposphere (0-10km)
    Where we are (weather, pollution)
Stratosphere (10-50km)
    Where airplanes and balloons are
    Stratospheric chemistry
    Ozone layer absorbs UV
Mesosphere (50-80km)
    Where suborbital flights go
Thermosphere (80-400km)
    Where very low earth satellites are
    Atomic oxygen absorbs radiation
    Ions
Exosphere (>400km)
    Where most satellites are
""")
slide_text.append("""Slide 7
Atmospheric drag – Orbit/attitude disturbance
We care about atmospheric density mostly because it affects the drag (D) seen by the satellite, which may lead to orbital decay and disturbance torques:
D = (1/2)*p*V^2*C_d*A
p  is the atmospheric density (varies exponentially but very small in orbit)
C_d is the drag coefficient (2-4 are typical values for spacecraft)
V is the orbital velocity
Atmospheric drag is strong up to 500km, negligible after that
    A CubeSat at 400km has 1-9 month lifespan, and 600km one has over 25 years lifespan
""")
slide_text.append("""Slide 8
Atomic Oxygen – Erosion
In the upper layers of the atmosphere the predominant constituent is atomic oxygen (O), formed by photodissociation of O2
 - O_2 + light = O + O
Highly reactive and energetic
It erodes satellite surfaces (teflon, epoxies, Mylar)
Surfaces can be protected by coating them with something that is "immune" to O:
 - silicon dioxide
 - aluminum
Source: http://esmat.esa.int/Atox_on_metals.PDF
""")
slide_text.append("""Slide 9
Vacuum – Outgassing
Outgassing is the release of gas that was trapped in some material
 - adhesives, insulators, thermal coating, electrical shields
Vacuum facilitates outgassing due to decreased sublimation and evaporation points. 
Outgassed material tends to condense onto cooler surfaces. 
 - Optical elements, radiators, solar cells
Reaction with UV radiation results in dark stains that may affect performance of instruments or solar panels.
Some materials outgas more than others in vacuum (e.g., Cd, Zn, Mg, paints, etc.)
Spacecraft manufacturers have lists of low outgassing materials
""")
slide_text.append("""Slide 10
Earth’s magnetic field
The Earth has a magnetic field
 - Protects us from radiation
 - Generates forces that rotate spacecraft (can be leveraged using magnetic torquers)
Magnetic field lines points from magnetic south to north
 - Different from geographic equator and poles
Intensity decreases with distance as 1/r^3
Max at the magnetic equator, min at the magnetic poles
""")
slide_text.append("""Slide 11
Earth’s magnetosphere
Magnetosphere is the region around Earth in which ions are controlled by the Earth’s magnetic field
It protects us from solar and other radiation up to certain levels of energy
""")
slide_text.append("""Slide 12
Electromagnetic radiation
Electromagnetic radiation is carried by waves and massless particles (named photons) that travel at the speed of light
Waves are periodic:
 - Wavelength is the distance between consecutive peaks
 - Frequence is the time interval between consecutive peaks
Frequency 'f' and wavelength 'lambda' are related to the speed of light 'c'
 - f = c / lambda
Energy of a photon is proportional to its frequency through the Planck constant h
 - E = h*f = (h*c) / lambda
""")
slide_text.append("""Slide 13
Solar Radiation – Light, matter, and fields
Explosions in the Sun's atmosphere produce both: light (photons), and matter (charged particles such as ions and electrons)
This becomes radiation from the Sun
Solar flares are huge bursts of photons in all wavelengths, but mostly x-rays and extreme UV (EUV): E ~ 10^25 J
Coronal Mass Ejections (CME) are made of particles (ions and electrons) ejected at very high speeds (solar wind)
 - from 0.2-3 CME/day
 - ~500km/s (~3days to reach earth)
 - ~10 protons/cm^3
""")
slide_text.append("""Slide 14
Solar Radiation – Geomagnetic storms
Geomagnetic storms are temporary disturbances in the Earth magnetosphere due to interaction with solar radiation
They create: Solar energetic particle events, Geomagnetically induced currents, Ionospheric disturbances, Auroras
This creates multiple problems for spacecraft and astronauts
 - Drag
 - Spacecraft charging
 - Radiation poisoning
And even affect Earth’s infrastructure such as power grids! 
""")
slide_text.append("""Slide 15
Solar cycle
Average total solar irradiance (energy per unit time and area) is about 1366 W/m^2
However, there are periodic variations on the order of +- 0.5W/m^2
These fluctuations have a period of ~11 years (solar cycle)
Can be observed through variations in solar spots
Thus, timing of launch within solar cycle affects atmospheric drag and amount of radiation
""")
slide_text.append("""Slide 16
Galactic Cosmic Rays
Galactic Cosmic Rays (GCR) are radiation from outside the solar system
 - from supernovae, black holes, etc
Much more energtic than solar radiation (GeV-PeV, where 1eV = 1.6*10^(-19); G, T, P = 10^9, 10^12, 10^15 respectively)
 - Protons or heavier ions travelling at relativistic speeds
Larger threat, especially for interplanetary missions
GCR is max at solar cycle minumum
Create Single Event Phenomena (SEP): Single particle can destroy an electronic component.
""")
slide_text.append("""Slide 17
Van Allen Radiation Belts
The Van Allen Belts are 2 regions of trapped fast charged particles (electrons and protons)
 - Inner belt: 1,000-6,000km altitude
 - Outer belt: 13,000-60,000km
Most LEO satellites are below the 1st ring (inner belt) so they have a more benign radiation environment
MEO satellites are in the middle of the 2nd ring (outer belt) so they see more radiation (e.g., GPS satellites)
GEO satellites are in the edge of the outer belt (radiation also a problem)
The South Atlantic Anomaly is a range of longitudes where the Earth’s magnetic field is weaker and thus radiation is worse. Leads to more radiation-related spacecraft failures.
""")
slide_text.append("""Slide 18
Spacecraft charging
As a result of charged particles looming around in space, a positive or negative charge can accumulate in a spacecraft’s surface
 - Like when you walk on carpet
This can lead to very damaging electrostatic discharges
 - when you touch the doorknob
Spacecraft have to be carefully designed to mitigate this risk
""")
slide_text.append("""Slide 19
Radiation and shielding
In summary, the total dose of radiation comes from:
 - Sunlight (mostly UV photons)
 - Solar flares (EUV and X-rays)
 - Solar wind (low energy protons)
 - CME (medium-high energy protons)
 - Radiation belt (protons and electrons)
 - Galactic Cosmic Rays (relativistic heavy nuclei)
Spacecraft must shield against this radiation
 - Ex: Thick layer of aluminum, or water for human spaceflight.
The more total radiation dose expected during the mission’s lifetime, the thicker the layer of aluminum must be.
""")
slide_text.append("""Slide 20
Orbital debris and meteoroids
Any non-operational object in orbit is considered debris
Includes mission-related debris, such as
 - Pieces of dead satellites
 - Pieces of launch vehicles (fairings, inter-stage adapters)
 - Others (e.g., Ed White’s glove from Gemini 4 mission)
And naturally occurring debris
 - Micrometeoroids
 - Asteroid particles
Mostly concentrated around most populated orbits (e.g., GPS and GEO orbits)
""")
slide_text.append("""Slide 21
Orbital debris and meteoroids
Can cause collisions that destroy [parts of] spacecraft
All objects above 10cm are visible from Earth and are currently being monitored and carefully catalogued
""")
slide_text.append("""Slide 22
Spacecraft Thermal Environment
Spacecraft receive heat from 
 - the Sun (direct and reflected off Earth), 
 - the Earth,
 - internal sources (e.g., electronics)
Variations in these contributions along a spacecraft’s orbit can result in fast and extreme temperature changes
 - When a spacecraft has large surface areas directly exposed to the Sun, it can get pretty hot
 - When a spacecraft is behind Earth (there is no sunlight), we say it is in eclipse – it gets cold pretty quickly
To manage this heat, spacecraft rely primarily on radiation
 - No convection in space (e.g., heat doesn’t rise)
To control radiation, spacecraft often use coatings such as paints and thermal insulators with radiative properties specially designed for the mission
 - More on this in the spacecraft subsystems module!
""")
slide_text.append("""Slide 23
2. Introduction to orbits
""")
slide_text.append("""Slide 24
What are orbits?
Orbits are the trajectories that spacecraft “naturally” follow around the Earth due to gravitational forces
Any two objects under each other’s gravitational force will “orbit each other”
 - This is called the 2-body problem
When one is much larger than the other (e.g., a satellite vs Earth, or the Earth vs the Sun) the motion of the large object is largely unaffected and it all happens as if the small object rotates around the large object
""")
slide_text.append("""Slide 25
Shape of orbits
Satellite orbits are generally ellipses
The earth (or central body) sits in one of the focus points
An ellipse is usually defined by 2 parameters:
 - the semimajor-axis a is half the length of the longer axis (increasing 'a' makes the orbit "bigger", further from earth)
 - Eccentricity e tells us how elongated the ellipse is (when e = 0 the orbit is circular)
Together, a and e define the shape of the orbit
""")
slide_text.append("""Slide 26
Conic sections, open vs closed orbits
More generally, orbital trajectories can follow the shape of any conic section (circle, ellipse, parabola, or hyperbola)
Circular and elliptical orbits (0 <= eccentricity < 1) are "closed orbits" around earth
A satellite with sufficient energy (eccentricity >= 1) will escape earth and follow an interplanetary trajectory that never comes back (i.e. open orbits)
 - when eccentricity = 1, it follows a parabolic trajectory
 - when eccentricity > 1 it follows a hyperbolic trajectory
Hyperbola: 
""")
slide_text.append("""Slide 27
Position of a satellite within its orbit
The true anomaly 'theta' is an angle that defines where within the orbit the satellite is at a given point in time.
There are two special points:
 - the perigee is the point where it is closest to the earth
 - the apogee is the point where it is farthest from earth
Given semi-major axis (a), eccentricity (e), and theta, we can compute the satellite position r, i.e. the distance betwseen the satellite and earth
 - r(theta) = (a*(1-e^2))/(1+e*cos(theta)) 
""")
slide_text.append("""Slide 28
Orientation of the orbit and orbital plane
The orbit lies on a plane called the orbital plane that intersects the Earth's equatorial plane (i.e. at 0 degrees latitude) at two points called the nodes:
 - Ascending node: where the satellite is going north
 - Descending node: where it is going south
The orientation of the orbit (the ellipse) within the orbital plane is defined by an angle called the argument of perigee
 - Angle from the ascending node to the perigee from the earth center, 'w'
The orientation of the orbital plane with respect to the Earth is defined by two angles:
 - the inclination 'i' is the tilt angle between the orbital plane and the equatorial plane
 - the right ascension of the ascending node (called RAAN) 'omega' is the twist angle of the orbital plane, from the vernal equinox (a fixed direction in space) to the ascending node.
""")
slide_text.append("""Slide 29
Orbital parameters, period
Together, the 6 orbital parameters semi-major axis (a), eccentricity (e), inclination (i), argument of perigee (w), right ascension of the ascending node (omega), and true anomaly (theta) fully define the trajectory of the satellite
 - from these 6 parameters, we can calculate anything: the satellite position, velocity, etc.
For example, from kepler's laws, we can calculate the orbital period (T), aka the time it takes the satellite to go around its orbit once:
 - T = (1/2*pi) * sqrt(a^3 / G*M)
Where G = 6.67*10^(-11) (Newton * meter^2 / kilogram^2) is the gravitational constant and M = 5.97*10^24 kg is the mass of earth
Note that it only depends on the semi-major axis!
""")
slide_text.append("""Slide 30
Orbital velocity
Similarly, using the vis-viva equation (conservation of energy), we can compute the velocity of the satellite:
 - V = sqrt(G*M*(2/r - 1/a)) where r is distance from earth and a is semi-major axis
For a general elliptical orbit, we see that as predicted by Kepler's laws, the satellite will move faster the closer it gets to Earth, and will slow down as it gets farther from Earth
For a circular orbit, r = a = R_e + h, where R_e = 6370km is the radius of earth and h is the orbit altitude. In this case, the velocity is constant:
 - V = sqrt(G*M*(1/(R_e + h)))
""")
slide_text.append("""Slide 31
Example: What is the orbital period and velocity of a satellite in a circular orbit around Earth at 600km altitude?
The orbital period is:
 - T = (1/2pi) * sqrt(a^3/(G*M)) = 96.7min
The orbital velocity is:
 - V = sqrt((G*M)/(R_e + h)) = 7.56km/s
In general, satellites in low Earth orbits (400-800km altitudes) have periods of ~92-100 minutes and velocities of ~7.4-7.7 km/s
Period increases with altitude whereas velocity decreases with it
The special altitude that leads to a period of 24h is about 36,000km, this is called a geosynchronous orbit
""")
slide_text.append("""Slide 32
Orbit perturbations – Effect of J2
In the absence of any peturbations, the orbital parameters a, e, i, w, omega would stay constant over time
 - The orientation of the orbital plane would stay fixed, independent of the motion of earth
In reality, the plane rotates over time primarily because the earth is not a perfect sphere.
 - This is nodal precession, a change in RAAN over time
 - The earth's shape is modeled using spherical harmonics with many coefficients terms
 - The largest coefficient is the ablateness of the earth, which is captured by the so-called J_2 parameter
Rate of nodal precession is different for different orbits:
 - precission_rate = -3/(2(1-e^2)^2) * n * J_2 * (R_e/a)^2 * cos(i), where n= 2pi / T
J2 also causes the argument of the perigee to rotate within the orbital plane, which is called apsidal precession
""")
slide_text.append("""Slide 33
Orbit perturbations
Another major orbit perturbation for very low Earth orbits is atmospheric drag which creates orbital decay below 600km
There are several other sources of orbit perturbations:
 - 3rd body effects (Moon and Sun) Solar radiation pressure
 - Other harmonics (J4, J6), other planets, albedo, tidal effects, ...
Magnitude of each depends strongly on altitude, but J2 is often strongest
Example: 
 - For a satellite at 300km, drag is as strong as J2 (really dominates)
 - At 800km, J2 dominates
 - At 36,000km, the Sun/Moon effects are as strong as J2
Because of all these perturbations, spacecraft use propellant to keep their orbit parameters constant 
 - This is called station-keeping
""")
slide_text.append("""Slide 34
Ground tracks
The ground track is the projection of the position of satellite on the Earth’s surface (lat,lon) over time
 - They are a useful visualization of an orbit since they show which regions are “seen”
Can infer orbital parameters from ground tracks
 - Inclination from max latitude
 - Period (and thus semimajor axis) from equatorial orbit shift between consecutive tracks
""")