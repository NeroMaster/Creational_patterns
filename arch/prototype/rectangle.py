from copy import deepcopy

from shape import Shape, Color


class Rectangle(Shape):
  _height: int
  _width: int

  def __init__(self, x:int, y:int, color:Color, height:int, width:int):
    super().__init__(x, y, color)
    self._height = height
    self._width = width
  
  def clone(self):
    return deepcopy(self)

  def __eq__(self, o: object):
    if self is o:
      return True
    if (o == None or type(self) != type(o)):
      return False
    rectangle: Rectangle = o
    return self._height == rectangle._height and self._width == rectangle._width

  def __hash__(self):
    return hash(self._height, self._width)
