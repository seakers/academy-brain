import torch
import numpy as np

from transformers import AutoTokenizer

from academy_assistant.assistant.ModelLoader import ModelLoader
from academy_assistant.database.client.GraphqlClient import GraphqlClient


global_roles = {
    'MaterialRecommender': ['Spacecraft Bus', 'Mission Payloads', 'Parametric Estimation', 'Lifecycle Cost'],
    'QA': ['Analyst', 'Engineer', 'Critic', 'Historian', 'Teacher']
}


class Classifier:

    def __init__(self, user_info, library='QA'):
        self.roles = global_roles[library]
        self.model_loader = ModelLoader(library=library)
        self.graphql_client = GraphqlClient(user_info)

    def get_role(self, role):
        if isinstance(role, int):
            role = self.roles[role]
            return role
        elif isinstance(role, list):
            role = role[0]
            return self.get_role(role)
        else:
            return role

    def get_intent(self, role, intent):
        if isinstance(intent, list):
            intent = intent[0]
        role = self.get_role(role)
        role_index = self.roles.index(role) + 1
        intent_num = str(role_index)
        if intent >= 10:
            intent_num += '0'
        else:
            intent_num += '00'
        intent_num += str(intent)
        return int(intent_num)

    def recommend_material(self, command):
        role_probs = self.classify_learning_module(command)
        role_idx_list = [self.roles.index(r) for r in self.roles]
        role_slide_probs = []
        for role_idx in role_idx_list:
            slide_probs = self.classify_slide(command, [role_idx])
            role_slide_probs.append(slide_probs)

        print(role_slide_probs)

        confidence = []
        for idx, role_prob in enumerate(role_probs):
            module_obj = {
                'name': self.roles[idx],
                'id': self.graphql_client.get_learning_module_id(self.roles[idx]),
                'confidence': round(role_prob, 3),
                'slides': [],
            }
            slide_confidences = []
            confidence.append(module_obj)
            for idx2, slide_prob in enumerate(role_slide_probs[idx]):
                slide_confidences.append({
                    'id': idx2,
                    'confidence': round(slide_prob, 3)
                })
            slide_confidences.sort(key=lambda itenz: itenz['confidence'], reverse=True)
            module_obj['slides'] = slide_confidences
        confidence.sort(key=lambda itenz: itenz['confidence'], reverse=True)
        return confidence

    def classify_learning_module(self, command):
        # Get Models
        tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        loaded_model = self.model_loader.get_model('General')

        # Evaluation
        # ==================================================
        inputs = tokenizer(command, return_tensors="pt")
        outputs = loaded_model(**inputs)
        logits = outputs.logits
        softmax = torch.nn.Softmax(dim=1)
        probs = softmax(logits)
        logits = probs.detach().numpy()
        return logits.tolist()[0]

    def classify_slide(self, command, role):
        role = self.get_role(role)

        # Get Models
        tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        loaded_model = self.model_loader.get_model(role)

        # Evaluation
        # ==================================================
        inputs = tokenizer(command, return_tensors="pt")
        outputs = loaded_model(**inputs)
        logits = outputs.logits
        softmax = torch.nn.Softmax(dim=1)
        probs = softmax(logits)
        logits = probs.detach().numpy()
        return logits.tolist()[0]

    def classify_role(self, command, top_number=1):
        # Get Models
        tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        loaded_model = self.model_loader.get_model('General')

        # Evaluation
        # ==================================================
        inputs = tokenizer(command, return_tensors="pt")
        outputs = loaded_model(**inputs)
        logits = outputs.logits

        # Add softmax layer
        softmax = torch.nn.Softmax(dim=1)
        probs = softmax(logits)
        logits = probs.detach().numpy()
        print('--> ROLE MODEL OUTPUTS:', logits.tolist())
        prediction = self.interpret_logits(logits, top_number=top_number)
        print('--> FULL ROLE PREDICTION:', prediction)
        return prediction[0]

    def classify_role_intent(self, command, role):
        role = self.get_role(role)

        # Get Models
        tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        loaded_model = self.model_loader.get_model(role)

        # Evaluation
        # ==================================================
        inputs = tokenizer(command, return_tensors="pt")
        outputs = loaded_model(**inputs)
        logits = outputs.logits

        softmax = torch.nn.Softmax(dim=1)
        probs = softmax(logits)
        logits = probs.detach().numpy()
        print('--> INTENT MODEL OUTPUTS:', logits.tolist())

        # --> Prediction Confidence
        max_value = np.amax(logits)
        # print('--> Role Intent Classification Max Confidence:', max_value)
        if max_value > 0.95:
            top_number = 1
        elif max_value > 0.90:
            top_number = 3
        else:
            self.not_answerable(max_value)
            return

        prediction = self.interpret_logits(logits, top_number=top_number)
        return prediction[0]

    def not_answerable(self, max_value):
        raise Exception("Question prediction confidence too low: " + str(max_value))

    def interpret_logits(self, logits, top_number=1):
        logits_list = logits.tolist()
        predicted_labels = []
        for item in logits_list:
            index_list = np.argsort(item)[-top_number:]
            index_list = index_list[::-1]
            predicted_labels.append(np.ndarray.tolist(index_list))
        return predicted_labels
