from component.archetype import Archetype
from component.armor import Armor
from component.body import Body
from component.weapon import Weapon
from character import Character

class CharacterBuilder:
  _name: str
  _body: Body
  _archetype: Archetype
  _armor: Armor
  _weapon: Weapon

  def get_result(self):
    return Character(self._name, self._body, self._archetype, self._armor, self._weapon)

  def set_name(self, name: str):
    self._name = name

  def set_body(self, body: Body):
    self._body = body

  def set_archetype(self, archetype: Archetype):
    self._archetype = archetype

  def set_armor(self, armor: Armor):
    self._armor = armor

  def set_weapon(self, weapon: Weapon):
    self._weapon = weapon
