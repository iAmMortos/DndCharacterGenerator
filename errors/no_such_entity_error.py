
class NoSuchEntityError(Exception):
  def __init__(self, name, typ=None):
    super().__init__(f'No {"entity" if not typ else typ} named [{name}] exists in Data Loader.')

