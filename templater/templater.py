
from templater.utils.properties_file import PropertiesFile


class Templater (object):
  def __init__(self, config_path='templater/config/application.properties'):
    self.properties = PropertiesFile(config_path)
    print(f'{self._token_start}{self._token_delimiter}{self._token_end}')

  @property
  def _token_start(self):
    return self.properties.get('token_start')

  @property
  def _token_end(self):
    return self.properties.get('token_end')

  @ property
  def _token_delimiter(self):
    return self.properties.get('token_delimiter')

  def make(self):
    pass


