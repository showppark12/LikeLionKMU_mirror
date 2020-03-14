from .base import *


SECRET_KEY = '@gc%$&53_n#2cyl5=ivq0fg(*9y@_)c7w9f3%az01%o3o6lbw^'

DEBUG = True  # 배포 시 false

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            # mysql.py의 경로
            'read_default_file': os.path.join(BASE_DIR, "conf/mysql.cnf")
        }
    }
}

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
