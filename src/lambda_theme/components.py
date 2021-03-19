from . import template

__all__ = [
    'Alert',
    'Link',
    'Button',
]


class Alert(template.Component):
    role = template.Attribute(default='alert', as_context=True)

    class Meta:
        template_name = '@/tags/alert.html'


class Link(template.Component):
    href = template.Attribute(as_context=True)

    class Meta:
        template_name = '@/tags/link.html'


class Button(template.Component):
    class TypeChoices(template.AttributeChoices):
        button = 'button'
        reset = 'reset'
        submit = 'submit'

    type = template.Attribute(choices=TypeChoices, default=TypeChoices.submit)
    click = template.Attribute(context_name='@click')
    disabled = template.Attribute()

    href = template.Attribute(as_context=True)

    class Meta:
        template_name = '@/tags/button.html'
