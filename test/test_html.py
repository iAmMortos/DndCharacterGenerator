import test_context
from model.data_loader import DataLoader
from utils.regexes import is_attack, get_attack
from xml.etree import ElementTree as ET
import webbrowser
import os
import io
import re
import random


def main():
  dl = DataLoader('data/xml/Complete.xml')
  monster = dl.get_monster('Young Frost Giant')
  # monster = random.choice(dl.monsters)
  
  with open('views/html/templates/boilerplate.html') as f:
    html = f.read()
  with open('views/html/templates/statblock.html') as f:
    block = f.read()

  block = block.replace('{creature-name}', monster.name)
  block = block.replace('{size-type-alignment}', monster.sta_txt)
  if monster.sources:
    block = block.replace('{source}', '<p class="source">{}</p>'.format(', '.join([s.get_abbr() for s in monster.sources])))
  block = block.replace('{armor-class}', str(monster.armor_class))
  block = block.replace('{hit-points}', str(monster.hit_points))
  block = block.replace('{speed}', str(monster.speed))

  block = block.replace('{stat-str}', str(monster.ability_scores.str))
  block = block.replace('{stat-dex}', str(monster.ability_scores.dex))
  block = block.replace('{stat-con}', str(monster.ability_scores.con))
  block = block.replace('{stat-int}', str(monster.ability_scores.int))
  block = block.replace('{stat-wis}', str(monster.ability_scores.wis))
  block = block.replace('{stat-cha}', str(monster.ability_scores.cha))

  profs = build_profs(monster)
  block = block.replace('{proficiencies}', profs)
  
  traits = build_traits(monster)
  block = block.replace('{traits}', traits)
  
  actions = build_actions(monster)
  block = block.replace('{actions}', actions)
  
  reactions = build_reactions(monster)
  block = block.replace('{reactions}', reactions)

  legendaries = build_legendaries(monster)
  block = block.replace('{legendaries}', legendaries)

  block = block.replace('{description}', '<p class="stat-line">{}</p>'.format(html_newlines(monster.description.strip())))

  html = html.replace('{title}', 'Test Stat Block')
  html = html.replace('{stylesheet-path}', 'templates/css/statblock.css')
  html = html.replace('{body}', block)
  with io.open('views/html/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

  abspath = os.path.abspath('views/html/index.html')
  abspath = abspath.replace('\\', '/')
  url = 'file:///{}'.format(abspath)
  webbrowser.open_new_tab(url)
  
  
def html_newlines(s):
  # st = re.sub('')
  return s.replace('\n', '<br />')


def build_profs(monster):
  with open('views/html/templates/statline.html') as f:
    statline = f.read()

  profs = ''
  if monster.saves:
    profs += statline.replace('{name}', 'Saving Throws').replace('{value}', str(monster.saves))
  if monster.skill:
    profs += statline.replace('{name}', 'Skills').replace('{value}', str(monster.skill))
  if monster.vulnerable:
    profs += statline.replace('{name}', 'Damage Vulnerabilities').replace('{value}', monster.vulnerable)
  if monster.resist:
    profs += statline.replace('{name}', 'Damage Resistances').replace('{value}', monster.resist)
  if monster.immune:
    profs += statline.replace('{name}', 'Damage Immunities').replace('{value}', monster.immune)
  if monster.conditionImmune:
    profs += statline.replace('{name}', 'Condition Immunities').replace('{value}', str(monster.conditionImmune))
  if monster.senses_str:
    profs += statline.replace('{name}', 'Senses').replace('{value}', monster.senses_str)
  if monster.languages:
    profs += statline.replace('{name}', 'Languages').replace('{value}', monster.languages)
  if monster.challenge_rating:
    profs += statline.replace('{name}', 'Challenge').replace('{value}', str(monster.challenge_rating))
  return profs


def build_traits(monster):
  if not monster.traits:
    return ''
  with open('views/html/templates/trait.html') as f:
    trait = f.read()

  traits = ''
  for t in monster.traits:
    if t.text:
      traits += trait.replace('{name}', t.name).replace('{value}', html_newlines(t.text))
    elif t.attack:
      raise(Exception(f'Found a trait containing an attack: [{t.attack}]'))
  return traits


def build_actions(monster):
  if not monster.actions:
    return ''
  with open('views/html/templates/actions.html') as f:
    actions_html = f.read()
  with open('views/html/templates/attack.html') as f:
    atk_html = f.read()
  with open('views/html/templates/trait.html') as f:
    act_html = f.read()
  actions = ''
  for action in monster.actions:
    if is_attack(action.text):
      parts = get_attack(action.text)
      actions += atk_html.replace('{name}', action.name).replace('{attack-type}', parts[0]).replace('{to-hit}', parts[1]).replace('{damage}', html_newlines(parts[2]))
    else:
      actions += act_html.replace('{name}', action.name).replace('{value}', html_newlines(action.text))

  return actions_html.replace('{actions}', actions)


def build_reactions(monster):
  if not monster.reactions:
    return ''
  with open('views/html/templates/reactions.html') as f:
    reactions_html = f.read()
  with open('views/html/templates/trait.html') as f:
    act_html = f.read()
  reactions = ''
  for reaction in monster.reactions:
    reactions += act_html.replace('{name}', reaction.name).replace('{value}', html_newlines(reaction.text))

  return reactions_html.replace('{reactions}', reactions)


def build_legendaries(monster):
  if not monster.legendaries:
    return ''
  with open('views/html/templates/legendaries.html') as f:
    legendaries_html = f.read()
  with open('views/html/templates/attack.html') as f:
    atk_html = f.read()
  with open('views/html/templates/trait.html') as f:
    leg_html = f.read()
  with open('views/html/templates/standalone_text_line.html') as f:
    std_html = f.read()
  legs = ''
  for legendary in monster.legendaries:
    if is_attack(legendary.text):
      parts = get_attack(html_newlines(legendary.text))
      legs += atk_html.replace('{name}', legendary.name).replace('{attack-type}', parts[0]).replace('{to-hit}', parts[1]).replace('{damage}', parts[2])
    elif legendary.name is None:
      legs += std_html.replace('{value}', html_newlines(legendary.text))
    else:
      legs += leg_html.replace('{name}', legendary.name).replace('{value}', html_newlines(legendary.text))

  return legendaries_html.replace('{legendaries}', legs)


if __name__ == '__main__':
  main()
