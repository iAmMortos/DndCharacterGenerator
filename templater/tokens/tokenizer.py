
from templater.utils.properties_file import PropertiesFile
from templater.tokens.token import Token
from templater.tokens.tokenizing_error import TokenizingError


class Tokenizer (object):
  def __init__(self):
    self.properties = PropertiesFile('templater/config/application.properties')
    self._token_start = self.properties.get('token_start')
    self._token_end = self.properties.get('token_end')
    self._token_delimiter = self.properties.get('token_delimiter')
    self._token_flag_setter = self.properties.get('token_flag_setter')
    
  def tokenize(self, s):
    out = []
    rs = s
    open = False
    while len(rs) > 0:
      if not open:
        i = rs.find(self._token_start)
        if i >= 0:
          if i > 0:
            out += [rs[:i]]
          rs = rs[i+len(self._token_start):]
          open = True
        else:
          out += [rs]
          rs = ''
      else:
        i = rs.find(self._token_end)
        if i >= 0:
          token = self._parse_token_content(rs[:i])
          out += [token]
          rs = rs[i + len(self._token_end)]
        else:
          raise TokenizingError("Unclosed Token")
    return out

  def _parse_token_content(self, s):
    parts = s.split(self._token_delimiter)
    value = parts[0]
    flags = {}
    for part in parts[1:]:
      key, val = part.split(self._token_flag_setter)
      flags[key] = val
    return Token(value, flags)

    
if __name__ == '__main__':
  pass
  
