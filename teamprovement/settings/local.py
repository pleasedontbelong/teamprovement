import dj_database_url

from .base import *  # NOQA

DEBUG = True
SHELL_PLUS = "ipython"

DATABASES['default'] = dj_database_url.parse('postgres://teamprov:teamprov@localhost:5432/teamprov', conn_max_age=600)
