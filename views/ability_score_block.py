import ui

class AbilityScoreBlockView(ui.View):
  def init(self, scores):
    self.lbl_str.text = str(scores.str)
    self.lbl_dex.text = str(scores.dex)
    self.lbl_con.text = str(scores.con)
    self.lbl_int.text = str(scores.int)
    self.lbl_wis.text = str(scores.wis)
    self.lbl_cha.text = str(scores.cha)
    
  def did_load(self):
    self.lbl_str = self['lbl_str']
    self.lbl_dex = self['lbl_dex']
    self.lbl_con = self['lbl_con']
    self.lbl_int = self['lbl_int']
    self.lbl_wis = self['lbl_wis']
    self.lbl_cha = self['lbl_cha']
    
  @staticmethod
  def load_view(scores):
    v = ui.load_view()
    v.init(scores)
    return v
