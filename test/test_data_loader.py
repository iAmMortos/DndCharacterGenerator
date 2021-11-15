import test_context

from model.data_loader import DataLoader
from utils.regexes import get_sources
from utils.regexes import is_attack

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()


def main():
  fs = []
  for m in dl.monsters:
    print(f'{m.name}: {m.environment}')
      
  print(fs)


if __name__ == "__main__":
  pass
  # main()
