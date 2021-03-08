
from enum import Enum
from model.xml_entity import XmlEntity
from model.creature_type import CreatureType
from model.alignment import Alignment
from model.armor_class import ArmorClass
from model.hit_points import HitPoints
from model.speed import Speed
from model.ability_score import AbilityScore
from model.saves import Saves
from model.skill import Skill
from model.challenge_rating import ChallengeRating
from model.action import Action


class CreatureSize (Enum):
  T = 'tiny'
  S = 'small'
  M = 'medium'
  L = 'large'
  H = 'huge'
  G = 'gargantuan'

  @staticmethod
  def of_value(s):
    try:
      return CreatureSize.__getitem__(s)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % s)


class Monster (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.size = self._get_as_obj('size', CreatureSize.of_value)
    self.type = self._get_as_obj('type', CreatureType)
    self.alignment = self._get_as_obj('alignment', Alignment)
    self.armor_class = self._get_as_obj('ac', ArmorClass)
    self.hit_points = self._get_as_obj('hp', HitPoints)
    self.speed = self._get_as_obj('speed', Speed)
    self.str = self._get_as_obj('str', AbilityScore)
    self.dex = self._get_as_obj('dex', AbilityScore)
    self.con = self._get_as_obj('con', AbilityScore)
    self.int = self._get_as_obj('int', AbilityScore)
    self.wis = self._get_as_obj('wis', AbilityScore)
    self.cha = self._get_as_obj('cha', AbilityScore)
    self.saves = self._get_as_obj('save', Saves)
    self.skill = self._get_as_obj('skill', Skill)
    self.vulnerable = self._get('vulnerable')
    self.resist = self._get('resist')
    self.immune = self._get('immune')
    self.conditionImmune = self._get('conditionImmune')
    self.senses = self._get('senses')
    self.passive = self._get_as_obj('passive', int)
    self.languages = self._get('languages')
    self.challenge_rating = self._get_as_obj('cr', ChallengeRating)

    self.traits = self._get_as_obj('trait', Action)
    self.actions = self._get_as_obj('action', Action)
    self.reactions = self._get_as_obj('reaction', Action)
    self.legendaries = self._get_as_obj('legendary', Action)

    if self.saves is not None:
      print(self.saves)