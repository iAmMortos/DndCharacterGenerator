
from templater.template_manager import TemplateManager
from templater.template_token import  TemplateToken
from templater.output_formats import OutputFormats
from templater.subtool import Subtool
from templater.templater_utils import subappend, subappendlist


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
    while len(sublist) > 1 or type(sublist[0]) is not str:
      newsublist = []
      for sub in sublist:
        if type(sub) is str:
          subappend(newsublist, sub)
        elif type(sub) is TemplateToken:
          if sub.template:
            tmp = self.template_manager.get_template(sub.template)
            sublist = self.subtool.sub(tmp, sub.obj)
            subappendlist(newsublist, sublist)
          else:
            pass
          # get template from token
          # do subs to get newsubs OR plain string replacement
          # do opt and optline parsing
          # append newsubs to newsublist
        else:
          raise TypeError(f"Unexpected type found in sublist: [{type(sub)}]")
      sublist = newsublist

    if len(sublist) == 1 and type(sublist[0]) is str:
      return sublist[0]
    return sublist
