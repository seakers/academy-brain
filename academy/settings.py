"""
Django settings for academy project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=quqh!f&n7xng*a@3r4t=n)+o_5ariwd-g1+q!0lvj+avni$)3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

USE_X_FORWARDED_HOST = True

# Application definition

INSTALLED_APPS = [
    # Installed Packages
    'channels',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    # Academy APIs
    'academy',
    'academy_auth',
    'academy_assistant',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'academy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'academy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'academy',
        'USER': 'academy',
        'PASSWORD': 'academy',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'https://academy.selva-research.com'
)

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = (
    'http://localhost:8080',
    "https://academy.selva-research.com"
)



# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [('127.0.0.1', '6379')],
        }
    },
}


ASGI_APPLICATION = 'academy.asgi.application'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



####################
### Academy Path ###
####################
ACADEMY_PATH = '/home/ec2-user/academy-brain'





#################
### NN Models ###
#################
NN_MODELS = {}
NN_MODELS_LIB_PATH = '/home/ec2-user/academy-brain/academy_assistant/assistant/models'
LOAD_NN_MODELS = False
if LOAD_NN_MODELS is True:
    print('--> LOADING NN MODELS')
    import os
    from pathlib import Path
    from transformers import AutoModelForSequenceClassification
    model_lib_dict = {}
    model_lib_path = Path(NN_MODELS_LIB_PATH)
    for model_folder in os.scandir(model_lib_path):
        if model_folder.is_dir():
            model_folder_name = model_folder.name
            model_folder_path = os.path.join(model_lib_path, model_folder_name)
            model_dict = {}
            model_lib_dict[model_folder_name] = model_dict
            for file in os.scandir(model_folder_path):
                if file.is_dir():
                    role_name = file.name
                    role_model_path = os.path.join(model_folder_path, role_name)
                    loaded_model = AutoModelForSequenceClassification.from_pretrained(role_model_path)
                    model_dict[role_name] = loaded_model
    NN_MODELS = model_lib_dict
    print('--> FINISHED LOADING NN MODELS')





###########
### NLP ###
###########

import spacy
NLP_MODEL = spacy.load('en_core_web_sm')







LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'
        },
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y/%m/%d %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'debugging': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'config': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

















