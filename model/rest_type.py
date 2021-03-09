
from enum import Enum


class RestType (Enum):
  S = "short rest"
  L = "long rest"

  def __str__(self):
    return self.value

  @staticmethod
  def of_value(val):
    try:
      return RestType.__getitem__(val)
    except Exception as ex:
      raise ValueError("No enum value available for string [%s]" % val)
