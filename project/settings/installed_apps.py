# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cors headers
    'corsheaders',

    # Django rest framework
    'rest_framework', 
    'rest_framework_simplejwt',

    # My apps
    'recipes',
    'authors',
    'tag',
]