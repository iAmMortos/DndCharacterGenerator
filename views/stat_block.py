import ui
import sharedlibs
sharedlibs.add_path_for('view_swap')
import view_swap
from views.ability_score_block import AbilityScoreBlockView
from utils import html_loader


class StatBlockView(ui.View):
  
  def init(self, monster):
    self.lbl_name.text = monster.name
    self.lbl_sta.text = monster.sta_txt
    self.lbl_ac.text = str(monster.armor_class)
    self.lbl_hp.text = str(monster.hit_points)
    self.lbl_speed.text = str(monster.speed)
    self.cv_scores = AbilityScoreBlockView.load_view(monster.ability_scores)
    view_swap.ViewSwap(self['sv']).swap('cv_scores', self.cv_scores)
    
  def did_load(self):
    s = self['sv']
    self.lbl_name = s['lbl_creature_name']
    self.lbl_sta = s['lbl_size_type_alignment']
    self.lbl_ac = s['lbl_ac']
    self.lbl_hp= s['lbl_hit_points']
    self.lbl_speed = s['lbl_speed']
    self.wv_skills = s['wv_skills']
    html = html_loader.load_html_boilerplate('<h1>sup</h1>')
    self.wv_skills.load_html(html)
  
  @staticmethod
  def load_view(monster):
    v = ui.load_view()
    v.init(monster)
    return v
