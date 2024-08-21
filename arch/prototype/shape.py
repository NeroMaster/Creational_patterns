from enum import Enum
from abc import ABCMeta, abstractmethod

class Color(Enum):
  RED = "RED"
  GREEN = "GREEN"
  BLUE = "BLUE"

class Shape():
  __metaclass__ = ABCMeta

  _x: int
  _y: int
  _color: Color

  def __init__(self, x: int, y: int, color: Color):
    self._x = x
    self._y = y
    self._color = color

  @abstractmethod
  def clone(self):
    pass

  def getX(self):
    return self.x
    
  def getY(self):
    return self.y
    
  def getColor(self):
    return self.color
