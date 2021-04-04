
import ui
import time
from threading import Thread


class AnimatedImageView (ui.View):
  def __init__(self, fps=60, frames=[]):
    self._cur_frame_idx = 0
    self._fps = fps
    self._thread = None
    self._running = False
    self._frames = frames
    self._loop = True
    self._img = ui.ImageView()
    self._img.frame = self.frame
    self._img.flex = 'WH'
    self.add_subview(self._img)

    self.onanimationfinished = lambda: None

  @property
  def loop(self):
    return self._loop

  @loop.setter
  def loop(self, val):
    if type(val) == bool:
      self._loop = val
    else:
      raise TypeError('Type of given value must be bool')

  @property
  def fps(self):
    return self._fps

  @fps.setter
  def fps(self, val):
    if type(val) == int and val >= 0:
      self._fps = val
    else:
      raise TypeError('Given value must be a non-negative int')

  @property
  def frames(self):
    return self._frames

  @frames.setter
  def frames(self, vals):
    self._frames = vals

  def _do_thread(self):
    while self._running:
      first = time.time()
      if self._cur_frame_idx in range(len(self._frames)):
        self._img.image = self._frames[self._cur_frame_idx]
        self._cur_frame_idx += 1
        elapsed = time.time() - first
        spf = 1 / self.fps
        if elapsed < spf:
          time.sleep(spf - elapsed)
      else:
        if len(self._frames) == 0 or not self.loop:
          self._running = False
        else:
          self._cur_frame_idx = 0

  def is_running(self):
    return self._running

  @ui.in_background
  def start(self):
    Thread(target=self._do_start).start()

  def _do_start(self):
    self._cur_frame_idx = 0
    self._thread = Thread(target=self._do_thread)
    self._running = True
    self._thread.start()
    self._thread.join()
    self.onanimationfinished()

  def stop(self):
    self._running = False

if __name__ == '__main__':
  AnimatedImageView()

