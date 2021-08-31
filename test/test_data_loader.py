import test_context

from model.data_loader import DataLoader
from utils.regexes import get_sources

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()


def main():
  # find_dupes()
  iterate()


def iterate():
  for bg in dl.backgrounds:
    has = False
    for t in bg.traits:
      if t.name == 'Description':
        has = True
    if not has:
      print(bg.name)


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