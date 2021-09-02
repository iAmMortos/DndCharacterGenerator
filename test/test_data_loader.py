import test_context

from model.data_loader import DataLoader
from utils.regexes import get_sources

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()


def main():
  # find_dupes()
  iterate()


def iterate():
  for cl in dl.classes:
    found = None
    for al in cl.auto_levels:
      if al.level == 1:
        for f in al.features:
          s = f.name if type(f.name) is str else ''.join(f.name)
          if s.startswith('Starting'):
            found = get_sources(''.join(f.text))
            break
    if not found:
      print(f'Missing Source: {cl.name}')
    else:
      print(f'{cl.name}: {found}')


def find_dupes():
  # for mn in dl.monsters:
  #   m = dl.monsters[mn]
  names = []
  dupes = []
  ls = dl.backgrounds

  for x in ls:
    if x.name in names:
      dupes += [x.name]
    else:
      names += [x.name]

  for x in ls:
    if x.name in dupes:
      print(x.name, get_sources(x.description), end="\n\n")


if __name__ == "__main__":
  main()
