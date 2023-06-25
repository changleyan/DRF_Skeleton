# -*- coding: utf-8 -*-
from datetime import timedelta
from django.utils import timezone
from oauth2_provider import models
from oauth2_provider.settings import oauth2_settings
from oauthlib import common


def oauth2_login(user, client_id):
    Application = models.get_application_model()
    RefreshToken = models.get_refresh_token_model()
    AccessToken = models.get_access_token_model()

    application = Application.objects.get(client_id=client_id)
    expires_in = oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS
    expires = timezone.now() + timedelta(seconds=expires_in)
    access_token = AccessToken(
        user=user,
        scope='read write',
        expires=expires,
        token=common.generate_token(),
        application=application
    )
    access_token.save()
    refresh_token = RefreshToken(
        user=user,
        token=common.generate_token(),
        application=application,
        access_token=access_token
    )
    refresh_token.save()

    data = {
        'username': user.username,
        'token_type': 'Bearer',
        'access_token': access_token.token,
        'scope': 'read write',
        'expires_in': expires_in,
        'refresh_token': refresh_token.token,
    }

    return data