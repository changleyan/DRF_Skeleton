# -*- coding: utf-8 -*-
import os
import platform

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DV_DEBUG', True))

# Activity log
ACTIVITY_LOG = '__all__'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOWED_ORIGINS = ['https://*',
                        'http://*', ]
CORS_ALLOW_ALL_METHODS = True

if platform.system() == 'Windows':
    REPORTS_PATH = "C:\\Users\\USER\\Documents\\reports\\"
else:
    REPORTS_PATH = "/var/reports/"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'base',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'logs_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'logs_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}

# LOGGING
LOGGIN_FILENAME = os.path.join(BASE_DIR, './logs/api.file.log')
LOGGIN_FILENAME_ERROR = os.path.join(BASE_DIR, './logs/api.file.error.log')
