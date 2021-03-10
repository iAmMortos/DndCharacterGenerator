
class DieTable(object):
  def __init__(self, s):
    lines = s.split("\n")
    self.die, self.name = DieTable.split_line(lines[0])
    self.values = []
    for line in lines[1:]:
      if line.strip() != '':
        self.values += [DieTable.split_line(line)]

  def __repr__(self):
    s = '{0.name}, Die: {0.die}\n'.format(self)
    s += '\n'.join([' {0[0]} - {0[1]}'.format(v) for v in self.values])
    return s

  @staticmethod
  def split_line(line):
    return [s.strip() for s in line.split('|')]