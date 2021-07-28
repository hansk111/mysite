from .base import *

ALLOWED_HOSTS = ['3.38.71.222', 'smarthan.site']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False

# DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.mysql',
#           'NAME': 'smarthandb',
#           'HOST': 'localhost',
#           'PORT': '3306',
#           'USER': 'root',
#           'PASSWORD': 'admin'
#       }
#   }



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#       'default': {
#           'ENGINE': 'django.db.backends.postgresql_psycopg2',
#           'NAME': 'mysite',
#           'HOST': 'localhost',
#           'PORT': '5432',
#           'USER': 'han',
#           'PASSWORD': 'han'
#       }
# }



# root password : admin
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'smarthandb',
          'HOST': 'localhost',
          'PORT': '3306',
          'USER': 'root',
          'PASSWORD': 'admin'
      }
  }