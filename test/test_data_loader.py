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


def main():
  for s in dl.spells:
    if s.name == "Shield of Faith":
      print(s.get_book_str())


if __name__ == "__main__":
  main()
