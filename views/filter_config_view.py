import ui

class FilterConfigView(ui.View):
  def did_load(self):
    sv = self['sv']
    self.race_sw = sv['sw_race']
    self.class_sw = sv['sw_class']
    self.class_sw.action = self.handle_class_sw
    self.spec_sw = sv['sw_spec']
    self.spec_sw.action = self.handle_spec_sw
    self.bg_sw = sv['sw_bg']
    self.even_sw = sv['sw_even']
    
    self.phb_sw = sv['sw_phb']
    self.dmg_sw = sv['sw_dmg']
    self.xgte_sw = sv['sw_xgte']
    self.vgtm_sw = sv['sw_vgtm']
    self.scag_sw = sv['sw_scag']
    self.mtof_sw = sv['sw_mtof']
    self.eepc_sw = sv['sw_eepc']
    self.ggtr_sw = sv['sw_ggtr']
    self.ttp_sw = sv['sw_ttp']
    self.erftlw_sw = sv['sw_erftlw']
    self.ua_sw = sv['sw_ua']
    self.tcoe_sw = sv['sw_tcoe']
    self.source_sws = [self.phb_sw, self.dmg_sw, self.xgte_sw, self.vgtm_sw, self.scag_sw, self.mtof_sw,
                       self.eepc_sw, self.ggtr_sw, self.ttp_sw, self.erftlw_sw,
                       self.ua_sw, self.tcoe_sw]
    
    self.sel_all_btn = sv['btn_sel_all']
    self.sel_all_btn.action = self.handle_sel_all
    self.desel_all_btn = sv['btn_desel_all']
    self.desel_all_btn.action = self.handle_desel_all
    
    self.name = 'Filter Options'
    
  def init(self, config):
    pass
    
  def handle_class_sw(self, target):
    if not self.class_sw.value:
      self.spec_sw.value = False
    
  def handle_spec_sw(self, target):
    if self.spec_sw.value:
      self.class_sw.value = True
      
  def handle_sel_all(self, target):
    for sw in self.source_sws:
      sw.value = True

  def handle_desel_all(self, target):
    for sw in self.source_sws:
      sw.value = False
      
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
    if self.tcoe_sw.value:
      srcs += ['TCoE']
    if self.scag_sw.value:
      srcs += ['SCAG']
    if self.mtof_sw.value:
      srcs += ['MToF']
    if self.eepc_sw.value:
      srcs += ['EEPC']
    if self.ggtr_sw.value:
      srcs += ['GGtR']
    if self.ttp_sw.value:
      srcs += ['tTP']
    if self.erftlw_sw.value:
      srcs += ['ERftLW']
    if self.ua_sw.value:
      srcs += ['UA']
    return srcs
  
  @staticmethod
  def load_view(config=None):
    v = ui.load_view()
    v.init(config)
    return v
