

class Token (object):
  def __init__(self, valueref, flags):
    self._value = None
    self.valueref = valueref
    self.prefix = self._set_flag(flags, ['prefix', 'pref', 'p'], '')
    self.suffix = self._set_flag(flags, ['suffix', 'suff', 's'], '')
    self.delimiter = self._set_flag(flags, ['delimiter', 'del', 'd'], ', ')
    self.template = self._set_flag(flags, ['template', 'temp', 't'])
    self.optline = self._set_bool_flag(flags, ['optline', 'o'])
    self.showif = self._set_flag(flags, ['showif', 'if'])
    self.nullval = self._set_flag(flags, ['nullval', 'nv'])
    self.nonnullval = self._set_flag(flags, ['nonnullval', 'nnv'])
    self.regextemplate = self._set_flag(flags, ['regextemplate', 'regextemp', 'rtemp', 'rt'])
    
  def _set_flag(self, flags, keys, default_val=None):
    for key in keys:
      if key in flags:
        return flags[key]
    return default_val
    
  def _set_bool_flag(self, flags, keys):
    for key in keys:
      if key in flags:
        return True
    return False

  @property
  def value(self):
    is_null = self._value is None
    if self.nonnullval and not is_null:
      return f'{self.prefix}{self.nonnullval}{self.suffix}'
    elif self.nullval and is_null:
      return f'{self.prefix}{self.nullval}{self.suffix}'
    elif is_null:
      return ''
    else:
      return f'{self.prefix}{self._value}{self.suffix}'

  @value.setter
  def value(self, val):
    if val is None:
      self._value = None
    elif type(val) is list:
      if len(val) == 0:
        self._value = None
      else:
        self._value = val
    elif type(val) is str:
      if val == '':
        self._value = None
      else:
        self._value = val
    else:  # is likely an object
      self._value = val

  @property
  def is_visible(self):
    return self.value != ''
    
  @property
  def is_reference(self):
    return self.template or self.regextemplate
  
