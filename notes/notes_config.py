
import sharedlibs
sharedlibs.add_path_for('config_file')
from config_file import ConfigFile

NOTES_CONFIG_FILE = 'notes/rsc/notes.config'

def get_config():
  return ConfigFile(NOTES_CONFIG_FILE)
