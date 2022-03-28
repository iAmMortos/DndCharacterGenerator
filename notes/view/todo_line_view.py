import ui
from notes.todo_node import TodoStatus

class TodoLineView(ui.View):
  def __init__(self, indent_lvl=0, text='', state=TodoStatus.TODO):
    self.border_width=1
    self.border_color = 'blue'
    self.height = 16
    self.flex = 'W'
    self.lbl = ui.Label()
    self.lbl.text = 'Hello World'
    self.lbl.font = ('DejaVu Sans Mono', 12)
    self.lbl.frame = (2,2,400,16)
    self.lbl.text_color = '#64c800'
    self.add_subview(self.lbl)
