# -*- coding: utf-8 -*-
from django.apps import apps
from django.conf import settings

from common.utils import utils
from apps.core.models.logs.RegistroAccion import RegistroAccion
import json


class AccessLogMiddleware(object):
    """You must define settings.ACTIVITY_LOG to active this logging middleware.
        Example: ACTIVITY_LOG = '__all__' will log all model accesses.
        ACTIVITY_LOG = ('MyModel', 'MyOtherModel', ) will log only these models."""

    def __init__(self, get_response):
        if not settings.ACTIVITY_LOG:
            raise Exception('You must define settings.ACTIVITY_LOG to enable this logging middleware.')

        try:
            self.get_response = get_response
        except Exception as e:
            print(e)
        # self.get_response = get_response

        app_config = apps.get_app_config('core')
        self.app_models = app_config.get_models(False, False)
        if settings.ACTIVITY_LOG == '__all__':
            self.models = [model for model in self.app_models if model is not RegistroAccion]
        else:
            self.models = []
            for str_model in settings.ACTIVITY_LOG:
                if str_model == 'Access':
                    continue
                else:
                    model = app_config.get_model(str_model)
                    self.models.append(model)

    def __call__(self, request):
        body_unicode = ''
        try:
            if request.content_type == 'application/json':
                body_unicode = request.body.decode('utf-8')

            response = self.get_response(request)

        except Exception as e:
            print(e)

        if response.status_code < 200 or response.status_code >= 300:
            return response

        method = request.method.upper()

        if method in 'POST':
            action = 'CREATE'
        elif method == 'DELETE':
            action = 'DELETE'
        elif method in ['PUT', 'PATCH']:
            action = 'UPDATE'
        else:
            return response

        user = request.user
        if not user:
            username = 'AnonymousUser'
        else:
            username = user.username or 'AnonymousUser'

        ip = utils.get_client_ip(request)
        url = request.path

        if url == '/o/token/':
            return response

        url_list = url.split('/')

        model = ''
        if len(url_list) > 2:
            model = url_list[2]

        tz = ''

        if request.content_type == 'application/json':
            body_data = body_unicode
        else:
            body_data = request.POST
            body_data = json.dumps(body_data)

        RegistroAccion(usuario=username,
                       ip=ip,
                       url=url,
                       accion=action,
                       tz=tz,
                       datos=body_data,
                       modelo=model).save()

        return response
