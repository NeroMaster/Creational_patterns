from shape import Shape, Color
from circle import Circle
from rectangle import Rectangle

def chechEquality(core: list[Shape], copies: list[Shape]):
  copies = [next.clone() for next in core]
  for i,_ in enumerate(core):
    domain: Shape = core[i]
    clone: Shape = copies[i]
    if domain != clone:
      print(f"Shapes at index {i} are different objects!")
    if domain == clone:
      print(f"Shapes at index {i} are equal!")

def main():
  core: list[Shape] = []
  copies: list[Shape] = []

  circle = Circle(10, 10, Color.BLUE, 5)
  core.append(circle)
  
  rectangle = Rectangle(10, 15, Color.RED, 5, 5)
  core.append(rectangle)

  chechEquality(core, copies)
  
if __name__ == "__main__":
  main()
