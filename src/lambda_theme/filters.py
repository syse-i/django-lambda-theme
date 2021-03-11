from django.forms import CheckboxInput


def is_checkbox(bound_field):
    try:
        return isinstance(bound_field.field.widget, CheckboxInput)
    except AttributeError:
        return False
