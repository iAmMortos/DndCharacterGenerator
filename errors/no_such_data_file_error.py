
class NoSuchDataFileError(Exception):
  def __init__(self, path):
    super().__init__(f'No data file exists at path [{path}].')
