
from templater.template_manager import TemplateManager
from templater.tokens.tokenizer import Tokenizer


class Templater (object):
  def __init__(self, output_type, config_path='templater/config/application.properties'):
    self.output_type = output_type
    self.template_manager = TemplateManager(self.output_type)
    self.tokenizer = Tokenizer()

  def make(self, o):
    obj_type = type(o)


