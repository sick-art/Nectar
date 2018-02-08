from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='*6+^2cv^s=d$r5q(i7l%0n1&yq@fr0fz31kj^ing$hq2doecpv')

DEBUG = env.bool('DJANGO_DEBUG', default=True)