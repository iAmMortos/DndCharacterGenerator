
import sharedlibs
sharedlibs.add_path_for('config_file')
from config_file import ConfigFile

from notes.notes_config import get_config

class Session (object):
  def __init__(self, num=None, date=None, title=None):
    if num or date or title:
      self.number = num
      self.date = date
      self.title = title
    else:
      self._notecfg = get_config()
      base = self._notecfg.get('base')
      sesh = self._notecfg.get('session_src')
      path = f'{base}{sesh}'
      self._seshcfg = ConfigFile(path)
      self.number = int(self._seshcfg.get('num'))
      self.date = self._seshcfg.get('date')
      self.title = self._seshcfg.get('title')
