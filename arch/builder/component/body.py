from enum import Enum

class Sex(Enum):
  MALE = "MALE"
  FEMALE = "FEMALE"

class Hair(Enum):
  RED = "RED"
  BROWN = "BROWN"
  GOLDEN = "GOLDEN"
  BLACK = "BLACK" 
  WHITE = "WHITE"

class Race(Enum):
  HUMAN = "HUMAN"
  ORC = "ORC"
  ELF = "ELF"
  DWARF = "DWARF"
  
class Body:
  _sex: Sex
  _hair: Hair
  _race: Race

  def __init__(self, sex: Sex, race: Race, hair: Hair):
    self._sex = sex
    self._race = race
    self._hair = hair

  def get_sex(self) -> Sex:
    return self._sex

  def get_hair(self) -> Hair:
    return self._hair

  def get_race(self) -> Race:
    return self._race
