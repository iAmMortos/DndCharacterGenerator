import test_context
from model.data_loader import DataLoader
import webbrowser
import os
import random


def main():
  monster = random.choice(DataLoader('data/xml/CoreOnly.xml').monsters)

  with open('views/html/templates/boilerplate.html') as f:
    html = f.read()
  with open('views/html/templates/statblock.html') as f:
    block = f.read()

  block = block.replace('{creature-name}', monster.name)
  block = block.replace('{size-type-alignment}', monster.sta_txt)
  block = block.replace('{armor-class}', str(monster.armor_class))
  block = block.replace('{hit-points}', str(monster.hit_points))
  block = block.replace('{speed}', str(monster.speed))

  block = block.replace('{stat-str}', str(monster.ability_scores.str))
  block = block.replace('{stat-dex}', str(monster.ability_scores.dex))
  block = block.replace('{stat-con}', str(monster.ability_scores.con))
  block = block.replace('{stat-int}', str(monster.ability_scores.int))
  block = block.replace('{stat-wis}', str(monster.ability_scores.wis))
  block = block.replace('{stat-cha}', str(monster.ability_scores.cha))

  html = html.replace('{title}', 'Test Stat Block')
  html = html.replace('{stylesheet-path}', 'templates/css/statblock.css')
  html = html.replace('{body}', block)
  with open('views/html/index.html', 'w') as f:
    f.write(html)

  abspath = os.path.abspath('views/html/index.html')
  abspath = abspath.replace('\\', '/')
  url = 'file:///{}'.format(abspath)
  webbrowser.open_new_tab(url)


if __name__ == '__main__':
  main()