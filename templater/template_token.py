
class TemplateToken (object):
  def __init__(self, token_str):
    self.is_simple = True
    self.opt = False
    self.optline = False
    self.template = None

    # Shouldn't need a flag for this: if a list is provided as an object, templater should figure it out.
    # self.repeats = False

    ps = token_str.split('|')
    self.obj = ps[-1]
    for p in ps[:-1]:
      if p == 'opt':
        self.opt = True
      elif p == 'optline':
        self.optline = True
      elif p.startswith('tmp:'):
        self.template = p[4:]
        self.is_simple = False
