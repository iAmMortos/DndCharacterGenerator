
import xml.etree.ElementTree as ET
import csv
import io
import os


class DataFileLoader (object):

  def __init__(self, data_path="data/", compendium_path="data/xml/"):
    self._data_path = data_path
    self._compendium_path = compendium_path

  def _build_path_for(self, base, name, ext=''):
    return f'{self._data_path}{name}.{ext}';

  def load_csv(self, data_name, delimiter=',', quotechar='"'):
    path = self._build_path_for(self._data_path, data_name, 'csv')
    out = []
    with io.open(path, mode='r', newline='', encoding='utf-8') as csvfile:
      rdr = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
      for row in rdr:
        out += [row]
    return out

  def load_compendium_xml(self, data_name):
    file = self._build_path_for(self._compendium_path, data_name, ext='xml')
    tree = ET.parse(file)
    return tree.getroot()
