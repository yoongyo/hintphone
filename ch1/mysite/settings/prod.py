from .common import *

DEBUG = False
ALLOWED_HOSTS = ['hintphone.pythonanywhere.com']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mysite', 'staticfiles')
STATICFILES_DIRS = [
 os.path.join(BASE_DIR,  'mysite', 'static'),
]