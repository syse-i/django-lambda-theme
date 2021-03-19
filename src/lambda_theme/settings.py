"""
Settings for ----- are all namespaced in the LAMBDA_THEME setting.
For example your project's `settings.py` file might look like this:

LAMBDA_THEME = {}

This module provides the `theme_settings` object, that is used to access
REST framework settings, checking for user settings first, then falling
back to the defaults.
"""
from django.conf import settings

THEME = getattr(settings, 'LAMBDA_THEME', 'default')
THEME_DIR = getattr(settings, 'LAMBDA_THEME_DIR', 'lambda_theme')
PARSE_TAG = getattr(settings, 'LAMBDA_THEME_PARSE_TAG', '@')
FALLBACK_THEME = getattr(settings, 'LAMBDA_THEME_FALLBACK_THEME', 'default')
