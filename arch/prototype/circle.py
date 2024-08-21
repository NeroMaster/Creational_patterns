from copy import deepcopy

from shape import Shape, Color

class Circle(Shape):
  _radius: int

  def __init__(self, x: int, y: int, color: Color, radius: int):
    super().__init__(x, y, color)
    self._radius = radius

  def clone(self):
    return deepcopy(self)

  def getRadius(self):
    return self._radius

  def __eq__(self, o: object):
    if self is o:
      return True
    if (o == None or type(self) != type(o)):
      return False
    circle: Circle = o
    return self._radius == circle._radius
    
  def __hash__(self):
    return hash(self.radius)
