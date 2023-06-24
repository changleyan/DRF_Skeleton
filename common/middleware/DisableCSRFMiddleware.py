# -*- coding: utf-8 -*-
from django.conf import settings


# If settings.DEBUG is True disable CSRF protection.
# This will not work in production.
class DisableCSRFMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        #if settings.DEBUG:
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        return response
