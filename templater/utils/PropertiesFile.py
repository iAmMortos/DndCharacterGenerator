
import os


class PropertiesFile (object):
  def __init__(self, path):
    self.path = path
    os.path.exists(path)

