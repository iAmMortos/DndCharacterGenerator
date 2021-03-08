# TODO: Flesh out class
class Saves(object):
  def __init__(self, s):
    saves = [e.strip() for e in s.split(',')]
    self.s = s

  def __repr__(self):
    return self.s
