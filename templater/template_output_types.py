
from enum import Enum


class TemplateOutputTypes (Enum):
  html = 'html'
  markdown = 'markdown'
  
  def __str__(self):
    return self.name

      
if __name__ == '__main__':
  t = TemplateOutputTypes('html')
  print(t)
  t = TemplateOutputTypes('markdown')
  print(t)
  try:
    t = TemplateOutputTypes('failure')
  except ValueError:
    print(f'"failure" is not a valid type')
  
