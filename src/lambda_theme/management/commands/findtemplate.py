# -*- coding: utf-8 -*-
import sys

from django.core.management.base import LabelCommand
from django.template import loader
from django.template.exceptions import TemplateDoesNotExist

from ...helpers import get_template_name_list


class Command(LabelCommand):
    help = "Finds the location of the given template by resolving its path"
    args = "[template_path]"
    label = 'template path'

    def handle_label(self, template_path, **options):
        try:
            template_name_list = get_template_name_list(template_path)
            template = loader.select_template(template_name_list).template
        except TemplateDoesNotExist:
            sys.stderr.write("No template found\n")
        else:
            sys.stdout.write(template.name)
