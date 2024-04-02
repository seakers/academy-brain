import os
import sys
import django
import json


# --> Setup django for standalone use
# sys.path.append('/home/ec2-user/academy-brain')
# sys.path.append('/home/ec2-user/academy-brain/academy_assistant')
sys.path.append('E:/SEM IV - Courses/GAR/Work/Source Code/academy-brain')
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

    index_experiment_users(client)
    print("#####2##########")


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