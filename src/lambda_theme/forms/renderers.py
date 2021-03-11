from django.forms.renderers import DjangoTemplates, ROOT
from django.utils.functional import cached_property

from ..settings import theme_settings


class FormRenderer(DjangoTemplates):

    @cached_property
    def engine(self):
        params = theme_settings.FORM_RENDERER_PARAMS
        params['DIRS'].append(ROOT / self.backend.app_dirname)
        return self.backend(params)
