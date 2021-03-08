
from enum import Enum
from model.xml_entity import XmlEntity
from model.creature_type import CreatureType
from model.alignment import Alignment
from model.armor_class import ArmorClass
from model.hit_points import HitPoints
from model.speed import Speed
from model.ability_scores import AbilityScores
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
    self.ability_scores = AbilityScores(self._get('str'), self._get('dex'), self._get('con'), self._get('int'), self._get('wis'), self._get('cha'))
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

    self.traits = self._get_as_obj_list('trait', Action)
    self.actions = self._get_as_obj_list('action', Action)
    self.reactions = self._get_as_obj_list('reaction', Action)
    self.legendaries = self._get_as_obj_list('legendary', Action)
    
    print(self)
    
  def __repr__(self):
    return 'Name: {0.name}\nSize: {0.size}\nType: {0.type}\nAlignment: {0.alignment}\nAC: {0.armor_class}\nHP: {0.hit_points}\nSpeed: {0.speed}\nAbility Scores: {0.ability_scores}\nSaves: {0.saves}\nSkill: {0.skill}\nVulnerable: {0.vulnerable}+\nResist: {0.resist}\nImmunities: {0.immune}\nConditional Immunities: {0.conditionImmune}\nSenses: {0.senses}\nPassive: {0.passive}\nLanguages: {0.languages}\nCR: {0.challenge_rating}\nTraits: {1}\nActions: {2}\nReactions: {3}\nLegendary Actions: {4}'.format(self,
    ', '.join([t.name for t in self.traits]),
    ', '.join([a.name for a in self.actions]),
    ', '.join([r.name for r in self.reactions]),
    ', '.join([l.name for l in self.legendaries]))

