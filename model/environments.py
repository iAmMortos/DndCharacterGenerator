
class Environments (object):
  def __init__(self, s):
    self._envs = [e.strip() for e in s.split(',')]
    
  def __iter__(self):
    return 
