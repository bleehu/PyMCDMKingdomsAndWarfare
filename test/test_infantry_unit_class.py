import pytest
from ..KingdomsAndWarfare.Units.Infantry import Infantry
from ..KingdomsAndWarfare.Units.Unit import Unit

def test_infantry():
    splonks_infantry = Infantry("splonks_infantry Infantry", "splonks_infantry with butterknives")
    assert splonks_infantry.name == "splonks_infantry Infantry"
    assert splonks_infantry.experience == Unit.Experience.REGULAR
    assert splonks_infantry.type == Unit.Type.INFANTRY

def test_infantry_level_up():
    teddy_bear_infantry = Infantry("Teddy Bear Infantry", "Teddy Bears with Toy Swords")
    teddy_bear_infantry.attack = 0
    teddy_bear_infantry.defense = 10
    teddy_bear_infantry.morale = 0
    teddy_bear_infantry.command = 0
    assert teddy_bear_infantry.experience == Unit.Experience.REGULAR
    teddy_bear_infantry.level_up()
    #assert stats were changed by level up correctly
    #magic numbers provided by table from MCDM K&W page 99
    assert teddy_bear_infantry.attack == 1
    assert teddy_bear_infantry.defense == 12
    assert teddy_bear_infantry.morale == 2
    assert teddy_bear_infantry.command == 2

def test_infantry_upgrade():
    pass