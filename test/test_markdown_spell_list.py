import test_context
from model.data_loader import DataLoader
import os
import io
import ui
from markdownutils.markdown_generator import MarkdownGenerator
import console


spell_list = '''Alarm
Animal Friendship
Cure Wounds
Detect Magic
Detect Poison and Disease
Ensnaring Strike
Fog Cloud
Goodberry
Hail of Thorns
Hunter's Mark
Jump
Longstrider
Speak with Animals
Animal Messenger
Barkskin
Beast Sense
Cordon of Arrows
Darkvision
Find Traps
Lesser Restoration
Locate Animals or Plants
Locate Object
Pass without Trace
Protection from Poison
Silence
Spike Growth
Conjure Animals
Conjure Barrage
Daylight
Lightning Arrow
Nondetection
Plant Growth
Protection from Energy
Speak with Plants
Water Breathing
Water Walk
Wind Wall
Conjure Woodland Beings
Freedom of Movement
Grasping Vine
Locate Creature
Stoneskin
Commune with Nature
Conjure Volley
Swift Quiver
Tree Stride
Disguise Self
Rope Trick
Fear
Greater Invisibility
Seeming'''.split('\n')


def main():
  mdt = ''
  md = MarkdownGenerator()
  dl = DataLoader('Complete')
  spells = {}
  for s in spell_list:
    sp = dl.get_spell(s)
    lvl = sp.level
    if lvl not in spells:
      spells[lvl] = []
    spells[lvl] += [sp]
    
  for k in sorted(spells.keys()):
    mdt += f'# Level {k}\n\n'
    spells[k].sort(key= lambda s: s.name)
    for s in spells[k]:
      mdt += md.gen_spell_block(s) + '\n'
  
  console.clear()
  print(mdt)

if __name__ == '__main__':
  main()
