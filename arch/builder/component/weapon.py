from enum import Enum

class WeaponType(Enum):
  SPEAR = "SPEAR"
  SWORD = "SWORD"
  AXE = "AXE"
  BOW = "BOW"
  STAFF = "STAFF"

class Weapon:
  _weapon_type: WeaponType
  _damage: int
  _title: str

  def __init__(self, weapon_type: WeaponType, damage: int, title: str):
    self._weapon_type = weapon_type
    self._damage = damage
    self._title = title

  def get_weapon_type(self) -> WeaponType:
    return self._weapon_type

  def get_damage(self) -> int:
    return self._damage

  def get_title(self) -> str:
    return self._title
