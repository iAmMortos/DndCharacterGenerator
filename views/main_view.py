import ui

class MainView(ui.View):
  def init(self, randomizer):
    self.rand = randomizer
    self.rand.pick()
    self.update_labels()
    
  def update_labels(self):
    self.summary_lbl.text = '%s %s' % (self.rand.cur_race, self.rand.cur_class)
    self.spec_name_lbl.text = '%s:' % self.rand.cur_spec_name
    self.spec_lbl.text = self.rand.cur_spec
    self.race_src_lbl.text = 'Race Source: %s' % self.rand.cur_race_src_short
    self.class_src_lbl.text = 'Class Source: %s' % self.rand.cur_class_src_short
    
  def did_load(self):
    self.summary_lbl = self['lbl_summary']
    self.race_src_lbl = self['lbl_race_src']
    self.class_src_lbl = self['lbl_class_src']
    self.spec_lbl = self['lbl_spec']
    self.spec_name_lbl = self['lbl_spec_name']
    
    sv = self['sv']
    self.race_sw = sv['sw_race']
    self.class_sw = sv['sw_class']
    self.class_sw.action = self.handle_class_sw
    self.spec_sw = sv['sw_spec']
    self.spec_sw.action = self.handle_spec_sw
    self.even_sw = sv['sw_even']
    
    self.phb_sw = sv['sw_phb']
    self.dmg_sw = sv['sw_dmg']
    self.xgte_sw = sv['sw_xgte']
    self.vgtm_sw = sv['sw_vgtm']
    self.scag_sw = sv['sw_scag']
    self.mtof_sw = sv['sw_mtof']
    self.eepc_sw = sv['sw_eepc']
    self.wgte_sw = sv['sw_wgte']
    self.ggtr_sw = sv['sw_ggtr']
    self.ttp_sw = sv['sw_ttp']
    self.lr_sw = sv['sw_lr']
    self.gpdf_sw = sv['sw_gpdf']
    self.source_sws = [self.phb_sw, self.dmg_sw, self.xgte_sw, self.vgtm_sw, self.scag_sw, self.mtof_sw,
                       self.eepc_sw, self.wgte_sw, self.ggtr_sw, self.ttp_sw, self.lr_sw, self.gpdf_sw]
    
    self.sel_all_btn = sv['btn_sel_all']
    self.sel_all_btn.action = self.handle_sel_all
    self.desel_all_btn = sv['btn_desel_all']
    self.desel_all_btn.action = self.handle_desel_all
    self.shuffle_btn = self['btn_shuffle']
    self.shuffle_btn.action = self.handle_shuffle
    
  def handle_shuffle(self, target):
    self.rand.pick(self.even_sw.value, self.race_sw.value, self.class_sw.value, self.spec_sw.value, self.get_selected_sources())
    self.update_labels()
  
  def handle_sel_all(self, target):
    for sw in self.source_sws:
      sw.value = True

  def handle_desel_all(self, target):
    for sw in self.source_sws:
      sw.value = False

  def handle_class_sw(self, target):
    if not self.class_sw.value:
      self.spec_sw.value = False
    
  def handle_spec_sw(self, target):
    if self.spec_sw.value:
      self.class_sw.value = True
      
  def get_selected_sources(self):
    srcs = []
    if self.phb_sw.value:
      srcs += ['PHB']
    if self.dmg_sw.value:
      srcs += ['DMG']
    if self.xgte_sw.value:
      srcs += ['XGtE']
    if self.vgtm_sw.value:
      srcs += ['VGtM']
    if self.scag_sw.value:
      srcs += ['SCAG']
    if self.mtof_sw.value:
      srcs += ['MToF']
    if self.eepc_sw.value:
      srcs += ['EEPC']
    if self.wgte_sw.value:
      srcs += ['WGtE']
    if self.ggtr_sw.value:
      srcs += ['GGtR']
    if self.ttp_sw.value:
      srcs += ['tTP']
    if self.lr_sw.value:
      srcs += ['LR']
    if self.gpdf_sw.value:
      srcs += ['gPDF']
    return srcs
  
  @staticmethod
  def load_view(randomizer):
    v = ui.load_view()
    v.init(randomizer)
    return v

  
