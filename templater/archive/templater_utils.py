def subappend(lst, item):
  laststr = len(lst) > 0 and type(lst[-1]) is str
  if type(item) is str and laststr:
    lst[-1] += item
  else:
    lst.append(item)

def subappendlist(lst, subs):
  laststr = len(lst) > 0 and type(lst[-1]) is str
  for sub in subs:
    if type(sub) is str:
      if laststr:
        lst[-1] += sub
      else:
        lst.append(sub)
      laststr = True
    else:
      lst.append(sub)
      laststr = False
    
