import ui
from utils import dpr_calc

class DPRToolView(ui.View):
  def __init__(self):
    pass
  def init(self):
    self.name = 'Damage Per Round Tool'
  def did_load(self):
    pass
  @staticmethod
  def load_view():
    v = ui.load_view()
    v.init()
    return v
