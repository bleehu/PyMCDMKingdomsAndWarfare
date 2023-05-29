from pdb import set_trace

import pytest

from ..KingdomsAndWarfare.Traits.Trait import Trait
from ..KingdomsAndWarfare.Units.Unit import CannotLevelUpError
from ..KingdomsAndWarfare.Units.Unit import CannotUpgradeError
from ..KingdomsAndWarfare.Units.Unit import Unit


# testing the unit class, not to be confused with unit tests...
# ... ok, these are unit tests, too, but still...
def test_unit():
    unit_name = "Splonks Infantry"
    unit_description = "Splonks with swords, mostly."
    splonks = Unit(unit_name, unit_description, Unit.Type.INFANTRY)

    assert splonks.name == unit_name
    assert splonks.description == unit_description

    magic_resistant = Trait("Magic Resistant", "this unit is resitant to magic")
    splonks.add_trait(magic_resistant)
    test_trait = splonks.traits[0]
    assert test_trait == magic_resistant


def test_levelup():
    splonks = Unit("Splonks Infantry", "Splonks with knives.", Unit.Type.INFANTRY)
    assert splonks.battles == 0
    assert splonks.experience == Unit.Experience.REGULAR
    splonks.battle()
    assert splonks.battles == 1
    assert splonks.experience == Unit.Experience.VETERAN
    splonks.battle()
    splonks.battle()
    splonks.battle()
    assert splonks.battles == 4
    assert splonks.experience == Unit.Experience.ELITE
    for index in range(4):
        splonks.battle()
    assert splonks.battles == 8
    assert splonks.experience == Unit.Experience.SUPER_ELITE
    with pytest.raises(CannotLevelUpError):
        splonks.level_up()


def test_levelup_levies():
    splonks = Unit(
        "Splonks levies", "Splonk levies use pumpkins as balaclavas.", Unit.Type.INFANTRY
    )
    splonks.experience = Unit.Experience.LEVIES
    with pytest.raises(CannotLevelUpError):
        splonks.level_up()


def test_upgrade_infantry():
    infantry = Unit("Splonks Infantry", "Splonkitude", Unit.Type.INFANTRY)
    assert infantry.equipment == Unit.Equipment.LIGHT
    infantry.upgrade()
    assert infantry.equipment == Unit.Equipment.MEDIUM
    infantry.upgrade()
    assert infantry.equipment == Unit.Equipment.HEAVY
    infantry.upgrade()
    assert infantry.equipment == Unit.Equipment.SUPER_HEAVY
    with pytest.raises(CannotUpgradeError):
        infantry.upgrade()


def test_upgrade_levies():
    levies = Unit("Splonks Levies", "Cucumbers", Unit.Type.INFANTRY)
    levies.experience = Unit.Experience.LEVIES
    with pytest.raises(CannotUpgradeError):
        levies.upgrade()
