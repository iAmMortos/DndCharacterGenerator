
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
    # If template_str is not provided, attempt to look up from class of given object
    template_name = template_str
    if not template_name:
      obj_clazz = fully_qualified_name(o)
      template_name = self.template_properties.get(obj_clazz)
      if not template_name:
        raise Exception(f"No valid template found for template [{template_name}]")
    template = self.template_manager.get_template(template_name)
    tokens = self.tokenizer.tokenize(template)
    for token in tokens:
      if type(token) is str:  # is a raw string straight from the template
        output += token
      else:  # token is Token object
        # resolve the value lookup
          # determine type: simple string? object? list?
        # determine visibility
          # if not visible, check if optline
        # determine text value
          # if template reference, recursively resolve string before continuing
          # add prefix, suffix
          # if list, use specified delimiter
        if token.valueref == 'this':
          if not token.template:
            raise Exception("Cannot use a self reference without also specifying a template")
          output += self.make(o, token.template)
        else:
          token.value = obj_utils.get_value(o, token.valueref)
          if token.is_finished:
            output += token.value
          else:
            output += self.make()

    return output  # obj_utils.get_value(template, o)


