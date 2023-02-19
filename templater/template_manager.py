
import io

from templater.output_formats import OutputFormats

from model.spell import Spell
from model.monster import Monster


class UnsupportedFormatException (Exception):
  def __init__(self, fstr):
    super().__init__(f'TemplateManager does not support output format [{fstr}].')


class NoSuchTemplateException(Exception):
  def __init__(self, typ, output):
    super().__init__(f'Template not yet supported for type [{typ}] of format [{output}].')


def _load(path):
  with io.open(path, encoding='utf-8') as f:
    return f.read()


class TemplateManager (object):
  def __init__(self, output_format):
    self.output_format = output_format
    self._format_map = {
      OutputFormats.html: {
      },
      OutputFormats.md: {
        Spell: 'templater/templates/markdown/spell.md',
        Monster: 'templater/templates/markdown/statblock.md'
      }
    }

  @property
  def output_format(self):
    return self._output_format

  @output_format.setter
  def output_format(self, val):
    if val not in OutputFormats:
      raise UnsupportedFormatException(val)
    self._output_format = val

  def get_template(self, obj_or_str):
    t = type(obj_or_str)
    if t is str:
      
    output = ''

    if self.output_format in self._format_map:
      opf = self._format_map[self.output_format]
      if t in opf:
        output = _load(opf[t])
      else:
        raise NoSuchTemplateException(t, self.output_format)
    else:
      # should never get here, as unsupported formats are handled when setting self.output_format
      raise Exception("Impossible State")

    return output
