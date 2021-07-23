"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'picw434tao3z90pp8dr+u=qyigfo@p#i!c$i*=s!=gl133y47b'
# SECRET_KEY = os.environ.get('SECRET_KEY','picw434tao3z90pp8dr+u=qyigfo@p#i!c$i*=s!=gl133y47b')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = int(os.environ.get('DEBUG', 1))

# if os.environ.get('DJANGO_ALLOWED_HOSTS'):
#     ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
# else:
#     ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['52.78.44.13']


# Application definition


BATON = {
    'SITE_HEADER': 'SmartHAN',
    'SITE_TITLE': 'Baton',
    'INDEX_TITLE': 'SmartHAN administration',
    'SUPPORT_HREF': 'https://smarthan.com',
    'COPYRIGHT': 'copyright © 2021 <a href="https://www.smarthan.com">SmartHAN</a>',
    'POWERED_BY': '<a href="https://www.smarthan.com">SmartHAN</a>',
    # 'CONFIRM_UNSAVED_CHANGES': True,
    # 'SHOW_MULTIPART_UPLOADING': True,
    # 'ENABLE_IMAGES_PREVIEW': True,
    # 'CHANGELIST_FILTERS_IN_MODAL': True,
    # 'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    # 'CHANGELIST_FILTERS_FORM': True,
    # 'MENU_ALWAYS_COLLAPSED': False,
    # 'MENU_TITLE': 'Menu',
    # 'MESSAGES_TOASTS': False,
    # 'GRAVATAR_DEFAULT_IMG': 'retro',
    # 'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    # 'SEARCH_FIELD': {
    #     'label': 'Search contents...',
    #     'url': '/search/',
    # },
    # 'MENU': (
    #     { 'type': 'title', 'label': 'main', 'apps': ('auth', ) },
    #     {
    #         'type': 'app',
    #         'name': 'auth',
    #         'label': 'Authentication',
    #         'icon': 'fa fa-lock',
    #         'models': (
    #             {
    #                 'name': 'user',
    #                 'label': 'Users'
    #             },
    #             {
    #                 'name': 'group',
    #                 'label': 'Groups'
    #             },
    #         )
    #     },
    #     { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
    #     { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
    #     { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
    #     { 'type': 'free', 'label': 'My parent voice', 'default_open': True, 'children': [
    #         { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp' },
    #         { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
    #     ] },
    # ),
    # 'ANALYTICS': {
    #     'CREDENTIALS': os.path.join(BASE_DIR, 'credentials.json'),
    #     'VIEW_ID': '12345678',
    # }
}

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board.apps.BoardConfig',
    'common.apps.CommonConfig',
    'baton.autodiscover',
    'photo.apps.PhotoConfig',
    'widget_tweaks',
    'scard',
    'chart',
    'video',
    #allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'mptt',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    'easy_thumbnails',

]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }


}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# ---------------------------------- [edit] ---------------------------------- #
# 로그인 성공후 이동하는 URL

# ---------------------------------------------------------------------------- #
# ---------------------------------- [edit] ---------------------------------- #
# 로그아웃 성공후 이동하는 URL
LOGOUT_REDIRECT_URL = '/'

DATA_UPLOAD_MAX_MEMORY_SIZE = 1000485760

AUTH_USER_MODEL = 'common.User'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SITE_ID = 2

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
# 메일을 호스트하는 서버
EMAIL_PORT = '587'
# gmail과의 통신하는 포트
EMAIL_HOST_USER = 'hanseokhee.han@gmail.com'
# 발신할 이메일
EMAIL_HOST_PASSWORD = 'han1475!'
# 발신할 메일의 비밀번호
EMAIL_USE_TLS = True
# TLS 보안 방법
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# 사이트와 관련한 자동응답을 받을 이메일 주소