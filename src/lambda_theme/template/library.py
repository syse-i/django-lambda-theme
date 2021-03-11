from component_tags.template.library import Library as BaseLibrary

from ..helpers import get_template_name_list
from ..settings import theme_settings


class Library(BaseLibrary):

    def __init__(self):
        super().__init__()

        for component in theme_settings.DEFAULT_COMPONENTS:
            name = component.__name__.lower()
            self.tag(name, component)

        for tag_func in theme_settings.DEFAULT_INCLUSION_TAGS:
            kwargs = {}
            if isinstance(tag_func, tuple):
                tag_func, kwargs = tag_func

            name = kwargs.get('name', tag_func.__name__)
            filename = kwargs.get('filename', f'@/tags/{name}.html')
            takes_context = kwargs.get('takes_context', False)
            self.inclusion_tag(filename=filename, name=name, takes_context=takes_context)(tag_func)

        for filter_func in theme_settings.DEFAULT_FILTERS:
            name = filter_func.__name__
            self.filter(name, filter_func)

    def inclusion_tag(self, filename, func=None, takes_context=False, name=None):
        filename = get_template_name_list(filename)
        return super().inclusion_tag(filename, func, takes_context, name)
