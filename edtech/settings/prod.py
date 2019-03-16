import os
import sys

from common import Common
from edtech.settings import log_conf

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Prod(Common):
    DEBUG = False
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    LOGGING = log_conf.get(log_root='/var/log/edtech/')
