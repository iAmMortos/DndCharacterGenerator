
import random


class Randomizer(object):
  def __init__(self):
    self.classes = []
    self.races = []
    self.sources = {}
    self.specializations = {}

    self.cur_race = None
    self.cur_race_src = None
    self.cur_race_src_short = None
    self.cur_class = None
    self.cur_class_src = None
    self.cur_class_src_short = None

    self.load_data()

  def load_data(self):
    self.classes = self._load_csv('data/classes.csv')
    self.races = self._load_csv('data/races.csv')

    temp_sources = self._load_csv('data/sources.csv')
    temp_specs = self._load_csv('data/class_specializations.csv')

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

  def _load_csv(self, file):
    with open(file) as f:
      lines = [l.strip().split(',') for l in f.readlines()]
    return lines

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
    return '(Src: %s)' % ', '.join(src_texts)

  def _get_source_text(self, srctext):
    src_texts = []
    sources = srctext.split('/')
    for rsrc in sources:
      additional = False
      if rsrc.endswith('+'):
        rsrc = rsrc[:-1]
        additional = True
      full_src = self.sources[rsrc]
      if additional:
        full_src = "%s [additional variations]" % full_src
      src_texts += [full_src]
    return '(Source: %s)' % ', '.join(src_texts)

  def _shuffle_race(self, sources=None):
    rs = self._get_filtered_list(self.races, sources)
    race, variation, identity, srcs = random.choice(rs)

    race_text = race
    if variation != '':
      race_text = "%s %s" % (variation, race_text)
    if identity != '':
      race_text = "%s (%s)" % (race_text, identity)

    self.cur_race = race_text
    self.cur_race_src = self._get_source_text(srcs)
    self.cur_race_src_short = self._get_short_source_text(srcs)

  def _shuffle_class(self, sources=None):
    cs = self._get_filtered_list(self.classes, sources)
    class_name, specification, exception, srcs = random.choice(cs)

    spec_name, formatting = self.specializations[class_name]
    class_text = '%s -' % class_name
    if exception != '':
      class_text = '%s %s' % (class_text, exception)
    else:
      class_text = '%s %s: %s' % (class_text, spec_name, formatting)
      class_text = str.format(class_text, specification)

    self.cur_class = class_text
    self.cur_class_src = self._get_source_text(srcs)
    self.cur_class_src_short = self._get_short_source_text(srcs)

  def pick(self, skip_race=False, skip_class=False, sources=None):
    if not skip_race:
      self._shuffle_race(sources)
    if not skip_class:
      self._shuffle_class(sources)
    self.print_race_class_with_short_sources()

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

  for _ in range(50):
    rnd.pick()
    print()
