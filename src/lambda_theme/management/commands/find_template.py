# -*- coding: utf-8 -*-
import sys

from django.core.management.base import LabelCommand
from django.template import TemplateDoesNotExist, loader


class Command(LabelCommand):
    help = "Finds the location of the given template by resolving its path"
    args = "[template_path]"
    label = 'template path'

    def handle_label(self, template_path, **options):
        try:
            template = loader.get_template(template_path).template
        except TemplateDoesNotExist:
            sys.stderr.write("No template found\n")
        else:
            sys.stdout.write(self.style.SUCCESS((template.name)))
