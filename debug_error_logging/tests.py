# -*- coding: utf-8 -*-
# (c) 2012 Bright Interactive Limited. All rights reserved.
# http://www.bright-interactive.com | info@bright-interactive.com

# No tests because I couldn't manage to construct a failing test. Django sets
# DEBUG = False when running tests and even if it is manually changed to True
# in a test's setUp method then errors are still logged to
# logging.getLogger('django.request') (unlike when DEBUG = True when running
# a Django app in development mode).
