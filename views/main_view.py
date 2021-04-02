import ui
from views.filter_config_view import FilterConfigView

class MainView(ui.View):
  def init(self, randomizer):
    self.rand = randomizer
    self.rand.pick()
    self.update_labels()
    
  def update_labels(self):
    self.summary_lbl.text = '%s %s' % (self.rand.cur_race, self.rand.cur_class)
    self.spec_name_lbl.text = '%s:' % self.rand.cur_spec_name
    self.spec_lbl.text = self.rand.cur_spec
    self.bg_lbl.text = 'Background: %s' % self.rand.cur_bg
    self.race_src_lbl.text = 'Race Source: %s' % self.rand.cur_race_src_short
    self.class_src_lbl.text = 'Class Source: %s' % self.rand.cur_class_src_short
    self.bg_src_lbl.text = 'Background Source: %s' % self.rand.cur_bg_src_short
    self.traits_txt.text = self.rand.cur_traits
    
  def did_load(self):
    self.summary_lbl = self['lbl_summary']
    self.race_src_lbl = self['lbl_race_src']
    self.class_src_lbl = self['lbl_class_src']
    self.spec_lbl = self['lbl_spec']
    self.spec_name_lbl = self['lbl_spec_name']
    self.bg_lbl = self['lbl_bg']
    self.bg_src_lbl = self['lbl_bg_src']
    self.traits_txt = self['txt_traits']
    self.shuffle_btn = self['btn_shuffle']
    self.shuffle_btn.action = self.handle_shuffle
    self.filter_btn = self['btn_filter']
    self.filter_btn.action = self.handle_filter
    
    self.filter_view = FilterConfigView.load_view()
    
  def handle_shuffle(self, target):
    self.rand.pick(self.filter_view.even_sw.value, self.filter_view.race_sw.value, self.filter_view.class_sw.value, self.filter_view.spec_sw.value, self.filter_view.bg_sw.value, self.filter_view.get_selected_sources())
    self.update_labels()
  
  def handle_filter(self, target):
    self.filter_view.present(style='fullscreen')
  
  @staticmethod
  def load_view(randomizer):
    v = ui.load_view()
    v.init(randomizer)
    return v

  
