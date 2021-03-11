import os

from django.template.loader import select_template as _select_template

from .settings import theme_settings

__all__ = [
    'get_template_name',
    'parse_template_name',
    'get_template_name_list',
    'select_template',
]


def get_template_name(template_name: str, theme_name: str = theme_settings.THEME):
    return os.path.join(theme_settings.DEFAULT_THEME_DIR, theme_name, template_name)


def get_fallback_template_name(template_name: str, theme_name: str = theme_settings.DEFAULT_THEME):
    return get_template_name(template_name, theme_name)


def parse_template_name(template_name: str, parse_tag: str = theme_settings.PARSE_TAG):
    if parse_tag in template_name:
        parse_name = template_name.split(parse_tag)[-1]
        return "".join(parse_name[1:]) if parse_name.startswith('/') else parse_name, True
    return template_name, False


def get_template_name_list(template_name):
    template_name, parsed = parse_template_name(template_name)
    return [template_name, get_template_name(template_name), get_fallback_template_name(template_name)]


def select_template(template_name, using=None):
    return _select_template(get_template_name_list(template_name), using)


# from django.utils.module_loading import import_string
# def get_form(form_name, as_string=False):
#     if as_string:
#         return '{module}.{form}'.format(module=MODULE_NAME, form=form_name)
#     return getattr(import_module(MODULE_NAME), form_name)
