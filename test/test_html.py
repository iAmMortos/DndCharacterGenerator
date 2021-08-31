import test_context
from model.data_loader import DataLoader
from utils.regexes import is_attack, get_attack
import webbrowser
import os
import io
import random


def main():
  dl = DataLoader('data/xml/Complete.xml')
  monster_name = random.choice(list(dl.monsters.keys()))
  monster = dl.monsters[monster_name]
  
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

  block = block.replace('{description}', '<p class="stat-line">{}<p>'.format(monster.description.strip().replace('\n', '<br />')))

  html = html.replace('{title}', 'Test Stat Block')
  html = html.replace('{stylesheet-path}', 'templates/css/statblock.css')
  html = html.replace('{body}', block)
  with io.open('views/html/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

  abspath = os.path.abspath('views/html/index.html')
  abspath = abspath.replace('\\', '/')
  url = 'file:///{}'.format(abspath)
  webbrowser.open_new_tab(url)


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
      traits += trait.replace('{name}', t.name).replace('{value}', t.text)
    elif t.attack:
      print(t.attack)
  return traits


def build_actions(monster):
  if not monster.actions:
    return ''
  with open('views/html/templates/actions.html') as f:
    actions_html = f.read()
  actions = []
  for action in monster.actions:
    if is_attack(action.text):
      with open('views/html/templates/attack.html') as f:
        html = f.read()
      parts = get_attack(action.text)
      html = html.replace('{name}', action.name).replace('{attack-type}', parts[0]).replace('{to-hit}', parts[1]).replace('{damage}', parts[2])
      actions += [html]
    else:
      with open('views/html/templates/trait.html') as f:
        html = f.read()
      html = html.replace('{name}', action.name).replace('{value}', action.text)
      actions += [html]
  actions_html = actions_html.replace('{actions}', ''.join(actions))

  return actions_html


def build_reactions(monster):
  if not monster.reactions:
    return ''
  with open('views/html/templates/reactions.html') as f:
    reactions = f.read()

  return reactions


def build_legendaries(monster):
  if not monster.legendaries:
    return ''
  with open('views/html/templates/legendaries.html') as f:
    legendaries = f.read()

  return legendaries


if __name__ == '__main__':
  main()
