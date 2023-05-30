from enum import Enum
from enum import IntEnum
from pdb import set_trace

from ..Traits import Trait


class Unit:
    class Type(Enum):
        INFANTRY = 1
        ARTILLERY = 2
        CAVALRY = 3
        AERIAL = 4
    
    class Tier(IntEnum):
        I = 1
        II = 2
        III = 3
        IV = 4
        V = 5

    class Experience(IntEnum):
        LEVIES = 1
        REGULAR = 2
        VETERAN = 3
        ELITE = 4
        SUPER_ELITE = 5

    class Equipment(IntEnum):
        LIGHT = 1
        MEDIUM = 2
        HEAVY = 3
        SUPER_HEAVY = 4

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.battles = 0
        self.traits = []
        self.experience = Unit.Experience.REGULAR
        self.equipment = Unit.Equipment.LIGHT
        self.tier = Unit.Tier.I
        self.attack = 0
        self.defense = 10
        self.power = 0
        self.toughness = 10
        self.morale = 0
        self.command = 0
        self.damage = 1
        self.attacks = 1
        self.ancestry = ""

    def __eq__(self, __value: "Unit") -> bool:
        matches = self.name == __value.name \
            and self.ancestry == __value.ancestry \
            and self.attack == __value.attack \
            and self.attacks == __value.attacks \
            and self.battles == __value.battles \
            and self.command == __value.command \
            and self.damage == __value.damage \
            and self.defense == __value.defense \
            and self.description == __value.description \
            and self.equipment == __value.equipment \
            and self.experience == __value.experience \
            and self.morale == __value.morale \
            and self.power == __value.power \
            and self.tier == __value.tier \
            and self.toughness == __value.toughness \
            and self.traits == __value.traits \
            and self.type == __value.type
        return matches

    def add_trait(self, trait: Trait):
        if len(self.traits) < 5:
            self.traits.append(trait)
        else:
            raise Exception("This unit already has 4 traits!")

    def battle(self):
        self.battles = self.battles + 1
        if self.experience != Unit.Experience.LEVIES:
            if self.battles == 1 or self.battles == 4 or self.battles == 8:
                self.level_up()

    def upgrade(self):
        if self.experience == Unit.Experience.LEVIES:
            raise CannotUpgradeError("Cannot upgrade Levies")
        if self.equipment == Unit.Equipment.SUPER_HEAVY:
            raise CannotUpgradeError("Cannot upgrade equipment past super-heavy.")
        self.equipment = self.equipment + 1
    
    def downgrade(self):
        if self.experience == Unit.Experience.LEVIES:
            raise CannotUpgradeError("Cannot downgrade Levies")
        if self.equipment == Unit.Equipment.LIGHT:
            raise CannotUpgradeError("Cannot downgrade equipment below Light")
        self.equipment = self.equipment - 1

    def level_up(self):
        if self.experience == Unit.Experience.LEVIES:
            raise CannotLevelUpError("Cannot level up levies.")
        if self.experience == Unit.Experience.SUPER_ELITE:
            raise CannotLevelUpError("Cannot level up a unit past Super-elite.")
        self.experience = self.experience + 1

    def level_down(self):
        if self.experience == Unit.Experience.LEVIES:
            raise CannotLevelUpError("Cannot level down levies.")
        if self.experience == Unit.Experience.REGULAR:
            raise CannotLevelUpError("Cannot lower level below regular.")
        self.experience = self.experience - 1


class CannotUpgradeError(Exception):
    pass


class CannotLevelUpError(Exception):
    pass
