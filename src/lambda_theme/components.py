from . import template

__all__ = [
    'Alert',
    'Link',
    'Button',
]


class Alert(template.Component):
    role = template.ContextAttribute(default='alert')

    class Meta:
        template_name = '@/tags/alert.html'


class Link(template.Component):
    href = template.ContextAttribute(default='#')

    class Meta:
        template_name = '@/tags/link.html'


class Button(template.Component):
    class TypeChoices(template.AttributeChoices):
        button = 'button'
        reset = 'reset'
        submit = 'submit'

    type = template.Attribute(choices=TypeChoices, default=TypeChoices.submit)
    click = template.Attribute(name='@click')
    disabled = template.Attribute(default=False)

    href = template.ContextAttribute(default='#')

    class Meta:
        template_name = '@/tags/button.html'
