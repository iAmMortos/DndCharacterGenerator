
import ui
from external import view_swap
from external.die_view import DieView


class StatRollView(ui.View):
  def did_load(self):
    vs = view_swap.ViewSwap(self)
    self.nfinished = 0
    self.name = 'Stat Roller'
    self.dice = []
    for r in range(1,7):
      row = []
      for c in range(1,5):
        d = DieView(self.on_finished)
        vs.swap(f'd{r}{c}', d)
        row.append(d)
      self.dice.append(row)
    self.stats = [self['str'], self['dex'], self['con'], self['int'], self['wis'], self['cha']]
    self.roll_btn = self['btn_roll']
    self.roll_btn.action = self.handle_roll
    self.total_lbl = self['lbl_total']
    self.sorted_lbl = self['lbl_sorted']
    
  def handle_roll(self, target):
    self.nfinished = 0
    self.total_lbl.text = ''
    self.sorted_lbl.text = ''
    for stat in self.stats:
      stat.text = '0'
    for row in self.dice:
      for die in row:
        die.enabled = True
        die.roll()
        
  def on_finished(self):
    self.nfinished += 1
    sts = []
    if self.nfinished == 24:
      for i,row in enumerate(self.dice):
        vs = [d._val for d in row]
        m = min(vs)
        for die in row[::-1]:
          if die._val == m:
            die.enabled = False
            break
        v = sum(vs) - m
        sts.append(v)
        self.stats[i].text = '{}({}{})'.format(v, '+' if v >= 10 else '', (v - 10)//2)
      self.total_lbl.text = f'Total: {sum(sts)}'
      self.sorted_lbl.text = ', '.join(['{}({}{})'.format(v, '+' if v >= 10 else '', (v - 10)//2) for v in sorted(sts, reverse=True)])
    
  @staticmethod
  def load_view():
    v = ui.load_view()
    # v.init()
    return v

