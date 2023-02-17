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
#		if 'instantaneous,' in str(s.duration).lower():
#			print(s.name)
		if str(s.duration) not in l:
			l += [str(s.duration)]
	print('\n'.join(sorted(l)))


def main():
	test_spells()
	
	
if __name__ == "__main__":
	main()

