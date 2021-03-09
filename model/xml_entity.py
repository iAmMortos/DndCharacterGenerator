
import xml.etree.ElementTree as ET


class _X (object):
  def __init__(self,a,d):
    self.a = a
    self.d = d


# TODO: each individual c from xml_node should technically be wrapped in an _X object to preserve the attribute
# of each.
class XmlEntity (object):
  def __init__(self, xml_node):
    self._data = {}
    self._node = xml_node
    self._attrib = xml_node.attrib
    for c in xml_node.getchildren():
      if len(c.getchildren()) == 0:
        # child is a text leaf
        if c.tag in self._data:
          if type(self._data[c.tag].d) is not list:
            self._data[c.tag].d = [self._data[c.tag].d]
          self._data[c.tag].d += [c.text]
        elif c.text is not None:
          self._data[c.tag] = _X(c.attrib,c.text)
      else:
        # child is another XmlEntity
        if c.tag in self._data:
          if type(self._data[c.tag].d) is not list:
            self._data[c.tag].d = [self._data[c.tag].d]
          self._data[c.tag].d += [c]
        elif c.text is not None:
          self._data[c.tag] = _X(c.attrib, c)

  def _get(self, key, default_value=None):
    return default_value if key not in self._data else self._data[key].d
    
  def _get_attrib(self, key):
    return {} if key not in self._data else self._data[key].a

  def _get_as_obj(self, key, cls, default_value=None):
    if key in self._keys:
      if type(self._data[key].d) is list:
        return [cls(e) for e in self._data[key].d]
      else:
        return cls(self._data[key].d)
    else:
      return default_value
      
  def _get_as_obj_list(self, key, cls, default_value=[]):
    obj = self._get_as_obj(key, cls, default_value)
    if type(obj) is list:
      return obj
    else:
      return [obj]

  def _get_as_bool(self, key, default_value=False):
    if key in self._keys:
      return bool(self._data[key].d in ["YES", "1"])
    else:
      return default_value

  def _get_as_list(self, key, sep=',', strip=True, fn=lambda a: a, default_value=[]):
    if key in self._keys:
      return [fn(a.strip() if strip else a) for a in self._data[key].d.split(sep)]
    else:
      return default_value

  def _get_xml(self):
    return ET.tostring(self._node, encoding='utf8')

  @property
  def _keys(self):
    return self._data.keys()
