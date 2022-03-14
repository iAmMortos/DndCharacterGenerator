
from enum import Enum


class TodoStatus(Enum):
  DONE = 'X'
  TODO = ' '
  INCON = '-'
  URGENT = '!'
  

class TodoNode (object):
  def __init__(self, text, status=TodoStatus.TODO, parent=None):
    self.is_root = parent is None
    self.parent = parent
    self.children = []
    self.text = text
    self.status = status
  
  def add_child(self, node):
    self.children.append(node)
    
  def check(self):
    self.status = TodoStatus.DONE
    
  def uncheck(self):
    self.status = TodoStatus.TODO
  
  def set_status(self, status):
    self.status = status
  
