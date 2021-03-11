from .. import template

from ..components import Alert, Link, Button
from ..tags import form_render, form_errors, form_field, form_fields, formset_render
from ..filters import is_checkbox

register = template.Library()

register.tag('alert', Alert)
register.tag('link', Link)
register.tag('button', Button)

# noinspection PyUnresolvedReferences
register.inclusion_tag('@/tags/form_render.html')(form_render)
# noinspection PyUnresolvedReferences
register.inclusion_tag('@/tags/form_errors.html')(form_errors)
# noinspection PyUnresolvedReferences
register.inclusion_tag('@/tags/form_field.html')(form_field)
# noinspection PyUnresolvedReferences
register.inclusion_tag('@/tags/form_fields.html')(form_fields)
# noinspection PyUnresolvedReferences
register.inclusion_tag('@/tags/formset_render.html')(formset_render)

register.filter(is_checkbox)
