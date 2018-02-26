ALLOWED_HOSTS = ['*']
DEBUG = False

# The values below are loaded from environment variables
import os

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_DATABASE'], 
        'USER': os.environ['DATABASE_USERNAME'],
        'PASSWORD': os.environ['MYSQL_ROOT_PASSWORD'],
        'HOST': 'db'
    }
}
