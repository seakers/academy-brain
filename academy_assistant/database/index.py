import os
import sys
import django
import json


# --> Setup django for standalone use
sys.path.append('/home/ec2-user/academy-brain')
sys.path.append('/home/ec2-user/academy-brain/academy_assistant')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academy.settings')
django.setup()
from django.contrib.auth.models import User

from client.Client import Client
from client.Excel import Excel
from client.Topic import Topic
from client.LearningModule import LearningModule
from client.Message import Message
from client.Questions import Questions


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
# Experiment Users
# ------------------------------------
test_experiment_user = {
    'username': 'testuser',
    'email': 'testuser@seaklab.com',
    'password': 'testuser',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_1 = {
    'username': 'subject1',
    'email': 'subject1@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_2 = {
    'username': 'subject2',
    'email': 'subject2@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_3 = {
    'username': 'subject3',
    'email': 'subject3@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_4 = {
    'username': 'subject4',
    'email': 'subject4@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_5 = {
    'username': 'subject5',
    'email': 'subject5@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_6 = {
    'username': 'subject6',
    'email': 'subject6@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_7 = {
    'username': 'subject7',
    'email': 'subject7@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_8 = {
    'username': 'subject8',
    'email': 'subject8@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_9 = {
    'username': 'subject9',
    'email': 'subject9@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_10 = {
    'username': 'subject10',
    'email': 'subject10@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_11 = {
    'username': 'subject11',
    'email': 'subject11@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_12 = {
    'username': 'subject12',
    'email': 'subject12@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_13 = {
    'username': 'subject13',
    'email': 'subject13@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_14 = {
    'username': 'subject14',
    'email': 'subject14@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_15 = {
    'username': 'subject15',
    'email': 'subject15@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_16 = {
    'username': 'subject16',
    'email': 'subject16@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_17 = {
    'username': 'subject17',
    'email': 'subject17@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_18 = {
    'username': 'subject18',
    'email': 'subject18@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_19 = {
    'username': 'subject19',
    'email': 'subject19@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_20 = {
    'username': 'subject20',
    'email': 'subject20@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_21 = {
    'username': 'subject21',
    'email': 'subject21@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_22 = {
    'username': 'subject22',
    'email': 'subject22@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_23 = {
    'username': 'subject23',
    'email': 'subject23@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_24 = {
    'username': 'subject24',
    'email': 'subject24@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_25 = {
    'username': 'subject25',
    'email': 'subject25@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_26 = {
    'username': 'subject26',
    'email': 'subject26@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_27 = {
    'username': 'subject27',
    'email': 'subject27@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_28 = {
    'username': 'subject28',
    'email': 'subject28@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
}
# ------------------------------------
experiment_user_29 = {
    'username': 'subject29',
    'email': 'subject29@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_30 = {
    'username': 'subject30',
    'email': 'subject30@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T1', 'T2'],
    'assistant': True,
    'assistant_order': [1, 0]
}
experiment_user_31 = {
    'username': 'subject31',
    'email': 'subject31@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': False,
    'assistant_order': [0, 1]
}
experiment_user_32 = {
    'username': 'subject32',
    'email': 'subject32@seaklab.com',
    'password': 'U4VPbxK2Ch9PZ5NL',
    'task_order': ['T2', 'T1'],
    'assistant': True,
    'assistant_order': [1, 0]
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
    experiment_user_11,
    experiment_user_12,
    experiment_user_13,
    experiment_user_14,
    experiment_user_15,
    experiment_user_16,
    experiment_user_17,
    experiment_user_18,
    experiment_user_19,
    experiment_user_20,
    experiment_user_21,
    experiment_user_22,
    experiment_user_23,
    experiment_user_24,
    experiment_user_25,
    experiment_user_26,
    experiment_user_27,
    experiment_user_28,
    experiment_user_29,
    experiment_user_30,
    experiment_user_31,
    experiment_user_32,
    test_experiment_user
]

def main():

    client = Client()

    # DROP / CREATE TABLES
    client.initialize()

    # Index demo users
    index_demo_users(client)
    index_experiment_users(client)

    # Index learning content
    Excel(client).index()
    LearningModule(client).index()
    Questions(client).index()
    Topic(client).index()
    Message(client).index()



def index_demo_users(client):
    usernames = [x.username for x in client.get_users()]
    for account in demo_accounts:
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