
import xml.etree.ElementTree as ET


class XmlEntity (object):
  def __init__(self, xml_node):
    self._data = {}
    self._node = xml_node
    for c in list(xml_node):
      if len(c) == 0 and c.text is None:
        # skip empty leaves
        continue
      if c.tag in self._data:
        if type(self._data[c.tag]) is not list:
          self._data[c.tag] = [self._data[c.tag]]
        self._data[c.tag] += [c]
      else:
        self._data[c.tag] = c

  def _get(self, key, default_value=None):
    if key in self._data:
      # if data at key is a list
      if type(self._data[key]) is list:
        # if the first element has no children, assume all text leaves
        if len(list(self._data[key][0])) == 0:
          # return list of string values
          return [e.text for e in self._data[key]]
        else:
          # return list of xml nodes
          return self._data[key]
      # just a single element
      else:
        # if is leaf
        if len(self._data[key]) == 0:
          # return the text value
          return self._data[key].text
        # is xml node
        else:
          # return whole node
          return self._data[key]
    else:
      return default_value
      
  def _get_as_xml(self, key, default_value=None):
    return self._data[key] if key in self._data else default_value
    
  def _get_attrib(self, key):
    xml = self._get_as_xml(key)
    if xml is not None:
      if type(xml) is list:
        return [e.attrib for e in xml]
      else:
        return xml.attrib
    else:
      return None

  def _get_as_obj(self, key, cls, default_value=None):
    if key in self._keys:
      if type(self._data[key]) is list:
        if len(self._data[key][0]) == 0:
          return [cls(e.text) for e in self._data[key]]
        else:
          return [cls(e) for e in self._data[key]]
      else:
        if len(self._data[key]) == 0:
          return cls(self._data[key].text)
        else:
          return cls(self._data[key])
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
      return bool(self._data[key].text in ["YES", "1"])
    else:
      return default_value

  def _get_as_list(self, key, sep=',', strip=True, fn=lambda a: a, default_value=[]):
    if key in self._keys:
      return [fn(a.strip() if strip else a) for a in self._data[key].text
      .split(sep)]
    else:
      return default_value
      
  @property
  def _keys(self):
    return self._data.keys()
    
  @property
  def _attrib(self):
    return self._node.attrib
    
  @property
  def _xml_str(self):
    return ET.tostring(self._node, encoding='utf8')
