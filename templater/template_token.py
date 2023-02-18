
class TemplateToken (object):
  def __init__(self, template, obj, repeats=False):
    self.template = template
    self.obj = obj
    self.repeats = repeats
