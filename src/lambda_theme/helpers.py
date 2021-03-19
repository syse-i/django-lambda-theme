from pathlib import Path
from typing import Tuple, List

from django.template.loader import select_template as _select_template
from .settings import THEME, THEME_DIR, FALLBACK_THEME, PARSE_TAG

__all__ = [
    'get_template_name',
    'parse_template_name',
    'get_template_name_list',
    'select_template',
]


def get_template_name(template_name: str, theme_name: str = THEME) -> str:
    return str(Path(THEME_DIR, theme_name, template_name))


def get_fallback_template_name(template_name: str, theme_name: str = FALLBACK_THEME) -> str:
    return get_template_name(template_name, theme_name)


def parse_template_name(template_name: str, parse_tag: str = PARSE_TAG) -> Tuple[str, bool]:
    if parse_tag in template_name:
        parse_name = template_name.split(parse_tag)[-1]
        return "".join(parse_name[1:]) if parse_name.startswith('/') else parse_name, True
    return template_name, False


def get_template_name_list(template_name) -> List[str]:
    template_name, parsed = parse_template_name(template_name)
    return [template_name, get_template_name(template_name), get_fallback_template_name(template_name)]


def select_template(template_name, using=None):
    return _select_template(get_template_name_list(template_name), using)
