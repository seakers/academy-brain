from django.conf import settings


class ModelLoader:

    def __init__(self, library='CA'):
        self.nn_models = settings.NN_MODELS[library]

    def get_model(self, key):
        return self.nn_models[key]