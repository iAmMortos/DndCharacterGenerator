
from templater.utils.properties_file import PropertiesFile
from templater.tokens.token import Token
from templater.tokens.tokenizing_error import TokenizingError


class Tokenizer (object):
  def __init__(self, token_config_path='templater/config/token.properties'):
    self.properties = PropertiesFile(token_config_path)
    self._token_start = self.properties.get('start')
    self._token_end = self.properties.get('end')
    self._token_delimiter = self.properties.get('delimiter')
    self._token_flag_setter = self.properties.get('flag_setter')
    
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
          rs = rs[i + len(self._token_end):]
          open = False
        else:
          raise TokenizingError("Unclosed Token")
    return out

  def _parse_token_content(self, s):
    parts = s.split(self._token_delimiter)
    value = parts[0]
    flags = {}
    for part in parts[1:]:
      if self._token_flag_setter in part:
        key, val = part.split(self._token_flag_setter)
        flags[key] = val
      else:
        flags[key] = None

    return Token(value, flags)

    
if __name__ == '__main__':
  pass
  
