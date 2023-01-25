import os
from pathlib import Path
from PIL import Image

import pytesseract
import string
pytesseract.pytesseract.tesseract_cmd = r'/home/ec2-user/installs/vcpkg/installed/x64-linux/tools/tesseract/tesseract'


def run_images():
    print('--> PARSING IMAGES')
    t_dir = 'Slides'

    cwd = Path.cwd()
    t_path = os.path.join(cwd, t_dir)

    for filename in os.listdir(t_path):
        slide_class = int(filename.split('.', 1)[0])
        f_path = os.path.join(t_path, filename)
        print(f_path)
        img = Image.open(f_path)
        text = pytesseract.image_to_string(img)
        lines = text.splitlines()
        for line in lines:
            test_str = line.translate(str.maketrans('', '', string.punctuation))
            print(test_str.lower())


        print(len(lines), lines)

def run2():
    print('--> TRANSFORMING QUESTIONS')
    t_dir = 'QA2'
    cwd = Path.cwd()
    t_path = os.path.join(cwd, t_dir)
    print(t_path)

    for filename in os.listdir(t_path):
        question_class = int(filename.split('.', 1)[0])
        full_path = os.path.join(t_path, filename)
        with open(full_path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        state = 1
        for idx, line in enumerate(data):
            if line == '--\n':
                state += 1
            else:
                if state == 1:
                    num_questions = int(line[:-1])
                elif state == 3:
                    labels = line[:-1]
                    if question_class in range(1000, 2000):
                        data[idx] = '1000'
                    elif question_class in range(2000, 3000):
                        data[idx] = '0100'
                    elif question_class in range(3000, 4000):
                        data[idx] = '0010'
                    elif question_class in range(4000, 5000):
                        data[idx] = '0001'
        with open(full_path, 'w', encoding='utf-8') as file:
            file.writelines(data)


def run():
    t_dir = 'QA2'

    print('--> TRANSFORMING QUESTIONS')
    cwd = Path.cwd()
    t_path = os.path.join(cwd, t_dir)
    print(t_path)

    mp = 0
    sb = 0
    pe = 0
    lc = 0
    for filename in os.listdir(t_path):
        question_class = int(filename.split('.', 1)[0])
        old_name = os.path.join(t_path, filename)
        new_name = old_name
        if question_class in range(5000, 5017):
            if mp < 10:
                new_name = '200' + str(mp) + '.txt'
            else:
                new_name = '20' + str(mp) + '.txt'
            print('MISSION PAYLOADS')
            mp += 1
        elif question_class in range(5017, 5038):
            if sb < 10:
                new_name = '100' + str(sb) + '.txt'
            else:
                new_name = '10' + str(sb) + '.txt'
            print('SPACECRAFT BUS')
            sb += 1
        elif question_class == 5038:
            if pe < 10:
                new_name = '300' + str(pe) + '.txt'
            else:
                new_name = '30' + str(pe) + '.txt'
            print('PARAMETRIC ESTIMATION')
            pe += 1
        elif question_class in range(5039, 5049):
            if lc < 10:
                new_name = '400' + str(lc) + '.txt'
            else:
                new_name = '40' + str(lc) + '.txt'
            print('LIFECYCLE COST')
            lc += 1
        new_name = os.path.join(t_path, new_name)
        print(new_name)
        os.rename(old_name, new_name)



        # print(question_class)









if __name__ == '__main__':
    run_images()