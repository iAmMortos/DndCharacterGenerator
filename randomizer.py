
import csv
import io
import random
from views.main_view import MainView
from model.background_traits import BackgroundTraits
from utils.data_file_loader import DataFileLoader as DFL


class Randomizer(object):
  def __init__(self):
    self.classes = []
    self.races = []
    self.bg_traits = None
    self.sources = {}
    self.specializations = {}

    self.cur_race = None
    self.cur_race_src = None
    self.cur_race_src_short = None
    self.cur_class = None
    self.cur_spec_name = None
    self.cur_spec = None
    self.cur_class_src = None
    self.cur_class_src_short = None
    self.cur_bg = None
    self.cur_traits = ''
    self.cur_bg_src_short = None

    self.load_data()

  def load_data(self):
    self.classes = DFL().load_csv('classes')
    self.races = DFL().load_csv('races')
    self.bg_traits = BackgroundTraits('background_traits')

    temp_sources = DFL().load_csv('sources')
    temp_specs = DFL().load_csv('class_specializations')

    for tsrc in temp_sources:
      self.sources[tsrc[0]] = tsrc[1]
    for tspec in temp_specs:
      self.specializations[tspec[0]] = tspec[1:]

  def _get_filtered_list(self, full_list, options):
    if options is None:
      return full_list

    filtered_set = []
    for item in full_list:
      for opt in options:
        if opt in item[-1]:
          filtered_set += [item]
          break
    return filtered_set

  def _get_short_source_text(self, srctext):
    src_texts = []
    sources = srctext.split('/')
    for rsrc in sources:
      additional = False
      if rsrc.endswith('+'):
        rsrc = rsrc[:-1]
        additional = True
      if additional:
        rsrc = "%s [addl. vars.]" % rsrc
      src_texts += [rsrc]
    return ', '.join(src_texts)

  def _get_source_text(self, srctext):
    src_texts = []
    sources = srctext.split('/')
    for rsrc in sources:
      additional = False
      if rsrc.endswith('+'):
        rsrc = rsrc[:-1]
        additional = True
      if rsrc.startswith('UA'):
        rsrc = 'UA'
      full_src = self.sources[rsrc]
      if additional:
        full_src = "%s [additional variations]" % full_src
      src_texts += [full_src]
    return '(Source: %s)' % ', '.join(src_texts)

  def _shuffle_race(self, even=False, skip_race=False, sources=None):
    rs = self._get_filtered_list(self.races, sources)
    if skip_race or rs == []:
      return
    if even:
      races = []
      for r in rs:
        if r[0] not in races:
          races += [r[0]]
      race = random.choice(races)
      single_race = []
      for r in rs:
        if r[0] == race:
          single_race += [r]
      _, variation, identity, srcs = random.choice(single_race)
    else:
      race, variation, identity, srcs = random.choice(rs)

    race_text = race
    if variation != '':
      race_text = "%s %s" % (variation, race_text)
    if identity != '':
      race_text = "%s (%s)" % (race_text, identity)

    self.cur_race = race_text
    self.cur_race_src = self._get_source_text(srcs)
    self.cur_race_src_short = self._get_short_source_text(srcs)

  def _shuffle_class(self, even=False, skip_class=False, skip_spec=False, sources=None):
    cs = self._get_filtered_list(self.classes, sources)
    if (skip_class and skip_spec) or cs == []:
      return
    if even or skip_class:
      if skip_class:
        class_name = self.cur_class
      else:
        classes = []
        for c in cs:
          if c[0] not in classes:
            classes += [c[0]]
        class_name = random.choice(classes)
      single_class = []
      for c in cs:
        if c[0] == class_name:
          single_class += [c]
      _, specification, exception, srcs = random.choice(single_class)
    else:
      class_name, specification, exception, srcs = random.choice(cs)

    spec_name, formatting = self.specializations[class_name]
    
    spec_text = ''
    if exception != '':
      spec_text = exception
    else:
      spec_text = str.format(formatting, specification)

    self.cur_class = class_name
    self.cur_spec = spec_text
    self.cur_spec_name = spec_name
    self.cur_class_src = self._get_source_text(srcs)
    self.cur_class_src_short = self._get_short_source_text(srcs)
    
  def _shuffle_bg(self, skip_bgs=False, sources=None):
    bg = self.bg_traits.get_random_bg(sources)
    if skip_bgs or bg is None:
      return
    self.cur_bg = bg.name
    self.cur_bg_src_short = bg.source
    self.cur_traits = bg.get_traits_as_str()
    

  def pick(self, even=False, skip_race=False, skip_class=False, skip_spec=False, skip_bg=False, sources=None):
    self._shuffle_race(even, skip_race, sources)
    self._shuffle_class(even, skip_class, skip_spec, sources)
    self._shuffle_bg(skip_bg, sources)
    # self.print_race_class_with_short_sources()

  def print_race_class(self):
    print(self.cur_race)
    print(self.cur_class)

  def print_race_class_with_sources(self):
    print('%s  |  %s' % (self.cur_race, self.cur_race_src))
    print('%s  |  %s' % (self.cur_class, self.cur_class_src))

  def print_race_class_with_short_sources(self):
    print('%s  |  %s' % (self.cur_race, self.cur_race_src_short))
    print('%s  |  %s' % (self.cur_class, self.cur_class_src_short))


if __name__ == '__main__':
  rnd = Randomizer()
  v = MainView.load_view(rnd)
  v.present(style='fullscreen')
