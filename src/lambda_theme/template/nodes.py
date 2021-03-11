from component_tags.template.nodes import ComponentNode as BaseComponentNode

from ..helpers import get_template_name_list

__all__ = ['ComponentNode']


class ComponentNode(BaseComponentNode):

    def get_template_name(self, context):
        template_name = self._meta.template_name
        if not template_name:
            raise self.TemplateIsNull('Template is undefined')
        template_name_list = get_template_name_list(template_name)
        return context.template.engine.select_template(template_name_list)
