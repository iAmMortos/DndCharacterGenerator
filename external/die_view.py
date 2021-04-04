
import os
from external.animated_image_view import AnimatedImageView
from external.img_utils import pil2ui

from PIL import Image
import random


class DieView (AnimatedImageView):

  _faces = [pil2ui(Image.open('external/die_face_%s.png' % (n))) for n in range(1,7)]

  def __init__(self, callback=lambda: None):
    super().__init__()
    self._rolling = False
    self._enabled = True
    self.loop = False
    self.callback = callback
    self.onanimationfinished = self._post_roll_action
    self.border_color = '#ff4f11'
    self.corner_radius = 10
    self.set_value(6)

  @property
  def enabled(self):
    return self._enabled

  @enabled.setter
  def enabled(self, val):
    self._enabled = val
    self.border_width = 2 if val else 0
    self._set_img_enabled(val)

  #resets without calling hold change
  def reset(self):
    self.set_value(6)
    self.border_width = 0

  def _set_img_enabled(self, val):
    self._img.alpha = 0.5 if not val else 1

  def _post_roll_action(self):
    self._rolling = False
    self.set_value(self._val)
    self.callback()
    self.border_width = 2 if self.enabled else 0

  def roll(self):
    self.border_width = 0
    self.roll_to(random.randint(1,6))

  def roll_to(self, val):
    self._rolling = True
    self._val = val
    self.frames = []
    self.fps = random.randint(10,20)
    last = random.randint(0,5)
    for _ in range(random.randint(10,30)):
      ints = list(range(6))
      ints.remove(last)
      idx = random.choice(ints)
      last = idx
      self.frames += [DieView._faces[idx]]
    self.start()

  def set_value(self, val):
    self._val = val
    self._img.image = DieView._faces[val-1]

