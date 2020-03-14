from KMU_likelion.base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG")  # 배포 시 false

ALLOWED_HOSTS = ['*']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

# SECURE_SSL_REDIRECT = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            # mysql.py의 경로
            'read_default_file': os.path.join(BASE_DIR, "conf/mysql.cnf")
        }
    }
}

# FRONTEND_BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR))), 'Frontend', 'frontend-react')
# FRONTEND_TEMPLATE_ROOT = os.path.join(FRONTEND_BASE_DIR, 'build', 'index.html')
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

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'frontend', 'build', 'static')
# ]