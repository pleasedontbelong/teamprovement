import dj_database_url

from .base import *  # NOQA

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
    'storages',
]

MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE

PARENT_HOST = 'teamprovement.herokuapp.com'
ALLOWED_HOSTS = ['.%s' % PARENT_HOST]
SESSION_COOKIE_DOMAIN = ALLOWED_HOSTS[0]
SESSION_COOKIE_NAME = 'teamprovement-cookie'
