
from model.ability_scores import AbilityScores
from model.pc.note import Note
from model.pc.container import Container
from model.pc.item import Item
from model.pc.tracker import Tracker
from model.pc.attack import Attack
from model.pc.feat import Feat
from model.pc.background import Background
from model.pc.image_ref import ImageRef
from model.pc.race import Race
from model.pc.pc_class import Class
from model.xml_entity import XmlEntity


class Character(XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)
    
    self.version = self._get('version')
    self.uid = self._get('uid')
    self.name = self._get('name')
    self.imageData = self._get_as_obj('imageData', ImageRef)
    self.race = self._get_as_obj('race', Race)
    self.pc_class = self._get_as_obj('class', Class)
    self.background = self._get_as_obj('background', Background)
    self.feats = self._get_as_obj_list('feat', Feat)
    self.attacks = self._get_as_obj_list('attack', Attack)
    self.trackers = self._get_as_obj_list('tracker', Tracker)
    self.items = self._get_as_obj_list('item', Item)
    self.containers = self._get_as_obj_list('container', Container)
    self.notes = self._get_as_obj_list('note', Note)
    self.abilities = AbilityScores(*self._get('abilities').split(',')[:6])
    self.hpMax = self._get('hpMax')
    self.hpCurrent = self._get('hpCurrent')
