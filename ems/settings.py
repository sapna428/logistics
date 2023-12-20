

from pathlib import Path
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--w(dug*va_megpa25w$gmv8o6+f8!fg_*m1^u$)z25pab0hicm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'employee_information.apps.EmployeeInformationConfig',
    'django.contrib.humanize',
    'chartjs',
     'crispy_forms',
    'crispy_bootstrap4',
     'import_export',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ems.urls'

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

WSGI_APPLICATION = 'ems.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'ltv',
    #     'USER': 'root',
    #     'PASSWORD': 'sapna',
    #     'HOST':'localhost',
    #     'PORT': '3306',
    #     'OPTIONS':{
    #         'sql_mode': 'traditional',
    #     }
    # }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'

EMAIL_HOST_USER = 'sapnakousar428.3@gmail.com'

EMAIL_HOST_PASSWORD = 'vusp jfzu lkvl djar'
EMAIL_PORT = 587
EMAIL_USE_TLS=True
EMAIL_USE_SLS=False


EMAIL_SIGNATURE = """

     
    Thank you for connecting to LTV Logistics!
    Best Regards,
     LTV LogisticsTeam




     
"""
import os

# Define the base directory for media uploads
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# import django_heroku
# import dj_database_url
# Add these lines to your settings.py file
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [   os.path.join(BASE_DIR, 'static')]

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # location of your application, should not be public web accessible 
    './static',
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]
# import os
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
# # STATIC_DIR = BASE_DIR / 'static'
# MEDIA_DIR = BASE_DIR / 'media'
# MEDIA_ROOT = MEDIA_DIR
# MEDIA_URL = '/media/'
from django.urls import path

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / "static"]



import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# django_heroku.settings(locals())


from django.conf import settings
from django.conf.urls.static import static