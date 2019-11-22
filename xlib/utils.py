import uuid
from hashlib import sha512

import jwt
from django.conf import settings
from django.utils.timezone import datetime, timedelta


def generate_uid():
    return uuid.uuid4()


def check_key(key, hash_key):
    if _hash_key(key) == hash_key:
        return True
    return False


def generate_token(key, user):
    payload = {
        'key': _hash_key(key),
        'exp': datetime.utcnow() + timedelta(minutes=getattr(settings, 'JWT_VALIDITY_TIME', 60)),
        'email': user.email,
    }

    return jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')


def _hash_key(key):
    return sha512(key.encode()).hexdigest()
