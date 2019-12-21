import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE", "DEFAULT_VALUE"),
        'HOST': os.getenv("HOST", "DEFAULT_VALUE"),
        'PORT': os.getenv("PORT", "DEFAULT_VALUE"),
        'NAME': os.getenv("NAME", "DEFAULT_VALUE"),
        'USER': os.getenv("USER", "DEFAULT_VALUE"),
        'PASSWORD': os.getenv("PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
