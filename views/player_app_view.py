import ui


class PlayerAppView(ui.View):
  def __init__(self):
    pass
    
  def init(self, pc):
    pass
    
  def did_load(self):
    self.portrait = self['iv_char_portrait']
    self.name = self['iv_char_name']
    self.race_class = self['iv_char_race_class']
    
  @staticmethod
  def load_view(pc=None):
    v = ui.load_view()
    v.init(pc)
    return v
