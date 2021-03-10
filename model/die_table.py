
import random


class DieTable(object):
  def __init__(self, s):
    lines = s.split("\n")
    self.die, self.name = DieTable.split_line(lines[0])
    self.values = []
    for line in lines[1:]:
      if line.strip() != '':
        self.values += [DieTable.split_line(line)]
        
  def roll(self):
    i = random.randint(1, int(self.die[1:]))
    for v in self.values:
      r,m = v
      r = r.split('-')
      if len(r) == 1:
        if int(r[0]) == i:
          return m
      elif len(r) == 2:
        if int(r[0]) <= i <= int(r[1]):
          return m
    raise Exception('Didn\'t find value for [%s]' % i)
      
      
      

  def __repr__(self):
    s = '{0.name}, Die: {0.die}\n'.format(self)
    s += '\n'.join([' {0[0]} - {0[1]}'.format(v) for v in self.values])
    return s

  @staticmethod
  def split_line(line):
    return [s.strip() for s in line.split('|')]
