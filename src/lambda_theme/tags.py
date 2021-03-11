from component_tags.template.context import TagContext


def formset_render(instance, method='POST', **attributes):
    context = TagContext(attributes)
    context['formset'] = instance
    context['method'] = method
    return context.flatten()


def messages(context, **attributes):
    context = TagContext(attributes, initial=context)
    return context.flatten()


def message(instance, **attributes):
    context = TagContext(attributes)
    context['body'] = instance
    return context.flatten()


def form_field(field, show_label=True, **attributes):
    context = TagContext(attributes)
    context['field'] = field
    context['show_label'] = show_label

    try:
        if field.name == 'DELETE':
            context.add_class('delete-field')
    except AttributeError:
        pass

    return context.flatten()


def form_fields(form, legend=None, **attributes):
    context = TagContext(attributes)
    context['form'] = form
    context['legend'] = legend
    return context.flatten()


def form_errors(instance, **attributes):
    context = TagContext(attributes)
    context['form'] = instance
    return context.flatten()


def form_render(*forms, method='POST', **attributes):
    context = TagContext(attributes)
    context['forms'] = forms
    context['method'] = method
    return context.flatten()
