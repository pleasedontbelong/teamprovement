import os

ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')

if ENVIRONMENT is None:
    raise ValueError('ENVIRONMENT is a mandatory variable!')
elif ENVIRONMENT == 'production':
    from .prod import *  # NOQA
elif ENVIRONMENT == 'test':
    from .test import *  # NOQA
elif ENVIRONMENT == 'local':
    from .local import *  # NOQA
else:
    raise ValueError('Incorrect value for ENVIRONMENT!')
