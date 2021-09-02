import test_context

from model.data_loader import DataLoader
from utils.regexes import get_sources

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()


def main():
  for r in dl.races:
    found = []
    for t in r.traits:
      if t.name == 'Description':
        found = get_sources(t.text)
    if not found:
      print(f'MISSING: {r.name}')
    else:
      print(f'{r.name}: {found}')


if __name__ == "__main__":
  main()
