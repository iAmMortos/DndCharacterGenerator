import test_context
from model.background_traits import BackgroundTraits

bt = BackgroundTraits('data/background_traits.csv')
bg = bt.get_bg('Far Traveler')
print(bg.roll_all_tables())

bg = bt.get_random_bg()
d = bg.roll_all_tables()
print(d)

print(bg.get_traits_as_str())

srcs = []
for bg in bt.bgs.values():
  if bg.source not in srcs:
    srcs.append(bg.source)
print(srcs)
