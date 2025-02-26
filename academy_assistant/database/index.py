import os
import sys
import django
import json


# --> Setup django for standalone use
sys.path.append('/home/ec2-user/academy-brain')
sys.path.append('/home/ec2-user/academy-brain/academy_assistant')
# sys.path.append('E:/SEM IV - Courses/GAR/Work/Source Code/academy-brain')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academy.settings')
django.setup()
from django.contrib.auth.models import User

from client.Client import Client
from client.Excel import Excel
from client.Topic import Topic
from client.LearningModule import LearningModule
from client.Message import Message
from client.Questions import Questions
from client.TextBook import TextBook


gabe_account = {
    'username': 'gapaza',
    'email': 'gapaza@seaklab.com',
    'password': '29tLzDN3AE7B5h5C'
}

bryan_account = {
    'username': 'bcoots',
    'email': 'bcoots@seaklab.com',
    'password': 'Yq7s5GXZaQ8vH7k6'
}

jennifer_account = {
    'username': 'jbowles',
    'email': 'jbowles@seaklab.com',
    'password': 'yzAhcenF3TdrCuve'
}

jennifer2_account = {
    'username': 'jbowles2',
    'email': 'jbowles@seaklab.com',
    'password': 'yzAhcenF3TdrCuve2'
}

greg_account = {
    'username': 'ghogan',
    'email': 'ghogan@seaklab.com',
    'password': 'EP9fAq3PpFW6gKLc'
}

dani_account = {
    'username': 'dselva',
    'email': 'dselva@seaklab.com',
    'password': 'aYH8x9y9hPsghbK5'
}

demo_user_1 = {
    'username': 'duser1',
    'email': 'duser1@seaklab.com',
    'password': 'MDEdnqxs373gK8Um'
}
demo_user_2 = {
    'username': 'duser2',
    'email': 'duser2@seaklab.com',
    'password': 'qJ64ZPLaGum8XcDf'
}
demo_user_3 = {
    'username': 'duser3',
    'email': 'duser3@seaklab.com',
    'password': 'UY2TV8DUUfgzdGVr'
}
demo_user_4 = {
    'username': 'duser4',
    'email': 'duser4@seaklab.com',
    'password': '667Ayq9UJNz2U2Tb'
}
demo_user_5 = {
    'username': 'duser5',
    'email': 'duser5@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL'
}

# cape_accounts = [
#     {'username': 'mlane', 'email': 'mlane@seaklab.com', 'password': '1aZ3xE8sB7pV9dT4'},
#     {'username': 'gsummers', 'email': 'gsummers@seaklab.com', 'password': '8yW2vQ6mR3kU1hN0'},
#     {'username': 'hdougherty', 'email': 'hdougherty@seaklab.com', 'password': '4nL7jX2wV9zP0aT3'},
#     {'username': 'dlyons', 'email': 'dlyons@seaklab.com', 'password': '5bQ8kJ1sM7pX6eZ2'},
#     {'username': 'chowells', 'email': 'chowells@seaklab.com', 'password': '2rN9xC4vB8lF7tW1'},
#     {'username': 'sfitzpatrick', 'email': 'sfitzpatrick@seaklab.com', 'password': '0yU5mR3kW8nL7jX4'},
#     {'username': 'jpatterson', 'email': 'jpatterson@seaklab.com', 'password': '9dP1vT7kE4sX6mZ5'},
#     {'username': 'aknepper', 'email': 'aknepper@seaklab.com', 'password': '6fL2nW8xJ5pV9tR3'}
# ]

cape_accounts = [
    {'username': 'mlane', 'email': 'mlane@seaklab.com', 'password': '1aZ3xE8sB7pV9dT4'},
    {'username': 'gsummers', 'email': 'gsummers@seaklab.com', 'password': '8yW2vQ6mR3kU1hN0'},
    {'username': 'hdougherty', 'email': 'hdougherty@seaklab.com', 'password': '4nL7jX2wV9zP0aT3'},
    {'username': 'dlyons', 'email': 'dlyons@seaklab.com', 'password': '5bQ8kJ1sM7pX6eZ2'},
    {'username': 'chowells', 'email': 'chowells@seaklab.com', 'password': '2rN9xC4vB8lF7tW1'},
    {'username': 'sfitzpatrick', 'email': 'sfitzpatrick@seaklab.com', 'password': '0yU5mR3kW8nL7jX4'},
    {'username': 'jpatterson', 'email': 'jpatterson@seaklab.com', 'password': '9dP1vT7kE4sX6mZ5'},
    {'username': 'aknepper', 'email': 'aknepper@seaklab.com', 'password': '6fL2nW8xJ5pV9tR3'},

    {'username': 'ghogan', 'email': 'gregory.hogan.3@us.af.mil', 'password': 'A1b2C3d4E5f6G7h8'},
    {'username': 'kpethel', 'email': 'kaylee.pethtel@us.af.mil', 'password': 'H8g7F6e5D4c3B2a1'},
    {'username': 'cmohindroo', 'email': 'chelsea.mohindroo@us.af.mil', 'password': 'I2j3K4l5M6n7O8p9'},
    {'username': 'econcepcion', 'email': 'enid.alvira-concepcion@us.af.mil', 'password': 'P9o8N7m6L5k4J3i2'},
    {'username': 'cmccarthy', 'email': 'christopher.mccarthy.18@us.af.mil', 'password': 'Q1r2S3t4U5v6W7x8'},
    {'username': 'apena', 'email': 'anthony.pena.3@us.af.mil', 'password': 'Y8x7W6v5U4t3S2r1'},
    {'username': 'phach', 'email': 'patricia.hach@us.af.mil', 'password': 'Z2a3B4c5D6e7F8g9'},
    {'username': 'efisk', 'email': 'estevan.fisk@us.af.mil', 'password': 'G9f8E7d6C5b4A3z2'},
    {'username': 'tpackard', 'email': 'travis.packard.4@us.af.mil', 'password': 'X1y2Z3a4B5c6D7e8'},
    {'username': 'cwhitehorn', 'email': 'christopher.whitehorn.1@us.af.mil', 'password': 'F8g7H6i5J4k3L2m1'},
    {'username': 'dvasconi', 'email': 'dawson.vasconi.1@us.af.mil', 'password': 'M1n2O3p4Q5r6S7t8'},
    {'username': 'nbiancalana', 'email': 'nickolas.biancalana.1@us.af.mil', 'password': 'T8u7V6w5X4y3Z2a1'},
    {'username': 'wkim', 'email': 'william.kim.11@us.af.mil', 'password': 'B1c2D3e4F5g6H7i8'},
    {'username': 'kjawad', 'email': 'jawad.kazi@us.af.mil', 'password': 'J8k7L6m5N4o3P2q1'}
]



demo_accounts = [
    dani_account,
    jennifer_account,
    jennifer2_account,
    bryan_account,
    greg_account,
    gabe_account,
    demo_user_1,
    demo_user_2,
    demo_user_3,
    demo_user_4,
    demo_user_5,
]






# ------------------------------------
# Experiment Users (20 total)
# ------------------------------------
test_experiment_user = {
    'username': 'testuser',
    'email': 'testuser@seaklab.com',
    'password': 'testuser',
}
# ------------------------------------
experiment_user_1 = {
    'username': 'soaracc1',
    'email': 'soaracc1@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_2 = {
    'username': 'soaracc2',
    'email': 'soaracc2@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_3 = {
    'username': 'soaracc3',
    'email': 'soaracc3@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_4 = {
    'username': 'soaracc4',
    'email': 'soaracc4@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_5 = {
    'username': 'soaracc5',
    'email': 'soaracc5@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_6 = {
    'username': 'soaracc6',
    'email': 'soaracc6@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_7 = {
    'username': 'soaracc7',
    'email': 'soaracc7@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_8 = {
    'username': 'soaracc8',
    'email': 'soaracc8@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_9 = {
    'username': 'soaracc9',
    'email': 'soaracc9@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_10 = {
    'username': 'soaracc10',
    'email': 'soaracc10@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_11 = {
    'username': 'soaracc11',
    'email': 'soaracc11@seaklab.com',
    'password': 'campsoar24',
}
experiment_user_12 = {
    'username': 'soaracc12',
    'email': 'soaracc12@seaklab.com',
    'password': 'campsoar24',
}











experiment_accounts = [
    experiment_user_1,
    experiment_user_2,
    experiment_user_3,
    experiment_user_4,
    experiment_user_5,
    experiment_user_6,
    experiment_user_7,
    experiment_user_8,
    experiment_user_9,
    experiment_user_10,
    test_experiment_user
]

def main():

    client = Client()

    # DROP / CREATE TABLES
    client.initialize()
    print("Init Done")
    
    # Index demo users
    index_demo_users(client)
    print("#####1##########")

    # index_experiment_users(client)
    # print("#####2##########")


    # Index learning content
    Excel(client).index()
    print("#####3##########")

    LearningModule(client).index()
    print("#####4##########")

    Questions(client).index()
    print("#####5##########")

    Topic(client).index()
    print("#####6##########")

    Message(client).index()
    print("#####7##########")

    TextBook(client).index()
    print("#####8##########")




def index_demo_users(client):
    usernames = [x.username for x in client.get_users()]
    combined_accounts = demo_accounts + experiment_accounts + cape_accounts
    for account in combined_accounts:
        if account['username'] not in usernames:
            user = User.objects.create_user(account['username'], account['email'], account['password'])
            user.save()
            client.index_authuser_group(user.id, 1)


def index_experiment_users(client):
    all_users = client.get_users()
    usernames = [x.username for x in all_users]
    ids = [x.id for x in all_users]
    for idx, account in enumerate(experiment_accounts):
        if account['username'] not in usernames:
            user = User.objects.create_user(account['username'], account['email'], account['password'])
            user.save()
            client.index_authuser_group(user.id, 1)
            task_order = json.dumps(account['task_order'])
            assistant_order = json.dumps(account['assistant_order'])
            client.index_experiment_user(user.id, account['assistant'], task_order, assistant_order)
            user.save()
        else:
            user_idx = usernames.index(account['username'])
            user_id = ids[user_idx]
            task_order = json.dumps(account['task_order'])
            assistant_order = json.dumps(account['assistant_order'])
            client.index_experiment_user(user_id, account['assistant'], task_order, assistant_order)






if __name__ == "__main__":
    main()