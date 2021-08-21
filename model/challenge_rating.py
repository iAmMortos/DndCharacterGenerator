class ChallengeRating(object):
  def __init__(self, s):
    if s not in ['1/8', '1/4', '1/2'] and s not in [str(n) for n in range(0, 31)]:
      raise ValueError('The given value [%s] is not a valid challenge rating.' % s)
    self.cr_str = s
    self.cr = .5 if s=='1/2' else .25 if s=='1/4' else .125 if s=='1/8' else int(s)
    self.xp = self.get_xp(self.cr)
    
  @staticmethod
  def get_xp(cr):
    d = {
      0: 10,
      0.125: 25,
      0.25: 50,
      0.5: 100,
      1: 200,
      2: 450,
      3: 700,
      4: 1100,
      5: 1800,
      6: 2300,
      7: 2900,
      8: 3900,
      9: 5000,
      10: 5900,
      11: 7200,
      12: 8400,
      13: 10000,
      14: 11500,
      15: 13000,
      16: 15000,
      17: 18000,
      18: 20000,
      19: 22000,
      20: 25000,
      21: 33000,
      22: 41000,
      23: 50000,
      24: 62000,
      25: 75000,
      26: 90000,
      27: 105000,
      28: 120000,
      29: 135000,
      30: 155000
    }
    if cr not in d:
      raise ValueError('The given value [%s] is not a valid challenge rating.' % cr)
    return d[cr]

  def __repr__(self):
    xps = str(self.xp)
    if len(xps) > 3:
      xps = '{},{}'.format(xps[:-3], xps[-3:])
    return '{} ({} XP)'.format(self.cr_str, xps)
