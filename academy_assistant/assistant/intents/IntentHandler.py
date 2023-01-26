import datetime
import json
from django.conf import settings

from academy_assistant.assistant.intents.ParameterExtractor import ParameterExtractor

from academy_assistant.database.client.GraphqlClient import GraphqlClient


class IntentHandler:


    def __init__(self, user_info, command, intent):
        self.app_path = settings.ACADEMY_PATH
        self.user_info = user_info
        self.command = command
        self.command_processed = settings.NLP_MODEL(self.command.strip())
        self.intent = intent
        self.extractor = ParameterExtractor(self.user_info, self.command_processed)



    def process(self):
        intent_func = 'intent_' + str(self.intent)
        if hasattr(self, intent_func):
            print('--> PROCESSING INTENT FUNCTION:', intent_func)
            func = getattr(self, intent_func)
            return func()
        else:
            raise Exception("Intent function DNE:", intent_func)

    ########################
    ### Intent Functions ###
    ########################
    # ["Analyst", "Engineer", "Critic", "Historian", "Teacher"]
    # Every one needs to be re-written for Cost Estimator Tutoring
    def insert_msg(self, message, type, writer, more_info=None):
        print('!!! Message insertion moved to end of view called by user message !!!')

    def intent_1000(self):
        return {'text': 'Satellite booms are extensible mechanisms made to deploy other mechanisms such as antennas or solar panels'}
    def intent_1001(self):
        return {'text': 'Satellite gimbals are used to point some component in a desired direction'}
    def intent_1002(self):
        return {'text': 'A low Earth orbit (LEO) is an orbit that is relatively close to Earth’s surface (<1000km but could be as low as 160km)'}
    def intent_1003(self):
        return {'text': 'A geostationary orbit (GEO) is a circular geosynchronous orbit 35,786km in altitude above earth\'s equator. An object in such an orbit has an orbital period equal to Earth\'s rotational period, and so to ground observers it appears fixed in the sky'}
    def intent_1004(self):
        return {'text': "A geosynchronous orbit (GSO) is an Earth-centered orbit with an orbital period that matches Earth's rotation on its axis. An object in geosynchronous orbit returns to exactly the same position in the sky after a period of one sidereal day"}
    def intent_1005(self):
        return {'text': 'The sidereal day is the time required for the Earth to rotate once relative to the background of the stars'}
    def intent_1006(self):
        return {'text': "A satellite is in eclipse when its orbiting body comes between the spacecraft and the sun"}
    def intent_1007(self):
        return {'text': "A battery cycle refers to one full drain of the battery's charge"}
    def intent_1008(self):
        return {'text': "In the context of batteries, specific energy is a measure of how much energy a battery contains in comparison to its weight (W-hr/kg)"}
    def intent_1009(self):
        return {'text': "EMI Shielding in electronic devices and equipment is done to protect signals from being disrupted by external electromagnetic signals."}
    def intent_1010(self):
        return {'text': "Spin stabilization is a attitude control method where the spacecraft spins on some axis to stabilize itself with respect to that axis"}
    def intent_1011(self):
        return {'text': 'Three-axis stabilization is an attitude control method that allows for stabilization with respect to all three axes'}
    def intent_1012(self):
        return {'text':  "An inertial reference unit (IRU) is a type of inertial sensor that determines a moving spacecraft's change in rotational attitude and translational position."}
    def intent_1013(self):
        return {'text': "Reaction wheels are used to control the attitude of a satellite without the use of thrusters. They work by equipping the spacecraft with an electric motor attached to a flywheel, which, when its rotation speed is changed, causes the spacecraft to begin to counter-rotate proportionately through conservation of angular momentum."}
    def intent_1014(self):
        return {'text': "A control moment gyroscope (CMG) is an attitude control device generally used in spacecraft attitude control systems. CMGs consist of a spinning rotor and one or more motorized gimbals that tilt the rotor’s angular momentum."}
    def intent_1015(self):
        return {'text': "A magnetorquer (also known as a torque rod) is a satellite system for attitude control. Magnetorquers create a magnetic dipole that interfaces with an ambient magnetic field, usually Earth's, so that the counter-forces produced provide useful torque. "}
    def intent_1016(self):
        return {'text': "A charge-coupled device (CCD) is an integrated circuit containing an array of linked, or coupled, capacitors."}
    def intent_1017(self):
        return {'text': "The nadir is the direction pointing directly below a particular location. For an earth orbiting spacecraft, nadir points directly at earth's center"}
    def intent_1018(self):
        return {'text': "Momentum dumping is when some force (such as a thruster) is applied to counteract a change in momentum caused by removing momentum from some attitude control mechanism."}
    def intent_1019(self):
        return {'text': "Orbital station keeping the correction of a satellites trajectory to maintain a desired one (ex. maintaining a specific orbital altitude)."}
    def intent_1020(self):
        return {'text':  "Cross strapping is a method of adding redundancy to a system through interconnected identical units where either unit can provide the required functionality."}

    def intent_2000(self):
        return {'text': "Delta-V is the total change in spacecraft velocity over a mission lifecycle"}
    def intent_2001(self):
        return {'text': "Eccentricity is the deviation of an orbit from circularity"}
    def intent_2002(self):
        return {'text': "Orbital inclination measures the tilt of a spacecraft\'s orbit around a celestial body. It is expressed as the angle between a reference plane and the orbital plane or axis of direction of the orbiting object."}
    def intent_2003(self):
        return {'text': "The three main approaches to cost estimation are the following: top-down, bottom-up, and anaology."}
    def intent_2004(self):
        return {'text': "There are four main remote sensor systems types: visible systems, infrared systems, radar systems, and microwave radiometers"}
    def intent_2005(self):
        return {'text': "In the EM spectrum, radar systems operate in the centimeter to millimeter bands."}
    def intent_2006(self):
        return {'text': "The earth's atmosphere impacts the propagation of RF signals due to the signal interacting with gaseous constituents of the atmosphere, aerosols, or hydrometeors."}
    def intent_2007(self):
        return {'text': "EO/IR payloads collect data between the ultra-violate and infrared wavelengths."}
    def intent_2008(self):
        return {'text': "Aperture refers to the instrument's lens diameter"}
    def intent_2009(self):
        return {'text': "NIIRS refers to the National Image Interpretability Rating Scales. It defines the quality of an image and the performance of imaging systems."}
    def intent_2010(self):
        return {'text': "Field of view (FOV) is an angular measure of the width a sensor can see."}
    def intent_2011(self):
        return {'text': "Instrument focal length is the distance from the lens to the detectors."}
    def intent_2012(self):
        return {'text': "Instantaneous field of view (IFOV) is the angular width a single pixel detector can see in an instrument."}
    def intent_2013(self):
        return {'text': "Field of view (FOV) is an angular measure of the width a sensor can see. Instantaneous field of view (IFOV) is the angular width a single pixel detector can see."}
    def intent_2014(self):
        return {'text': "The two types of EO/IR payloads are scanners and starers. Scanners use a linear array of detectors, while starers use a rectangular array."}
    def intent_2015(self):
        return {'text': "At a high level, EO/IR payloads consist of a focal plane array (FPA) and readout integrated circuits (ROIC)"}
    def intent_2016(self):
        return {'text': "Passive thermal control systems dispel heat passively through the natural infrared radiation"}

    def intent_3000(self):
        return {'text': "Focal plane arrays are arrays of light detectors placed in the focal plane of an imaging system."}

    def intent_4000(self):
        return {'text': "Lifecycle cost is the total mission cost from planning through end-of-life"}
    def intent_4001(self):
        return {'text': "The three phases of lifecycle cost are: 1) Research, Development, Test, and Evaluation, 2) Production, and 3) Operations and Maintenance."}
    def intent_4002(self):
        return {'text': "Qualification units are used in qualification testing to verify the design and requirements."}
    def intent_4003(self):
        return {'text': "Brassboards are experimental or demonstration test models following an earlier prototyping stage called breadboards."}
    def intent_4004(self):
        return {'text': "Theoretical first units represent the first flight-qualified satellite off the production line."}
    def intent_4005(self):
        return {'text': "The learning curve is a factor multiplied by the theoretical first unit cost to determine the production cost of subsequent satellites."}
    def intent_4006(self):
        return {'text': "Space mission final operating capability represents the full compliment of on-orbit satellites."}
    def intent_4007(self):
        return {'text': "A satellite constellation is a group of satellites working together as a system."}
    def intent_4008(self):
        return {'text': "A satellite\'s orbit has implications on many factors such as delta-v budget (low altitude orbits need more station-keeping maneuvers), optical payload (spacial resolution), and revisit time for example."}
    def intent_4009(self):
        return {'text': "Satellite slewing agility determines the satellite\'s ability to change its attitude."}


















