from .. import template

from lambda_theme.components import Alert, Link, Button
from lambda_theme.tags import form_render, form_errors, form_field, form_fields, formset_render, message, messages
from lambda_theme.filters import is_checkbox

register = template.Library()

# Components
register.tag('alert', Alert)
register.tag('link', Link)
register.tag('button', Button)

# Tags
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
# noinspection PyUnresolvedReferences
register.inclusion_tag('@/tags/message.html')(message)
# noinspection PyUnresolvedReferences
register.inclusion_tag('@/tags/messages.html', takes_context=True)(messages)

# Filters
register.filter(is_checkbox)
