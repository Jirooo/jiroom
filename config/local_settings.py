import os
BASE_DIR = os.path(__file__).resolve().parent.parent # django

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

Debug = True