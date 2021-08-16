import io
import random


class BG (object):
  def __init__(self, name, src):
    self.name = name
    self.source = src
    self.tables = {}
    
  def roll_all_tables(self):
    d = {k:t.roll() for k,t in self.tables.items()}
    pts = 'Personality Trait'
    if pts in d:
      pt = d[pts]
      pt2 = pt
      while pt2 == pt:
        pt2 = self.tables[pts].roll()
      s = f'- {pt}\n  - {pt2}'
      d[pts] = s
    return d
 
  def get_traits_as_str(self):
    d = self.roll_all_tables()
    ss = []
    defaults = ['Personality Trait', 'Ideal', 'Bond', 'Flaw']
    for k in d.keys():
      if k not in defaults:
        ss += [f'{k}:\n\n  {d[k]}']
    for k in defaults:
      if k in d:
        if k == 'Personality Trait':
          ss += [f'Personality Traits:\n\n  {d[k]}']
        else:
          ss += [f'{k}:\n\n  {d[k]}']
    return '\n\n'.join(ss)
  
  def get_tbl(self, name):
    if name in self.tables:
      return self.tables[name]
    else:
      raise ValueError(f'Table [{name}] does not exist.')
      
  def get_tbls(self):
    return sorted(list(self.tables.keys()))


class Table (object):
  def __init__(self, name, nvals):
    self.name = name
    self.nvals = int(nvals)
    self.values = []
    
  def roll(self):
    i = random.randint(1, self.nvals)
    for v in self.values:
      if i <= v.hi:
        return v.val


class TblValue (object):
  def __init__(self, s):
    self.nval, self.val = s.split('|')
    if '-' in self.nval:
      self.lo, self.hi = [int(i) for i in self.nval.split('-')]
    else:
      self.lo = 0
      self.hi = int(self.nval)

  def __repr__(self):
    return f'{self.nval}: {self.val}'


class BackgroundTraits (object):
  def __init__(self, path):
    self.bgs = {}
    with io.open(path, mode='r', encoding='utf-8') as f:
      lines = [l.strip() for l in f.readlines()]
      for line in lines:
        bg, tb, n, v, src = line.split('\t')
        if bg not in self.bgs:
          self.bgs[bg] = BG(bg, src)
        b = self.bgs[bg]
        if tb not in b.tables:
          b.tables[tb] = Table(tb, n)
        t = b.tables[tb]
        t.values.append(TblValue(v))
        
  def get_random_bg(self, filters=None):
    filtered_bgs = []
    for bg in self.bgs.values():
      if filters is None or bg.source in filters:
        filtered_bgs.append(bg)
    if filtered_bgs:
      return random.choice(filtered_bgs)
    else:
      return None
        
  def get_bg(self, name):
    if name in self.bgs:
      return self.bgs[name]
    else:
      raise ValueError(f'Background [{name}] does not exist.')
    
  def get_bgs(self):
    return sorted(list(self.bgs.keys()))

