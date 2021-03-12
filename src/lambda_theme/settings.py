"""
Settings for ----- are all namespaced in the LAMBDA_THEME setting.
For example your project's `settings.py` file might look like this:

LAMBDA_THEME = {}

This module provides the `theme_settings` object, that is used to access
REST framework settings, checking for user settings first, then falling
back to the defaults.
"""
from django.conf import settings
from django.utils.module_loading import import_string
from django.test.signals import setting_changed

# TODO: merge dict settings so the user doesnt need to specify the whole dict

DEFAULTS = {
    'THEME': 'default',
    'PARSE_TAG': '@',
    'FORM_RENDERER_PARAMS': {
        'DIRS': [],
        'NAME': 'djangoforms',
        'APP_DIRS': True,
        'OPTIONS': {
            'builtins': ['lambda_theme.builtins'],
        },
    },
    'DEFAULT_THEME': 'default',
    'DEFAULT_THEME_DIR': 'lambda_theme',
    'DEFAULT_COMPONENTS': [],
    'DEFAULT_TAGS': [],
    'DEFAULT_INCLUSION_TAGS': [],
    'DEFAULT_FILTERS': [],
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = [
    'DEFAULT_COMPONENTS',
    'DEFAULT_TAGS',
    'DEFAULT_INCLUSION_TAGS',
    'DEFAULT_FILTERS',
]

REMOVED_SETTINGS = []

SETTINGS_DOC = None  # "https://www.django-rest-framework.org/api-guide/settings/"


def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        print("FOO")
        if isinstance(val, (list, tuple)):
            return import_string(val[0]), *val[1:]
        return import_string(val)
    except ImportError as e:
        msg = "Could not import '%s' for API setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)
    except (SyntaxError, Exception) as ex:
        print(str(ex), val, setting_name)
        pass


class ThemeSettings:

    def __init__(self, user_settings: dict = None, defaults: dict = None, import_strings: list = None):
        if user_settings:
            self._user_settings = self.__check_user_settings(user_settings)
        self.defaults = defaults or DEFAULTS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'LAMBDA_THEME', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if attr in self.import_strings:
            val = perform_import(val, attr)

        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    # noinspection PyMethodMayBeStatic
    def __check_user_settings(self, user_settings):
        for setting in REMOVED_SETTINGS:
            if setting in user_settings:
                raise RuntimeError(
                    f'The {setting} setting has been removed. '
                    f'Please refer to {SETTINGS_DOC} for available settings.'
                )
        return user_settings

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, '_user_settings'):
            delattr(self, '_user_settings')


theme_settings = ThemeSettings(None, DEFAULTS, IMPORT_STRINGS)


def reload_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting == 'LAMBDA_THEME':
        print(f'Reloading: {setting}')
        theme_settings.reload()


setting_changed.connect(reload_settings)
