
from model.xml_entity import XmlEntity
from model.creature_type import CreatureType
from model.creature_size import CreatureSize
from model.alignment import Alignment
from model.armor_class import ArmorClass
from model.hit_points import HitPoints
from model.speed import Speed
from model.ability_scores import AbilityScores
from model.saves import Saves
from model.skill import Skill
from model.challenge_rating import ChallengeRating
from model.action import Action
from utils.regexes import get_sources


class Monster (XmlEntity):
  def __init__(self, xml_node):
    super().__init__(xml_node)

    self.name = self._get('name')
    self.size = self._get_as_obj('size', CreatureSize.of_value)
    if 'tome of Beasts' in self._data['type'].text:
      self.type = CreatureType(self._data['type'].text.split(',')[0])
      self._data['description'] = 'Source: Tome of Beasts'
    else:
      self.type = self._get_as_obj('type', CreatureType)
    self.alignment = self._get_as_obj('alignment', Alignment)
    self.sta_txt = '%s %s, %s' % (str(self.size).capitalize(), self.type, self.alignment)
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

    self.senses_str = self.senses
    if self.senses_str and self.passive:
      self.senses_str += ", passive Perception {}".format(self.passive)
    elif self.passive:
      self.senses_str = 'passive Perception {}'.format(self.passive)
    else:
      self.senses_str = None

    self.languages = self._get('languages')
    self.challenge_rating = self._get_as_obj('cr', ChallengeRating)
    self.summary = '%s, %s %s' % (self.challenge_rating, self.size, self.type)
    self.description = self._get('description')

    self.traits = self._get_as_obj_list('trait', Action)
    self.actions = self._get_as_obj_list('action', Action)
    self.reactions = self._get_as_obj_list('reaction', Action)
    self.legendaries = self._get_as_obj_list('legendary', Action)
    self.mythics = self._get_as_obj_list('mythic', Action)
    self.lairs = self._get_as_obj_list('lair', Action)
    self.environment = self._get('environment')

    self.sources = get_sources(self.description)
    

  def __repr__(self):
    return 'Name: {0.name}\nSize: {0.size}\nType: {0.type}\nAlignment: {0.alignment}\nAC: {0.armor_class}\n' \
           'HP: {0.hit_points}\nSpeed: {0.speed}\nAbility Scores: {0.ability_scores}\nSaves: {0.saves}\n' \
           'Skill: {0.skill}\nVulnerable: {0.vulnerable}+\nResist: {0.resist}\nImmunities: {0.immune}\n' \
           'Conditional Immunities: {0.conditionImmune}\nSenses: {0.senses}\nPassive: {0.passive}\n' \
           'Languages: {0.languages}\nCR: {0.challenge_rating}\n' \
           'Traits: {1}\nActions: {2}\nReactions: {3}\nLegendary Actions: {4}\nMythic Actions: {5}\nLair: {6}'.format(
      self, len(self.traits), len(self.actions), len(self.reactions), len(self.legendaries), len(self.mythics), len(self.lairs))

