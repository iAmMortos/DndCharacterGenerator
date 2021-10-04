import test_context

from model.data_loader import DataLoader
from utils.regexes import get_sources
from utils.regexes import is_attack

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()


def main():
  for m in dl.monsters:
    for a in m.actions:
      if is_attack(a.text) and '\n' in a.text:
        print(f'{m.name}: {a.name}')


if __name__ == "__main__":
  main()
