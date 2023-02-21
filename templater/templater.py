
from templater.template_manager import TemplateManager
from templater.template_token import  TemplateToken
from templater.output_formats import OutputFormats
from templater.subtool import Subtool


class Templater (object):

  def __init__(self, output_format):
    self.template_manager = TemplateManager(output_format)
    self.subtool = Subtool()

  @property
  def output_format(self):
    return self.template_manager.output_format

  @output_format.setter
  def output_format(self, output_format):
    self.template_manager.output_format = output_format

  def make(self, obj):
    tmp = self.template_manager.get_template(obj)
    sublist = self.subtool.sub(tmp, obj)
    while len(sublist) > 1:
      for sub in sublist:
        if type(sub) is TemplateToken:
          tmp = self.template_manager.get_template(sub.)
    return sublist
