from character_builder import CharacterBuilder
from component.archetype import Archetype
from component.body import Body, Sex, Race, Hair
from component.weapon import Weapon, WeaponType
from component.armor import Armor, ArmorType
from character import Character
from director import Director


def classic_builder():
  builder = CharacterBuilder()
  builder.set_name("Aragorn")
  builder.set_archetype(Archetype.WARRIOR)
  builder.set_body(
    Body(Sex.MALE, Race.HUMAN, Hair.BROWN)
  )
  builder.set_armor(
    Armor(ArmorType.LEATHER, 5, "Fine Leather Armor")
  )
  builder.set_weapon(
    Weapon(WeaponType.SWORD, 15, "Anduril")
  )
  aragorn: Character = builder.get_result()
  print(aragorn)

def directed_builder():
  director = Director()
  moria_fighter = director.get_moria_fighter("Druma")
  rivendell_bowman = director.get_rivendell_bowman("Ellarial")
  rohan_spearman = director.get_rohan_spearman("John")
  white_wizard = director.get_white_wizard("Uzmar")

  print(moria_fighter)
  print(rivendell_bowman)
  print(rohan_spearman)
  print(white_wizard)

def main():
  classic_builder()
  directed_builder()

if __name__ == "__main__":
  main()
