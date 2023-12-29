
from templater import TemplateTypes


class TemplateManager (object):
  # knows what kind of templates there are, how to find them.
  def __init__(self, template_type):
    self.type = template_type
    
