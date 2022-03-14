import ui


class TodoView(ui.View):
  def __init__(self, file=None):
    self.sv = ui.ScrollView()
    self.sv.frame = self.frame
    self.sv.flex = 'WH'
    self.background_color = 'white'
    # self.add_subview
