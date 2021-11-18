import test_context

from model.data_loader import DataLoader
from utils.regexes import get_sources
from utils.regexes import is_attack

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()


def main():
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


if __name__ == "__main__":
  main()
