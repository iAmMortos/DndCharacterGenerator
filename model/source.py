



class Source(object):
  def __init__(self, s):
    pp = s.split('p.')
    self.src = None
    self.abbr = None
    self.p = None
    if len(pp) > 1:
      self.src = pp[0].strip()
      self.p = pp[1].strip()
    else:
      self.src = pp[0]
    self.abbr = self.lookup(self.src)


  def lookup(self, s):
    with open('data/sources.csv') as f:
      lines = [line.strip().split(',') for line in f.readlines()]
    for line in lines:
      if line[1] == s or line[2] == s:
        return line[0]
    return None


  def __repr__(self):
    return f'{self.src}{"" if self.p is None else f" (p. {self.p})"}'
