
from enum import Enum


class TemplateTypes (Enum):
  html='html'
  markdown='markdown'
  
  def __repr__(self):
    return self.name()
  
  @staticmethod
  def of(s):
    try:
      t = TemplateTypes(s)
      return t
    except:
      raise Exception(f"Invalid template type [{s}], value options are: {[t.name for t in TemplateTypes]}")
      
      
if __name__ == '__main__':
  t = TemplateTypes.of('html')
  t = TemplateTypes.of('markdown')
  t = TemplateTypes.of('failure')
  
