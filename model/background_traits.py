import io
import random


class Background (object):
  def __init__(self, name, src):
    self.name = name
    self.source = src
    self.tables = {}
    
  def roll_all_tables(self):
    return {k:t.roll() for k,t in self.tables.items()}
 
  def get_traits_as_str(self):
    d = self.roll_all_tables()
    ss = []
    defaults = ['Personality Trait', 'Ideal', 'Bond', 'Flaw']
    for k in d.keys():
      if k not in defaults:
        ss += [f'{k}\n  {d[k]}']
    for k in defaults:
      if k in d:
        ss += [f'{k}\n  {d[k]}']
    return '\n'.join(ss)
  
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
          self.bgs[bg] = Background(bg, src)
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

