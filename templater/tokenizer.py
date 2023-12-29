
# from templater.utils.properties_file import PropertiesFile


class Tokenizer (object):
  def __init__(self):
    # self.properties = PropertiesFile('templater/config/application.properties')
    self.token_start = '{'  # self.properties.get('token_start')
    self.token_end = '}'  # self.properties.get('token_end')
    self.token_delimiter = '|'  # self.properties.get('token_delimiter')
    
  def tokenize(self, s):
    out = []
    rs = s
    open = False
    while len(rs) > 0:
      if not open:
        i = rs.find(self.token_start)
        if i >= 0:
          
      else:
        i = rs.find(self.token_end)
    return out
    
    
if __name__ == '__main__':
  pass
  
