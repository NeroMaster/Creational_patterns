from component.archetype import Archetype
from component.armor import Armor
from component.body import Body
from component.weapon import Weapon


class Character:
  _name: str
  _body: Body
  _archetype: Archetype
  _armor: Armor
  _weapon: Weapon

  def __init__(
    self, 
    name: str, 
    body: Body, 
    archetype: Archetype, 
    armor: Armor, 
    weapon: Weapon
  ):
    self._name = name
    self._body = body
    self._archetype = archetype
    self._armor = armor
    self._weapon = weapon

  def set_armor(self, armor: Armor):
    self._armor = armor

  def set_weapon(self, weapon: Weapon):
    self._weapon = weapon

  def get_name(self) -> str:
    return self._name

  def get_body(self) -> Body:
    return self._body

  def get_archetype(self) -> Archetype:
    return self._archetype

  def get_armor(self) -> Armor:
    return self._armor
    
  def get_weapon(self) -> Weapon:
    return self._weapon

  def __repr__(self):
    to_str = f"""
    My name is {self._name}
    I am a {self._body.get_sex()}
    My profession is {self._archetype}
    I wear {self._armor.get_armor_type()} and fight with {self._weapon.get_weapon_type()}
    """
    return to_str
