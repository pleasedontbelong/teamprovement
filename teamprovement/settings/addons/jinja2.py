# Full configuration in http://niwinz.github.io/django-jinja/latest/#_installation
from django_jinja.builtins import DEFAULT_EXTENSIONS

INSTALLED_APPS += ('django_jinja',)  # NOQA

TEMPLATES += [  # NOQA
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja2",
            "app_dirname": "jinja2",
            "auto_reload": True,  # Set to False in prod
            "extensions": DEFAULT_EXTENSIONS + ["pipeline.jinja2.PipelineExtension"],
            # "environment": "myproject.jinja2.environment",  # (optional) if you have one
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    },
]
