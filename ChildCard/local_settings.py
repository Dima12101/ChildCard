# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%dm9ce$!m8w$4a!y*hn$qmnji2b9+%4bey^i&4$1t$(4mrud6f'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ChildCard',
#         'USER': 'postgres',
#         'PASSWORD': 'Flvby66!',
#         'HOST': 'aws-rds-postgresql.cfxoin7bynly.us-east-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }


EMAIL_HOST_USER = 'child-card@mail.ru'
EMAIL_HOST_PASSWORD = 'Flvby66!'
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '287619930555-ka1kgni82rr81tc4j3ahjpt1k04fmfho.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'ijVowrmBABk86J2O-dzVBZiF'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_KEY = '463560134371758'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '6937a8f6279507b95ee4f5ec4bde6c03'  # App Secret
# #SOCIAL_AUTH_FACEBOOK_OAUTH2_SCOPE = ['email']
#
SOCIAL_AUTH_VK_OAUTH2_KEY = '7156125'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'pM3AhMVLczZejRt0Pia8'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

# add this code
SOCIAL_AUTH_INSTAGRAM_KEY = '3df5cf352d46480eb9a9e2b766760f2e'         #Client ID
SOCIAL_AUTH_INSTAGRAM_SECRET = '69cc20b50a3c467c971adc57d8d08a1b '  #Client SECRET


SOCIAL_AUTH_YANDEX_OAUTH2_KEY = 'bfc3315c5f1c4fd086cc49f6e5a40b03'         #Client ID
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = '8ee5176ef3944d5e9e18cdb413b427de '  #Client SECRET