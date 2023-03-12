
from templater.subtemplates import SubTemplates


class TemplateToken (object):
  ESC_PIPE = '{{ESC_PIPE}}'
  def __init__(self, token_str):
    self.opt = False
    self.optline = False
    self.template = None
    self.value = None
    self.prefix = ""
    self.suffix = ""

    # Shouldn't need a flag for this: if a list is provided as an object, templater should figure it out.
    # self.repeats = False

    
    ps = token_str.replace('\\|', self.ESC_PIPE).split('|')
    self.obj = ps[-1].replace(self.ESC_PIPE, '|')
    for pt in ps[:-1]:
      p = pt.replace(self.ESC_PIPE, '|')
      if p == 'opt':
        self.opt = True
      elif p == 'optline':
        self.optline = True
      elif ':' in p:
        if p.startswith('temp:'):
          self.template = SubTemplates.of(p[5:])
        elif p.startswith('pref:'):
          self.prefix = p[5:]
        elif p.startswith('suff:'):
          self.suffix = p[5:]
        else:
          raise Exception(f"Unrecogniezd flag in [{p}]")

