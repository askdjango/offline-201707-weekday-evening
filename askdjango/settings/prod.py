from .common import *

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['storages']

STATICFILES_STORAGE = 'askdjango.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'askdjango.storages.MediaS3Boto3Storage'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = 'askdjango-weekday-evening'
AWS_S3_REGION_NAME = 'ap-northeast-2'

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}

