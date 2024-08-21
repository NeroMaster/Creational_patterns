from enum import Enum

class ArmorType(Enum):
  CLOTH = "CLOTH"
  LEATHER = "LEATHER"
  CHAIN_MAIL = "CHAIN_MAIL"
  PLATE = "PLATE"

class Armor:
  _armor_type: ArmorType
  _durability: int
  _title: str

  def __init__(self, armor_type: ArmorType, durability: int, title: str):
    self._armor_type = armor_type
    self._durability = durability
    self._title = title

  def get_armor_type(self) -> ArmorType:
    return self._armor_type

  def get_durability(self) -> int:
    return self._durubility

  def get_title(self) -> str:
    return self._title
