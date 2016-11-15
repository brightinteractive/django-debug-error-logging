# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

from django.conf import settings

__version__ = '2.1.0'


def enable_error_logging_in_debug_mode():
    """If DEBUG = True then monkey patch the default DEBUG 500 response, so
    that we also log the errors.  (So that we can see them
    retrospectively)."""

    if settings.DEBUG:
        from django.views import debug
        import logging

        orig_technical_500_response = debug.technical_500_response

        def custom_technical_500_response(request, exc_type, exc_value, tb, status_code=None):
            """
            Create a technical server error response. The last three arguments are
            the values returned from sys.exc_info() and friends.
            """
            logger = logging.getLogger('django.request')
            logger.error('Internal Server Error: %s' % request.path,
                exc_info=(exc_type, exc_value, tb),
                extra={'status_code': 500, 'request': request}
            )
            return orig_technical_500_response(request, exc_type, exc_value, tb, status_code=status_code)

        debug.technical_500_response = custom_technical_500_response
