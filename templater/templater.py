
from templater.template_manager import TemplateManager
from templater.template_output_types import TemplateOutputTypes


class Templater (object):
  def __init__(self, output_type, config_path='templater/config/application.properties'):
    self.output_type = TemplateOutputTypes(output_type)
    self.template_manager = TemplateManager(self.output_type)

  def make(self, o):
    pass


