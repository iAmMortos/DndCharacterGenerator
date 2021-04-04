
class ViewSwap (object):

  def __init__(self, view=None):
    self._view = view

  def swap(self, name, obj, view=None):
    v = view
    if v == None:
      v = self.view
    if v == None:
      raise Exception('No view given in constructor or in swap call.')

    pl = v[name]
    if pl == None:
      raise Exception('No subview found with name: %s' % name)

    obj.frame = pl.frame
    obj.flex = pl.flex
    v.remove_subview(pl)
    v.add_subview(obj)

  @property
  def view(self):
    return self._view

