
from templater.utils.properties_file import PropertiesFile
from templater.template_manager import TemplateManager
from templater.template_output_types import TemplateOutputTypes


class Templater (object):
  def __init__(self, output_type, config_path='templater/config/application.properties'):
    self.output_type = TemplateOutputTypes(output_type)
    self.template_manager = TemplateManager(self.output_type)
    self.properties = PropertiesFile(config_path)

  @property
  def _token_start(self):
    return self.properties.get('token_start')

  @property
  def _token_end(self):
    return self.properties.get('token_end')

  @property
  def _token_delimiter(self):
    return self.properties.get('token_delimiter')

  def make(self, o):
    pass


