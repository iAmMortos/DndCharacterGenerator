
from templater.template_output_types import TemplateOutputTypes


class TemplateManager (object):
  # knows what kind of templates there are, how to find them.
  def __init__(self, template_type, template_dir='templater/templates'):
    self.template_dir = template_dir
    self.type = template_type
    
