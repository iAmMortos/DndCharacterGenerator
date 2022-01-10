
def get_ord_str(num):
  o = 'th'
  v = num % 10
  if v == 1 and num != 11:
    o = 'st'
  elif v == 2 and num != 12:
    o = 'nd'
  elif v == 3 and num != 13:
    o = 'rd'
  return f'{num}{o}'
