
from templater.utils.properties_file import PropertiesFile
from templater.utils.class_utils import fully_qualified_name
from templater.template_manager import TemplateManager
from templater.tokens.tokenizer import Tokenizer
from templater.utils import obj_utils


class Templater (object):
  def __init__(self, output_type, token_config_path='templater/config/token.properties', template_config_path='templater/config/template.properties'):
    self.output_type = output_type
    self.template_manager = TemplateManager(self.output_type)
    self.tokenizer = Tokenizer(token_config_path)
    self.template_properties = PropertiesFile(template_config_path)

  def make(self, o, template_str=None):
    output = ''
    template_name = template_str
    if not template_name:
      obj_clazz = fully_qualified_name(o)
      template_name = self.template_properties.get(obj_clazz)
    template = self.template_manager.get_template(template_name)
    tokens = self.tokenizer.tokenize(template)
    return None  # obj_utils.get_value(template, o)


