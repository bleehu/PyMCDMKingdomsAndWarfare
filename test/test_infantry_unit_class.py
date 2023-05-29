import pytest
from ..KingdomsAndWarfare.Units.Infantry import Infantry
from ..KingdomsAndWarfare.Units.Unit import Unit

def test_infantry():
    Splonks = Infantry("Splonks Infantry", "Splonks with butterknives", Unit.Type.INFANTRY)
    assert Splonks.name == "Splonks Infantry"
    assert Splonks.experience == Unit.Experience.REGULAR