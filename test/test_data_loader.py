import test_context

from model.data_loader import DataLoader

dl = DataLoader('data/xml/Complete.xml')
dl.print_stats()

# for m in dl.monsters:
#   for a in m.actions:
#     if a.attack:
#       if 'Melee' not in a.text and 'Ranged' not in a.text:
#         n = a.name
#         # t = a.text.replace('\n', '\\n')
#         print(f'# {n}\n\t{a.text}')
n = dl.monsters['Neothelid']
print(n)
