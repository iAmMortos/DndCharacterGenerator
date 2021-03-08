
from model.ability_score import AbilityScore

class AbilityScores (object):
  def __init__(self, str=10, dex=10, con=10, int=10, wis=10, cha=10):
    self.str = AbilityScore(str)
    self.dex = AbilityScore(dex)
    self.con = AbilityScore(con)
    self.int = AbilityScore(int)
    self.wis = AbilityScore(wis)
    self.cha = AbilityScore(cha)
    
  def __repr__(self):
    return 'Str: {0.str} Dex: {0.dex} Con: {0.con} Int: {0.int} Wis: {0.wis} Cha: {0.cha}'.format(self)
