from django.template.base import TemplateSyntaxError
from django.template.loader_tags import construct_relative_path, ExtendsNode

from .. import template
from ..helpers import parse_template_name, get_template_name

register = template.Library()


class CustomExtendsNode(ExtendsNode):

    def find_template(self, template_name, context):
        """
        This is a wrapper around engine.find_template(). A history is kept in
        the render_context attribute between successive extends calls and
        passed as the skip argument. This enables extends to work recursively
        without extending the same template twice.
        """
        template_name, parsed = parse_template_name(template_name)
        if parsed:
            template_name = get_template_name(template_name)
        return super().find_template(template_name, context)


@register.tag('extends')
def do_extends(parser, token):
    """
    Signal that this template extends a parent template.

    This tag may be used in two ways: ``{% extends "base" %}`` (with quotes)
    uses the literal value "base" as the name of the parent template to extend,
    or ``{% extends variable %}`` uses the value of ``variable`` as either the
    name of the parent template to extend (if it evaluates to a string) or as
    the parent template itself (if it evaluates to a Template object).
    """
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError("'%s' takes one argument" % bits[0])
    bits[1] = construct_relative_path(parser.origin.template_name, bits[1])
    parent_name = parser.compile_filter(bits[1])
    nodelist = parser.parse()
    if nodelist.get_nodes_by_type(ExtendsNode):
        raise TemplateSyntaxError("'%s' cannot appear more than once in the same template" % bits[0])
    return CustomExtendsNode(nodelist, parent_name)
