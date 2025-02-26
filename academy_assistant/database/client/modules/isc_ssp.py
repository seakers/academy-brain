from academy_assistant.database.client.modules.AbstractBuilder import AbstractBuilder
slide_text = ['']
import os
# slide_text_dir = os.path.join('/Users/mahima/Documents/daphne-academy/academy-brain/academy_assistant/database/client/modules/slide_text', 'ssp')
base_dir = os.path.dirname(os.path.abspath(__file__))
slide_text_dir = os.path.join(base_dir, 'slide_text', 'ssp')
# Iterate over all txt files in slide_text_dir
for file in os.listdir(slide_text_dir):
    if file.endswith('.txt'):
        with open(os.path.join(slide_text_dir, file), 'r') as f:
            slide_text.append(f.read())

def get_module():
    builder = AbstractBuilder('mdi-telescope', ['Optical payloads', 'Microwave payloads'], 'Intro to Space Commodities', None)

    # From slide 1 to 95
    builder.add_slide('ISC_SSP_1', slide_text[1], "https://academy2.selva-research.com/images/ssp/Slide1.png")
    builder.add_slide('ISC_SSP_2', slide_text[2], "https://academy2.selva-research.com/images/ssp/Slide2.png")
    builder.add_slide('ISC_SSP_3', slide_text[3], "https://academy2.selva-research.com/images/ssp/Slide3.png")
    builder.add_slide('ISC_SSP_4', slide_text[4], "https://academy2.selva-research.com/images/ssp/Slide4.png")
    builder.add_slide('ISC_SSP_5', slide_text[5], "https://academy2.selva-research.com/images/ssp/Slide5.png")
    builder.add_slide('ISC_SSP_6', slide_text[6], "https://academy2.selva-research.com/images/ssp/Slide6.png")
    builder.add_slide('ISC_SSP_7', slide_text[7], "https://academy2.selva-research.com/images/ssp/Slide7.png")
    builder.add_slide('ISC_SSP_8', slide_text[8], "https://academy2.selva-research.com/images/ssp/Slide8.png")
    builder.add_slide('ISC_SSP_9', slide_text[9], "https://academy2.selva-research.com/images/ssp/Slide9.png")
    builder.add_slide('ISC_SSP_10', slide_text[10], "https://academy2.selva-research.com/images/ssp/Slide10.png")
    builder.add_slide('ISC_SSP_11', slide_text[11], "https://academy2.selva-research.com/images/ssp/Slide11.png")
    builder.add_slide('ISC_SSP_12', slide_text[12], "https://academy2.selva-research.com/images/ssp/Slide12.png")
    builder.add_slide('ISC_SSP_13', slide_text[13], "https://academy2.selva-research.com/images/ssp/Slide13.png")
    builder.add_slide('ISC_SSP_14', slide_text[14], "https://academy2.selva-research.com/images/ssp/Slide14.png")
    builder.add_slide('ISC_SSP_15', slide_text[15], "https://academy2.selva-research.com/images/ssp/Slide15.png")
    builder.add_slide('ISC_SSP_16', slide_text[16], "https://academy2.selva-research.com/images/ssp/Slide16.png")
    builder.add_slide('ISC_SSP_17', slide_text[17], "https://academy2.selva-research.com/images/ssp/Slide17.png")
    builder.add_slide('ISC_SSP_18', slide_text[18], "https://academy2.selva-research.com/images/ssp/Slide18.png")
    builder.add_slide('ISC_SSP_19', slide_text[19], "https://academy2.selva-research.com/images/ssp/Slide19.png")
    builder.add_slide('ISC_SSP_20', slide_text[20], "https://academy2.selva-research.com/images/ssp/Slide20.png")
    builder.add_slide('ISC_SSP_21', slide_text[21], "https://academy2.selva-research.com/images/ssp/Slide21.png")
    builder.add_slide('ISC_SSP_22', slide_text[22], "https://academy2.selva-research.com/images/ssp/Slide22.png")
    builder.add_slide('ISC_SSP_23', slide_text[23], "https://academy2.selva-research.com/images/ssp/Slide23.png")
    builder.add_slide('ISC_SSP_24', slide_text[24], "https://academy2.selva-research.com/images/ssp/Slide24.png")
    builder.add_slide('ISC_SSP_25', slide_text[25], "https://academy2.selva-research.com/images/ssp/Slide25.png")
    builder.add_slide('ISC_SSP_26', slide_text[26], "https://academy2.selva-research.com/images/ssp/Slide26.png")
    builder.add_slide('ISC_SSP_27', slide_text[27], "https://academy2.selva-research.com/images/ssp/Slide27.png")
    builder.add_slide('ISC_SSP_28', slide_text[28], "https://academy2.selva-research.com/images/ssp/Slide28.png")
    builder.add_slide('ISC_SSP_29', slide_text[29], "https://academy2.selva-research.com/images/ssp/Slide29.png")
    builder.add_slide('ISC_SSP_30', slide_text[30], "https://academy2.selva-research.com/images/ssp/Slide30.png")
    builder.add_slide('ISC_SSP_31', slide_text[31], "https://academy2.selva-research.com/images/ssp/Slide31.png")
    builder.add_slide('ISC_SSP_32', slide_text[32], "https://academy2.selva-research.com/images/ssp/Slide32.png")
    builder.add_slide('ISC_SSP_33', slide_text[33], "https://academy2.selva-research.com/images/ssp/Slide33.png")
    builder.add_slide('ISC_SSP_34', slide_text[34], "https://academy2.selva-research.com/images/ssp/Slide34.png")
    builder.add_slide('ISC_SSP_35', slide_text[35], "https://academy2.selva-research.com/images/ssp/Slide35.png")
    builder.add_slide('ISC_SSP_36', slide_text[36], "https://academy2.selva-research.com/images/ssp/Slide36.png")
    builder.add_slide('ISC_SSP_37', slide_text[37], "https://academy2.selva-research.com/images/ssp/Slide37.png")
    builder.add_slide('ISC_SSP_38', slide_text[38], "https://academy2.selva-research.com/images/ssp/Slide38.png")
    builder.add_slide('ISC_SSP_39', slide_text[39], "https://academy2.selva-research.com/images/ssp/Slide39.png")
    builder.add_slide('ISC_SSP_40', slide_text[40], "https://academy2.selva-research.com/images/ssp/Slide40.png")
    builder.add_slide('ISC_SSP_41', slide_text[41], "https://academy2.selva-research.com/images/ssp/Slide41.png")
    builder.add_slide('ISC_SSP_42', slide_text[42], "https://academy2.selva-research.com/images/ssp/Slide42.png")
    builder.add_slide('ISC_SSP_43', slide_text[43], "https://academy2.selva-research.com/images/ssp/Slide43.png")
    builder.add_slide('ISC_SSP_44', slide_text[44], "https://academy2.selva-research.com/images/ssp/Slide44.png")
    builder.add_slide('ISC_SSP_45', slide_text[45], "https://academy2.selva-research.com/images/ssp/Slide45.png")
    builder.add_slide('ISC_SSP_46', slide_text[46], "https://academy2.selva-research.com/images/ssp/Slide46.png")
    builder.add_slide('ISC_SSP_47', slide_text[47], "https://academy2.selva-research.com/images/ssp/Slide47.png")
    builder.add_slide('ISC_SSP_48', slide_text[48], "https://academy2.selva-research.com/images/ssp/Slide48.png")
    builder.add_slide('ISC_SSP_49', slide_text[49], "https://academy2.selva-research.com/images/ssp/Slide49.png")
    builder.add_slide('ISC_SSP_50', slide_text[50], "https://academy2.selva-research.com/images/ssp/Slide50.png")
    builder.add_slide('ISC_SSP_51', slide_text[51], "https://academy2.selva-research.com/images/ssp/Slide51.png")
    builder.add_slide('ISC_SSP_52', slide_text[52], "https://academy2.selva-research.com/images/ssp/Slide52.png")
    builder.add_slide('ISC_SSP_53', slide_text[53], "https://academy2.selva-research.com/images/ssp/Slide53.png")
    builder.add_slide('ISC_SSP_54', slide_text[54], "https://academy2.selva-research.com/images/ssp/Slide54.png")
    builder.add_slide('ISC_SSP_55', slide_text[55], "https://academy2.selva-research.com/images/ssp/Slide55.png")
    builder.add_slide('ISC_SSP_56', slide_text[56], "https://academy2.selva-research.com/images/ssp/Slide56.png")
    builder.add_slide('ISC_SSP_57', slide_text[57], "https://academy2.selva-research.com/images/ssp/Slide57.png")
    builder.add_slide('ISC_SSP_58', slide_text[58], "https://academy2.selva-research.com/images/ssp/Slide58.png")
    builder.add_slide('ISC_SSP_59', slide_text[59], "https://academy2.selva-research.com/images/ssp/Slide59.png")
    builder.add_slide('ISC_SSP_60', slide_text[60], "https://academy2.selva-research.com/images/ssp/Slide60.png")
    builder.add_slide('ISC_SSP_61', slide_text[61], "https://academy2.selva-research.com/images/ssp/Slide61.png")
    builder.add_slide('ISC_SSP_62', slide_text[62], "https://academy2.selva-research.com/images/ssp/Slide62.png")
    builder.add_slide('ISC_SSP_63', slide_text[63], "https://academy2.selva-research.com/images/ssp/Slide63.png")
    builder.add_slide('ISC_SSP_64', slide_text[64], "https://academy2.selva-research.com/images/ssp/Slide64.png")
    builder.add_slide('ISC_SSP_65', slide_text[65], "https://academy2.selva-research.com/images/ssp/Slide65.png")
    builder.add_slide('ISC_SSP_66', slide_text[66], "https://academy2.selva-research.com/images/ssp/Slide66.png")
    builder.add_slide('ISC_SSP_67', slide_text[67], "https://academy2.selva-research.com/images/ssp/Slide67.png")
    builder.add_slide('ISC_SSP_68', slide_text[68], "https://academy2.selva-research.com/images/ssp/Slide68.png")
    builder.add_slide('ISC_SSP_69', slide_text[69], "https://academy2.selva-research.com/images/ssp/Slide69.png")
    builder.add_slide('ISC_SSP_70', slide_text[70], "https://academy2.selva-research.com/images/ssp/Slide70.png")
    builder.add_slide('ISC_SSP_71', slide_text[71], "https://academy2.selva-research.com/images/ssp/Slide71.png")
    builder.add_slide('ISC_SSP_72', slide_text[72], "https://academy2.selva-research.com/images/ssp/Slide72.png")
    builder.add_slide('ISC_SSP_73', slide_text[73], "https://academy2.selva-research.com/images/ssp/Slide73.png")
    builder.add_slide('ISC_SSP_74', slide_text[74], "https://academy2.selva-research.com/images/ssp/Slide74.png")
    builder.add_slide('ISC_SSP_75', slide_text[75], "https://academy2.selva-research.com/images/ssp/Slide75.png")
    builder.add_slide('ISC_SSP_76', slide_text[76], "https://academy2.selva-research.com/images/ssp/Slide76.png")
    builder.add_slide('ISC_SSP_77', slide_text[77], "https://academy2.selva-research.com/images/ssp/Slide77.png")
    builder.add_slide('ISC_SSP_78', slide_text[78], "https://academy2.selva-research.com/images/ssp/Slide78.png")
    builder.add_slide('ISC_SSP_79', slide_text[79], "https://academy2.selva-research.com/images/ssp/Slide79.png")
    builder.add_slide('ISC_SSP_80', slide_text[80], "https://academy2.selva-research.com/images/ssp/Slide80.png")
    builder.add_slide('ISC_SSP_81', slide_text[81], "https://academy2.selva-research.com/images/ssp/Slide81.png")
    builder.add_slide('ISC_SSP_82', slide_text[82], "https://academy2.selva-research.com/images/ssp/Slide82.png")
    builder.add_slide('ISC_SSP_83', slide_text[83], "https://academy2.selva-research.com/images/ssp/Slide83.png")
    builder.add_slide('ISC_SSP_84', slide_text[84], "https://academy2.selva-research.com/images/ssp/Slide84.png")
    builder.add_slide('ISC_SSP_85', slide_text[85], "https://academy2.selva-research.com/images/ssp/Slide85.png")
    builder.add_slide('ISC_SSP_86', slide_text[86], "https://academy2.selva-research.com/images/ssp/Slide86.png")
    builder.add_slide('ISC_SSP_87', slide_text[87], "https://academy2.selva-research.com/images/ssp/Slide87.png")
    builder.add_slide('ISC_SSP_88', slide_text[88], "https://academy2.selva-research.com/images/ssp/Slide88.png")
    builder.add_slide('ISC_SSP_89', slide_text[89], "https://academy2.selva-research.com/images/ssp/Slide89.png")
    builder.add_slide('ISC_SSP_90', slide_text[90], "https://academy2.selva-research.com/images/ssp/Slide90.png")
    builder.add_slide('ISC_SSP_91', slide_text[91], "https://academy2.selva-research.com/images/ssp/Slide91.png")
    builder.add_slide('ISC_SSP_92', slide_text[92], "https://academy2.selva-research.com/images/ssp/Slide92.png")
    builder.add_slide('ISC_SSP_93', slide_text[93], "https://academy2.selva-research.com/images/ssp/Slide93.png")
    builder.add_slide('ISC_SSP_94', slide_text[94], "https://academy2.selva-research.com/images/ssp/Slide94.png")
    builder.add_slide('ISC_SSP_95', slide_text[95], "https://academy2.selva-research.com/images/ssp/Slide95.png")
    builder.add_slide('ISC_SSP_96', slide_text[96], "https://academy2.selva-research.com/images/ssp/Slide96.png")
    builder.add_slide('ISC_SSP_97', slide_text[97], "https://academy2.selva-research.com/images/ssp/Slide97.png")
    builder.add_slide('ISC_SSP_98', slide_text[98], "https://academy2.selva-research.com/images/ssp/Slide98.png")
    builder.add_slide('ISC_SSP_99', slide_text[99], "https://academy2.selva-research.com/images/ssp/Slide99.png")
    builder.add_slide('ISC_SSP_100', slide_text[100], "https://academy2.selva-research.com/images/ssp/Slide100.png")
    builder.add_slide('ISC_SSP_101', slide_text[101], "https://academy2.selva-research.com/images/ssp/Slide101.png")
    builder.add_slide('ISC_SSP_102', slide_text[102], "https://academy2.selva-research.com/images/ssp/Slide102.png")
    builder.add_slide('ISC_SSP_103', slide_text[103], "https://academy2.selva-research.com/images/ssp/Slide103.png")

    builder.add_quiz_start_slide()

    # Multiple Choice Questions
    builder.add_mc_question(
        'A wavenumber of 10,000 cm^-1 corresponds to a wavelength of…',
        [
            {'text': '10 um', 'correct': False, 'id': 0},
            {'text': '1 um', 'correct': True, 'id': 1},
            {'text': '0.1 um', 'correct': False, 'id': 2},
            {'text': '10 nm', 'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'An optical imager in which spectral region is more likely to require cryocooling?',
        [
            {'text': 'NIR', 'correct': False, 'id': 0},
            {'text': 'MIR/SWIR', 'correct': True, 'id': 1},
            {'text': 'UV', 'correct': False, 'id': 2},
            {'text': 'TIR', 'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'Which of the following is NOT a key design parameter for an optical imager?',
        [
            {'text': 'Pulse Repetition Frequency', 'correct': True, 'id': 0},
            {'text': 'Number of pixels', 'correct': False, 'id': 1},
            {'text': 'Focal length', 'correct': False, 'id': 2},
            {'text': 'Aperture', 'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'The number of bits with which the intensity of light is measured by an optical imager is also called…',
        [
            {'text': 'Spectral resolution', 'correct': False, 'id': 0},
            {'text': 'Radiometric resolution', 'correct': True, 'id': 1},
            {'text': 'Radiance', 'correct': False, 'id': 2},
            {'text': 'Bit rate', 'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )

    builder.add_mc_question(
        'For a VNIR imager at 800km with a focal length of 20cm and an aperture of 20cm, spatial resolution is more likely to be limited by?',
        [
            {'text': 'Optics (focal length)', 'correct': True, 'id': 0},
            {'text': 'Diffraction (aperture)', 'correct': False, 'id': 1},
            {'text': 'Both since they have the same value.', 'correct': False, 'id': 2},
            {
                'text': 'Neither since spatial resolution can be arbitrarily improved with data processing regardless of hardware.',
                'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=False
    )
    builder.add_quiz_end_slide()

    builder.add_mc_question(
        'Which of the following would likely increase the cost of an optical system?',
        [
            {'text': 'Reducing the focal length', 'correct': False, 'id': 0},
            {'text': 'Reducing the aperture', 'correct': False, 'id': 1},
            {'text': 'Adding UV bands', 'correct': True, 'id': 2},
            {'text': 'Removing UV bands', 'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'What would be a result of increasing the f-number of an optical system while keeping aperture constant?',
        [
            {'text': 'Improved ground sampling distance', 'correct': False, 'id': 0},
            {'text': 'Decreased cost', 'correct': False, 'id': 1},
            {'text': 'Increased cost', 'correct': False, 'id': 2},
            {'text': 'Both A&C', 'correct': True, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'The swath of a whiskbroom imager is primarily driven by?',
        [
            {'text': 'The scanning angle', 'correct': True, 'id': 0},
            {'text': 'The FOV', 'correct': False, 'id': 1},
            {'text': 'The number of pixels', 'correct': False, 'id': 2},
            {'text': 'The focal length', 'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Improving spatial resolution in a pushbroom imager is likely to also…',
        [
            {'text': 'Increase swath', 'correct': False, 'id': 0},
            {'text': 'Improve coverage', 'correct': False, 'id': 1},
            {'text': 'Degrade revisit time', 'correct': True, 'id': 2},
            {'text': 'Reduce cost', 'correct': False, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following would NOT result in higher payload data rates in an optical imager?',
        [
            {'text': 'Adding more bands', 'correct': False, 'id': 0},
            {'text': 'Increasing number of pixels', 'correct': False, 'id': 1},
            {'text': 'Decreasing altitude (and thus increasing orbital velocity)', 'correct': False, 'id': 2},
            {'text': 'Decreasing aperture size', 'correct': True, 'id': 3}
        ],
        '',
        ['Optical payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'In order for an L-band (~1.5 GHz) radiometer to have the same spatial resolution as an infrared radiometer (~2um wavelength) flying at the same altitude, how much larger should the aperture be?',
        [
            {'text': '100 times', 'correct': False, 'id': 0},
            {'text': '1000 times', 'correct': False, 'id': 1},
            {'text': '10,000 times', 'correct': False, 'id': 2},
            {'text': '100,000 times', 'correct': True, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following is more likely to be a cost driver in a space-based radar mission?',
        [
            {'text': 'A transmitted power of 100W', 'correct': False, 'id': 0},
            {'text': 'A GEO orbit', 'correct': True, 'id': 1},
            {'text': 'An aperture size of 2 meters', 'correct': False, 'id': 2},
            {'text': 'A look angle of 25 deg', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'The received power in a radar with a rectangular aperture is proportional to the orbit altitude to the power of n, where n equals?',
        [
            {'text': '2', 'correct': False, 'id': 0},
            {'text': '3', 'correct': False, 'id': 1},
            {'text': '-3', 'correct': True, 'id': 2},
            {'text': '-2', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'How does using Aperture Synthesis help?',
        [
            {'text': 'It increases the azimuth spatial resolution', 'correct': True, 'id': 0},
            {'text': 'It increases the penetration of the signals in the soil', 'correct': False, 'id': 1},
            {'text': 'It reduces the amount of data collected', 'correct': False, 'id': 2},
            {'text': 'It increases the SNR', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'In a Synthetic Aperture Radar, the azimuth resolution depends on altitude to the power of n, where n equals?',
        [
            {'text': '0', 'correct': True, 'id': 0},
            {'text': '-1', 'correct': False, 'id': 1},
            {'text': '-2', 'correct': False, 'id': 2},
            {'text': '-3', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'In a pulsed radar, how can you increase bandwidth without reducing pulse length?',
        [
            {'text': 'By using a narrower range of frequencies', 'correct': False, 'id': 0},
            {'text': 'By increasing the distance between the transmitter and receiver', 'correct': False, 'id': 1},
            {'text': 'By modulating the pulse', 'correct': True, 'id': 2},
            {'text': 'By employing a simpler data compression algorithm', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'If the frequency of a MW radiometer is changed from C-band (~4GHz) to L-band (~1.33 GHz), to keep the same spatial resolution the aperture will have to…?',
        [
            {'text': 'Increased by a factor of ~3', 'correct': True, 'id': 0},
            {'text': 'Decreased by a factor of ~3', 'correct': False, 'id': 1},
            {'text': 'Increased by a factor of ~9', 'correct': False, 'id': 2},
            {'text': 'Decreased by a factor of ~9', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Which of the following statement about SAR is false?',
        [
            {'text': 'Range resolution only depends on bandwidth and look angle', 'correct': False, 'id': 0},
            {'text': 'Azimuth resolution only depends on antenna length', 'correct': False, 'id': 1},
            {'text': 'Altitude does not affect resolution', 'correct': False, 'id': 2},
            {'text': 'Altitude does not affect SNR', 'correct': True, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'Increasing the number of looks in a radar will result in…',
        [
            {'text': 'Improved spatial resolution', 'correct': False, 'id': 0},
            {'text': 'Improved SNR', 'correct': True, 'id': 1},
            {'text': 'Increased bandwidth', 'correct': False, 'id': 2},
            {'text': 'Higher PRF', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_mc_question(
        'The pulse repetition frequency of a pulsed radar is?',
        [
            {'text': '1 over the pulse length', 'correct': False, 'id': 0},
            {'text': '1 over the time between two consecutive pulses', 'correct': True, 'id': 1},
            {'text': '1 over the integration time', 'correct': False, 'id': 2},
            {'text': 'The frequency of the waves in the pulses', 'correct': False, 'id': 3}
        ],
        '',
        ['Microwave payloads'],
        difficulty=0.75,
        discrimination=10,
        graded=True
    )

    builder.add_exam_finish_slide()

    return builder.get_module()

    




























    # builder.add_mc_question(
    #     'What band is most commonly used to determine atmospheric composition?',
    #     [
    #         {'text': 'VNIR', 'correct': True, 'id': 0},
    #         {'text': 'UV', 'correct': False, 'id': 1},
    #         {'text': 'MIR', 'correct': False, 'id': 2},
    #         {'text': 'TIR', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What band is most commonly used for thermal analysis?',
    #     [
    #         {'text': 'VNIR', 'correct': False, 'id': 0},
    #         {'text': 'UV', 'correct': False, 'id': 1},
    #         {'text': 'MIR', 'correct': False, 'id': 2},
    #         {'text': 'TIR', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following is the name of a satellite imaging system?',
    #     [
    #         {'text': 'Pushbroom', 'correct': False, 'id': 0},
    #         {'text': 'Whiskbroom', 'correct': False, 'id': 1},
    #         {'text': 'Matrix Imager', 'correct': False, 'id': 2},
    #         {'text': 'All of the above', 'correct': True, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'Which direction does a Pushbroom sensor capture data in?',
    #     [
    #         {'text': 'Across the swath line by line', 'correct': False, 'id': 0},
    #         {'text': 'In line with the limb of the Earth', 'correct': False, 'id': 1},
    #         {'text': 'Across the entire swath at once', 'correct': True, 'id': 2},
    #         {'text': 'Outward using the reflection of nearby planetary bodies', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=False
    # )
    #
    # builder.add_mc_question(
    #     'What is the "limb" of the Earth?',
    #     [
    #         {'text': 'A scientific name for clouds and aerosols', 'correct': False, 'id': 0},
    #         {'text': 'The edge of the planet seen from space', 'correct': True, 'id': 1},
    #         {'text': 'The thin layer of gasses in Earth\'s atmosphere', 'correct': False, 'id': 2},
    #         {'text': 'The area under a satellite\'s FOV', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
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
    # builder.add_quiz_end_slide()
    #
    # builder.add_mc_question(
    #     'Which of the following is a benefit of using a Multi-Angle Imaging Spectroradiometer?',
    #     [
    #         {'text': 'Determining angular distribution of a structure', 'correct': True, 'id': 0},
    #         {'text': 'Analyzing vertical profiles of atmospheric constituents', 'correct': False, 'id': 1},
    #         {'text': 'Limiting diffraction', 'correct': False, 'id': 2},
    #         {'text': 'Decreased cost', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'Which of the following is TRUE:',
    #     [
    #         {'text': 'Atmospheric conditions limit space observation optical systems', 'correct': False, 'id': 0},
    #         {'text': 'Resolution is determined using orbital velocity and aperture diameter', 'correct': False,
    #          'id': 1},
    #         {
    #             'text': 'If two points are too close in angle (or ground distance), they look like a single point due to the PSF (diffraction)',
    #             'correct': True, 'id': 2},
    #         {'text': 'Optical system design does not affect diffraction', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'How does high-resolution satellite imagery differ from low-resolution imagery?',
    #     [
    #         {'text': 'High resolution imagery incurs higher costs', 'correct': True, 'id': 0},
    #         {'text': 'Low-resolution imagery covers a smaller ground area', 'correct': False, 'id': 1},
    #         {'text': 'Low-resolution takes more images over the same area', 'correct': False, 'id': 2},
    #         {'text': 'Both B&C', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is the focal length of an optical system?',
    #     [
    #         {'text': 'The relationship between distances in the image plane and distances in the object plane',
    #          'correct': False, 'id': 0},
    #         {'text': 'The distance between the lens/mirror and the point at which all optical rays converge',
    #          'correct': True, 'id': 1},
    #         {'text': 'The relationship between the magnification and the aperture', 'correct': False, 'id': 2},
    #         {'text': 'The width of the object plane', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    # builder.add_mc_question(
    #     'What is required to determine the magnification of an optical system?',
    #     [
    #         {'text': 'Focal Length, Orbit Altitude', 'correct': True, 'id': 0},
    #         {'text': 'Orbit Altitude, F-number', 'correct': False, 'id': 1},
    #         {'text': 'Focal Length, F-number', 'correct': False, 'id': 2},
    #         {'text': 'F number, Aperture Length', 'correct': False, 'id': 3}
    #     ],
    #     '',
    #     ['Optics'],
    #     difficulty=0.5,
    #     discrimination=10,
    #     graded=True
    # )
    #
    #
    #
    #
    # builder.add_exam_finish_slide()
    # return builder.get_module()







