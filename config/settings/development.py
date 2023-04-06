from .base import *

DEBUG = True

# Database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override Installed App
INSTALLED_APPS += [
    'blog.apps.BlogConfig'

]