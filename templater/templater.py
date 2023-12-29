
from templater.utils.properties_file import PropertiesFile


class Templater (object):
  def __init__(self, config_path='templater/config/application.properties', template_manager):
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


