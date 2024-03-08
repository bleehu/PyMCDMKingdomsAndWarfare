from . import UnitEnums
from .UnitType import UnitType

class Aerial(UnitType):
    def level_up(experience: UnitEnums.Experience, attacks: int, attack: int, defense: int, morale: int, command: int) -> tuple[int, int, int, int, int]:
        attack = attack + 1
        defense = defense + 1
        morale = morale + 1
        command = command + 2
        if experience == UnitEnums.Experience.VETERAN:
            attacks = attacks + 1
        return attacks, attack, defense, morale, command

    def level_down(experience: UnitEnums.Experience, attacks: int, attack: int, defense: int, morale: int, command: int) -> tuple[int, int, int, int, int]:
        attack = attack - 1
        defense = defense - 1
        morale = morale - 1
        command = command - 2
        if experience == UnitEnums.Experience.ELITE:
            attacks = attacks - 1
        return attacks, attack, defense, morale, command

    def upgrade(equipment: UnitEnums.Equipment, power: int, toughness: int, damage: int) -> tuple[int, int, int]:
        """Upgrade a unit's equipment bonuses. This is usually done by spending gold."""
        power = power + 1
        toughness = toughness + 1
        if equipment == UnitEnums.Equipment.HEAVY:
            damage = damage + 1
        return power, toughness, damage

    def downgrade(equipment: UnitEnums.Equipment, power: int, toughness: int, damage: int) -> tuple[int, int, int]:
        """Downgrade a unit's equipment bonuses. This is usualy the 'undo' function for upgrading."""
        power = power - 1
        toughness = toughness - 1
        if equipment == UnitEnums.Equipment.SUPER_HEAVY:
            damage = damage - 1
        return power, toughness, damage
