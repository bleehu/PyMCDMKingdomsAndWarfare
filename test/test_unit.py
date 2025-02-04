from copy import deepcopy
from pdb import set_trace

import pytest

from ..KingdomsAndWarfare.Traits.Trait import Trait
from ..KingdomsAndWarfare.Units.Aerial import Aerial
from ..KingdomsAndWarfare.Units.Artillery import Artillery
from ..KingdomsAndWarfare.Units.Cavalry import Cavalry
from ..KingdomsAndWarfare.Units.Infantry import Infantry
from ..KingdomsAndWarfare.Units.Unit import CannotLevelUpError
from ..KingdomsAndWarfare.Units.Unit import CannotUpgradeError
from ..KingdomsAndWarfare.Units.Unit import Unit
from ..KingdomsAndWarfare.Units.UnitFactory import parse_equipment
from ..KingdomsAndWarfare.Units.UnitFactory import parse_experience
from ..KingdomsAndWarfare.Units.UnitFactory import parse_type
from ..KingdomsAndWarfare.Units.UnitFactory import unit_from_dict
from ..KingdomsAndWarfare.Units import UnitEnums


# testing the unit class, not to be confused with unit tests...
# ... ok, these are unit tests, too, but still...
def test_unit():
    unit_name = "Splonks Infantry"
    unit_description = "Splonks with swords, mostly."
    splonks = Unit(unit_name, Infantry, unit_description)

    assert splonks.name == unit_name
    assert splonks.description == unit_description

    magic_resistant = Trait("Magic Resistant", "this unit is resitant to magic")
    splonks.add_trait(magic_resistant)
    test_trait = splonks.traits[0]
    assert test_trait == magic_resistant


def test_levelup():
    splonks = Unit("Splonks Infantry", Infantry, "Splonks with knives.")
    assert splonks.battles == 0
    assert splonks.experience == UnitEnums.Experience.REGULAR
    splonks.battle()
    assert splonks.battles == 1
    assert splonks.experience == UnitEnums.Experience.VETERAN
    splonks.battle()
    splonks.battle()
    splonks.battle()
    assert splonks.battles == 4
    assert splonks.experience == UnitEnums.Experience.ELITE
    for index in range(4):
        splonks.battle()
    assert splonks.battles == 8
    assert splonks.experience == UnitEnums.Experience.SUPER_ELITE
    with pytest.raises(CannotLevelUpError):
        splonks.level_up()


def test_level_up_undo():
    units = [
        Unit("Goldfish Infantry", Infantry, "Goldfish with lightsabers"),
        Unit("Gunslingers", Artillery, "Slingers who throw guns"),
        Unit("Rhino Cavalry", Cavalry, "Rhinos riding very large horses"),
    ]
    for unit in units:
        assert unit.experience == UnitEnums.Experience.REGULAR
        my_clone = deepcopy(unit)
        unit.level_up()
        unit.level_up()
        unit.level_up()
        assert unit.experience == UnitEnums.Experience.SUPER_ELITE
        unit.level_down()
        unit.level_down()
        unit.level_down()
        assert unit.experience == UnitEnums.Experience.REGULAR
        assert my_clone == unit


def test_level_up_undo():
    units = [
        Unit("Goldfish Infantry", Infantry, "Goldfish with lightsabers"),
        Unit("Gunslingers", Artillery, "Slingers who throw guns"),
        Unit("Rhino Cavalry", Cavalry, "Rhinos riding very large horses"),
    ]
    for unit in units:
        assert unit.experience == UnitEnums.Experience.REGULAR
        my_clone = deepcopy(unit)
        unit.level_up()
        unit.level_up()
        unit.level_up()
        assert unit.experience == UnitEnums.Experience.SUPER_ELITE
        unit.level_down()
        unit.level_down()
        unit.level_down()
        assert unit.experience == UnitEnums.Experience.REGULAR
        assert my_clone == unit


def test_levelup_levies():
    splonks = Unit("Splonks levies", Infantry, "Splonk levies use pumpkins as balaclavas.")
    splonks.experience = UnitEnums.Experience.LEVIES
    with pytest.raises(CannotLevelUpError):
        splonks.level_up()


def test_upgrade_infantry():
    infantry = Unit("Splonks Infantry", Infantry, "Splonkitude")
    assert infantry.equipment == UnitEnums.Equipment.LIGHT
    infantry.upgrade()
    assert infantry.equipment == UnitEnums.Equipment.MEDIUM
    infantry.upgrade()
    assert infantry.equipment == UnitEnums.Equipment.HEAVY
    infantry.upgrade()
    assert infantry.equipment == UnitEnums.Equipment.SUPER_HEAVY
    with pytest.raises(CannotUpgradeError):
        infantry.upgrade()


def test_upgrade_undo():
    units = [
        Unit("Creepy Puppets", Infantry, "Puppets on magical strings."),
        Unit("Fish People", Artillery, "Fish people with squirtguns."),
        Unit("Sand People", Cavalry, "Riding Speeder bikes."),
    ]
    for unit in units:
        my_clone = deepcopy(unit)
        assert unit.equipment == UnitEnums.Equipment.LIGHT
        unit.upgrade()
        unit.upgrade()
        unit.upgrade()
        assert unit.equipment == UnitEnums.Equipment.SUPER_HEAVY
        unit.downgrade()
        unit.downgrade()
        unit.downgrade()
        assert unit.equipment == UnitEnums.Equipment.LIGHT
        assert unit == my_clone


def test_upgrade_undo():
    units = [
        Unit("Creepy Puppets", Infantry, "Puppets on magical strings."),
        Unit("Fish People", Artillery, "Fish people with squirtguns."),
        Unit("Sand People", Cavalry, "Riding Speeder bikes."),
    ]
    for unit in units:
        my_clone = deepcopy(unit)
        assert unit.equipment == UnitEnums.Equipment.LIGHT
        unit.upgrade()
        unit.upgrade()
        unit.upgrade()
        assert unit.equipment == UnitEnums.Equipment.SUPER_HEAVY
        unit.downgrade()
        unit.downgrade()
        unit.downgrade()
        assert unit.equipment == UnitEnums.Equipment.LIGHT
        assert unit == my_clone


def test_upgrade_levies():
    levies = Unit("Splonks Levies", Infantry, "Cucumbers")
    levies.experience = UnitEnums.Experience.LEVIES
    with pytest.raises(CannotUpgradeError):
        levies.upgrade()


def test_typical_use():
    catapult = Unit("Catapult", Infantry, "Cats with heavy pulitzer prize trophies.")
    seige_weapon = Trait("Seige Weapon", "These cats will lay seige until given pets.")
    assert catapult.attacks == 1
    assert catapult.attack == 0
    assert catapult.defense == 10
    assert catapult.power == 0
    assert catapult.toughness == 10
    assert catapult.morale == 0
    assert catapult.command == 0
    assert catapult.experience == UnitEnums.Experience.REGULAR
    assert catapult.equipment == UnitEnums.Equipment.LIGHT
    catapult.add_trait(seige_weapon)
    clone = deepcopy(catapult)
    catapult.upgrade()
    catapult.level_up()
    assert catapult.attacks == 1
    assert catapult.attack == 1
    assert catapult.defense == 12
    assert catapult.power == 2
    assert catapult.toughness == 12
    assert catapult.morale == 2
    assert catapult.command == 1
    assert catapult.experience == UnitEnums.Experience.VETERAN
    assert catapult.equipment == UnitEnums.Equipment.MEDIUM
    saved = catapult.to_dict()
    loaded = unit_from_dict(saved)
    assert loaded.attacks == 1
    assert loaded.attack == 1
    assert loaded.defense == 12
    assert loaded.power == 2
    assert loaded.toughness == 12
    assert loaded.morale == 2
    assert loaded.command == 1
    assert loaded.experience == UnitEnums.Experience.VETERAN
    assert loaded.equipment == UnitEnums.Equipment.MEDIUM
    loaded.upgrade()
    loaded.level_up()
    # infantry leveled up twice to elite, heavy
    assert loaded.attacks == 2
    assert loaded.attack == 2
    assert loaded.defense == 14
    assert loaded.power == 4
    assert loaded.toughness == 14
    assert loaded.morale == 4
    assert loaded.command == 1
    loaded.level_down()
    loaded.level_down()
    loaded.downgrade()
    loaded.downgrade()
    assert loaded == clone

def test_infantry_attack():
    attacker = Unit("Attacker", Infantry, "The attacker in the test scenario.")
    attacker.attack = 1
    attacker.power = 1
    attacker.damage = 1
    target = Unit("Defender", Infantry, "The Defender in the test scenario.")
    target.defense = 11
    target.toughness = 11
    target.size = 6
    target.casualties = 6
    assert target.casualties == 6
    attacker.attack_unit(target, 9, 9) #this attack should miss
    assert target.casualties == 6
    attacker.attack_unit(target, 10, 9) #the attack test should win, the power test should miss, dealing exactly 1 casualty
    assert target.casualties == 5
    attacker.attack_unit(target, 10, 10) #both attack and power succeed, dealing 2 casualties
    assert target.casualties == 3
    assert target.get_diminished()


def test_parse_type():
    assert parse_type(Infantry.__qualname__) == Infantry
    assert parse_type(Cavalry.__qualname__) == Cavalry
    assert parse_type(Artillery.__qualname__) == Artillery
    assert parse_type(Aerial.__qualname__) == Aerial


def test_parse_equipment():
    assert parse_equipment("light") == UnitEnums.Equipment.LIGHT
    assert parse_equipment("medium") == UnitEnums.Equipment.MEDIUM
    assert parse_equipment("heavy") == UnitEnums.Equipment.HEAVY
    assert parse_equipment("super_heavy") == UnitEnums.Equipment.SUPER_HEAVY
    assert parse_equipment("EQUIPMENT.LIGHT") == UnitEnums.Equipment.LIGHT
    assert parse_equipment("EQUIPMENT.MEDIUM") == UnitEnums.Equipment.MEDIUM
    assert parse_equipment("EQUIPMENT.HEAVY") == UnitEnums.Equipment.HEAVY
    assert parse_equipment("EQUIPMENT.SUPER_HEAVY") == UnitEnums.Equipment.SUPER_HEAVY
    assert parse_equipment("1") == UnitEnums.Equipment.LIGHT
    assert parse_equipment("2") == UnitEnums.Equipment.MEDIUM
    assert parse_equipment("3") == UnitEnums.Equipment.HEAVY
    assert parse_equipment("4") == UnitEnums.Equipment.SUPER_HEAVY


def test_parse_experience():
    assert parse_experience("regular") == UnitEnums.Experience.REGULAR
    assert parse_experience("veteran") == UnitEnums.Experience.VETERAN
    assert parse_experience("elite") == UnitEnums.Experience.ELITE
    assert parse_experience("super_elite") == UnitEnums.Experience.SUPER_ELITE
    assert parse_experience("levies") == UnitEnums.Experience.LEVIES
    assert parse_experience("EXPERIENCE.REGULAR") == UnitEnums.Experience.REGULAR
    assert parse_experience("EXPERIENCE.VETERAN") == UnitEnums.Experience.VETERAN
    assert parse_experience("EXPERIENCE.ELITE") == UnitEnums.Experience.ELITE
    assert parse_experience("EXPERIENCE.SUPER_ELITE") == UnitEnums.Experience.SUPER_ELITE
    assert parse_experience("EXPERIENCE.LEVIES") == UnitEnums.Experience.LEVIES
    assert parse_experience("1") == UnitEnums.Experience.LEVIES
    assert parse_experience("2") == UnitEnums.Experience.REGULAR
    assert parse_experience("3") == UnitEnums.Experience.VETERAN
    assert parse_experience("4") == UnitEnums.Experience.ELITE
    assert parse_experience("5") == UnitEnums.Experience.SUPER_ELITE
