
class XmlEntity (object):
  def __init__(self, xml_node):
    self._data = {}
    for c in xml_node.getchildren():
      if c.tag in self._data:
        print(c.tag)
      elif c.text is not None:
        self._data[c.tag] = c.text

  def _get(self, key, default_value=None):
    return default_value if key not in self._data else self._data[key]

  def _get_as_obj(self, key, cls, default_value=None):
    if key in self._keys:
      return cls(self._data[key])
    else:
      return default_value

  def _get_as_bool(self, key, default_value=False):
    if key in self._keys:
      return bool(self._data[key] == "YES")
    else:
      return default_value

  def _get_as_list(self, key, sep=',', strip=True, fn=lambda a: a, default_value=[]):
    if key in self._keys:
      return [fn(a.strip() if strip else a) for a in self._data[key].split(sep)]
    else:
      return default_value

  @property
  def _keys(self):
    return self._data.keys()
