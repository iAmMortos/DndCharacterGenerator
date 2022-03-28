import ui
from notes.view.todo_line_view import TodoLineView


class TodoView(ui.View):
  def __init__(self, file=None):
    self.sv = ui.ScrollView()
    self.sv.frame = self.frame
    self.sv.flex = 'WH'
    self.add_subview(self.sv)
    self.background_color = 'black'
    
    for i in range (100):
      ln = TodoLineView()
      ln.x = 0
      ln.y = i * 16
      ln.width = self.width
      self.sv.add_subview(ln)
    self.sv.content_size = (400, 1600)
    

if __name__ == '__main__':
  tv = TodoView()
  tv.present(style='fullscreen')
