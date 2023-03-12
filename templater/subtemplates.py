import enum

class SubTemplates (enum.Enum):
  proficiencies = 'Proficiencies'
  spell = 'Spell'
  monster = 'Monster'
  

  @classmethod
  def list(cls):
    return list(map(lambda c: c.value, cls))
    
  @classmethod
  def of(cls, value):
    if type(value) is cls:
      return value
    elif type(value) is not str:
      value = type(value).__name__
      
    for e in cls:
      if e.value == value:
        return e
    raise Exception(f'No such template exists: [{value}]. Available templates are: {cls.list()}')
  

if __name__ == "__main__":
  print(SubTemplates.of('Spell'))
  try:
    print(SubTemplates.of('Test'))
  except Exception as ex:
    print(f"Error caught: {ex}")
  print(type(SubTemplates.monster) is SubTemplates)
  
  class Monster (object):
    pass
    
  print(SubTemplates.of(Monster()))
