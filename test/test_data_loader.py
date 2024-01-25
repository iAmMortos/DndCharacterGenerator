import clipboard

import test_context

from model.data_loader import DataLoader
from utils.regexes import get_sources
from utils.regexes import is_attack

dl = DataLoader('Complete')
# dl.print_stats()


def test_environments():
  c = 0
  envs = []
  for m in dl.monsters:
    if m.environment:
      c += 1
      for e in [n.strip() for n in m.environment.split(',')]:
        if e not in envs:
          envs += [e]
      print(f'{m.name}: {m.environment}')
  print(f'{c} of {len(dl.monsters)} monsters have environments.')
  print(sorted(envs))


def test_wildemount_creatures():
  c = 0
  for m in dl.monsters:
    for s in m.sources:
      if s.abbr == 'EGtW':
        print(m.name)
        c += 1
        break
  print(f'{c} monsters found')

def test_environments():
  envs = []
  for m in dl.monsters:
    if m.environment:
      es = m.environment.split(', ')
      for env in es:
        if env == 'farmland':
          print(m.name)
        if env not in envs:
          envs += [env]
  print(envs)

def test_lair_monsters():
  c = 0
  for m in dl.monsters:
    if m.lairs:
      c += 1
  print(f'{c} monsters have lair features.')


def test_mythic_monsters():
  c = 0
  for m in dl.monsters:
    if m.mythics:
      c += 1
      print(m.name)
  print(f'{c} monsters have lair features.')

def test_spells():
  l = []
  for s in dl.spells:
#               if 'instantaneous,' in str(s.duration).lower():
#                       print(s.name)
    if str(s.duration) not in l:
      l += [str(s.duration)]
  print('\n'.join(sorted(l)))

def test_creature_cr_filter():
  ms = []
  for m in dl.monsters:
    if m.challenge_rating.cr <= 8:
      abbrs = [s.abbr for s in m.sources]
      # if 'MM' in abbrs or 'VGtM' in abbrs or 'MToF' in abbrs:
      if 'MM' in abbrs:
        ms += [m]
        # if 'fly' in m.speed.s.lower():
        #   ms += [m]
  monsters = sorted(ms, key=lambda m:m.challenge_rating.cr, reverse=True)
  print('\n'.join([f'{m.name}: {m.challenge_rating} - {[b.abbr for b in m.sources]}' for m in monsters]))
  
def test_create_polymorph_list():
  import clipboard, console
  console.clear()
  ms = []
  strout = ''
  monnames = ''
  for m in [dl.get_monster(monname) for monname in monnames.split(',')]:
    if 'MM' in [s.abbr for s in m.sources] and 'beast' in str(m.type).lower():
      if m.environment and 'urban' in m.environment:
        ms += [m]
  monsters = sorted(ms, key=lambda m:m.challenge_rating.cr, reverse=True)
  strout += '| CR | Name | HP | AC | Size | Movement | Senses | Weak | Resist | Immune |\n|:---:|:--- |:---:|:---:|:---:|:--- |:--- |:--- |:--- |:--- |\n'
  strout += '\n'.join([f'| {m.challenge_rating.cr_str} | [[{m.name}]] | {m.hit_points.hp} | {m.armor_class} | {m.size} | {m.speed} | {"–" if m.senses is None else m.senses} | {"–" if m.vulnerable is None else m.vulnerable} | {"–" if m.resist is None else m.resist} | {"–" if m.immune is None else m.immune} |' for m in monsters])
  # strout = '\n'.join([f'{m.name}' for m in monsters])
  clipboard.set(strout)
  print(strout)
  # cr, name, hp, ac, str dex con int wis cha, movement
  
def make_monster_csv():
  txt = ''
  def get_src_and_pg(m):
    src = ''
    pg = None
    for s in m.sources:
      if s is not None and s.abbr is not None:
        src = s.abbr
        pg = s.p
        break
    return src, pg
    
  def make_terrain_cells(env):
    if not env:
      return ''
    terrains = ['arctic', 'badlands', 'coastal', 'desert', 'farmland', 'forest', 'grassland', 'hills', 'mountains', 'planar', 'ruins', 'swamp', 'underground', 'underwater', 'urban']
    subs = { 'mountain': 'mountains', 'underdark': 'underground', 'hill': 'hills' }
    envs = [e.strip().lower() for e in env.split(',')]
    envs = [subs[e] if e in subs else e for e in envs]
    flags = [False] * len(terrains)
    for env in envs:
      flags[terrains.index(env)] = True
    return '\t'.join(['X' if f else '' for f in flags])
    
  # id	Monster	Size	Type	Alignment	CR	Source	Page	Terrain
  envs = []
  for m in dl.monsters:
    src, pg = get_src_and_pg(m)
    envcells = make_terrain_cells(m.environment)
    if src not in ['CC', 'ToB']:
      txt += f'###\t{m.name}\t{m.size}\t{m.type}\t{m.alignment}\t{m.challenge_rating.cr}\t{src}\t{pg}\t{m.environment}\t{envcells}\n'
      # print(f'###\t{m.name}\t{m.size}\t{m.type}\t{m.alignment}\t{m.challenge_rating.cr}\t{src}\t{pg}\t{m.environment}\t{envcells}')
  clipboard.set(txt)
  print("copied to clipboard")

def main():
  test_create_polymorph_list()
  

if __name__ == "__main__":
  main()

