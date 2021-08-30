import test_context
from model.data_loader import DataLoader
from utils.regexes import *


def main():
  dl = DataLoader('data/xml/Complete.xml')
  for m in dl.monsters:
    for a in m.actions:
      if a.text and is_attack(a.text):
        gs = get_attack(a.text)
        if not gs:
          print(m.name)
          print(a.name)
          print(a.text)
          exit(1)
        print(f'{gs[0]}: {gs[1]}\n  Hit: {gs[2]}')

if __name__ == "__main__":
  main()