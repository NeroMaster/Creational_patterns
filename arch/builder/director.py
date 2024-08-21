from character_builder import CharacterBuilder
from character import Character
from component.archetype import Archetype
from component.body import Body, Sex, Race, Hair
from component.armor import Armor, ArmorType
from component.weapon import Weapon, WeaponType

class Director:
  def get_rohan_spearman(self, name: str):
    builder = CharacterBuilder()
    builder.set_name(name)
    builder.set_archetype(Archetype.WARRIOR)
    builder.set_body(
      Body(Sex.MALE, Race.HUMAN, Hair.BROWN)
    )
    builder.set_armor(
      Armor(ArmorType.CHAIN_MAIL, 15, "Iron Chain Mail")
    )
    builder.set_weapon(
      Weapon(WeaponType.SPEAR, 5, "Long Spear")
    )
    return builder.get_result()
    
  def get_rivendell_bowman(self, name: str):
    builder = CharacterBuilder()
    builder.set_name(name)
    builder.set_archetype(Archetype.ARCHER)
    builder.set_body(
      Body(Sex.FEMALE, Race.ELF, Hair.GOLDEN)
    )
    builder.set_armor(
      Armor(ArmorType.LEATHER, 10, "Fine Leather Armour")
    )
    builder.set_weapon(
      Weapon(WeaponType.BOW, 10, "Longbow")
    )
    return builder.get_result()

  def get_moria_fighter(self, name: str):
    builder = CharacterBuilder()
    builder.set_name(name)
    builder.set_archetype(Archetype.WARRIOR)
    builder.set_body(
      Body(Sex.MALE, Race.DWARF, Hair.RED)
    )
    builder.set_armor(
      Armor(ArmorType.PLATE, 20, "Solid Plate Armour")
    )
    builder.set_weapon(
      Weapon(WeaponType.AXE, 20, "Great Axe")
    )
    return builder.get_result()

  def get_white_wizard(self, name: str):
    builder = CharacterBuilder()
    builder.set_name(name)
    builder.set_archetype(Archetype.WIZARD)
    builder.set_body(
      Body(Sex.MALE, Race.HUMAN, Hair.WHITE)
    )
    builder.set_armor(
      Armor(ArmorType.CLOTH, 5, "Fine Cloth")
    )
    builder.set_weapon(
      Weapon(WeaponType.STAFF, 15, "Magic Staff")
    )
    return builder.get_result()    
