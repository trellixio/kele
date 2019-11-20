import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from event.auth.models import AuthToken
from event.xlib.utils import check_key, generate_token


class EventTokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'
    model = AuthToken

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Invalid username/password.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid username/password.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = 'Invalid username/password.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_header(self, request):
        return self.keyword

    def authenticate_credentials(self, token):
        try:
            payload = jwt.decode(token, settings.JWT_SECRET)
        except (jwt.ExpiredSignatureError, jwt.DecodeError):
            msg = 'Invalid username/password'
            raise exceptions.AuthenticationFailed(msg)

        user_model = get_user_model()

        try:
            user = user_model.objects.get(email=payload['email'])
        except user_model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        key = user.auth_token.key

        if not check_key(key, payload['key']):
            raise exceptions.AuthenticationFailed('Invalid username/password.')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return user, generate_token(key, user)

    def get_auth_token(self, user):
        auth_token = self.model.objects.filter(user=user).first()

        if not auth_token:
            auth_token = self.model.objects.create(user=user)

        return generate_token(auth_token.key, user)
