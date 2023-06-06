import pdb

from ..Traits.Trait import Trait
from .Unit import Unit
from .UnitType import UnitType
from . import UnitEnums


def unit_from_dict(new_unit_dict: dict) -> "Unit":
    new_unit = None
    new_type = parse_type(new_unit_dict["type"])
    new_name = new_unit_dict["name"]
    new_description = new_unit_dict["description"]
    if new_type == UnitEnums.Type.INFANTRY:
        new_unit = Unit(new_name, UnitEnums.Type.INFANTRY, new_description)
    elif new_type == UnitEnums.Type.CAVALRY:
        new_unit = Unit(new_name, UnitEnums.Type.CAVALRY, new_description)
    elif new_type == UnitEnums.Type.ARTILLERY:
        new_unit = Unit(new_name, UnitEnums.Type.ARTILLERY, new_description)
    elif new_type == UnitEnums.Type.AERIAL:
        new_unit = Unit(new_name, UnitEnums.Type.AERIAL, new_description)
    else:
        raise NoSuchUnitTypeError(
            f"Could not instantiate unit type of {new_type}. \
                                       Expected one of [Infantry, Cavalry, Artillery, Aerial]."
        )
    new_unit.battles = int(new_unit_dict["battles"])
    new_unit.traits = []
    for trait_dict in new_unit_dict["traits"]:
        new_unit.traits.append(Trait.from_dict(trait_dict))
    new_unit.experience = parse_experience(new_unit_dict["experience"])
    new_unit.equipment = parse_equipment(new_unit_dict["equipment"])
    new_unit.tier = new_unit_dict["tier"]
    new_unit.attack = int(new_unit_dict["attack"])
    new_unit.defense = int(new_unit_dict["defense"])
    new_unit.size = int(new_unit_dict["size"])
    new_unit.power = int(new_unit_dict["power"])
    new_unit.toughness = int(new_unit_dict["toughness"])
    new_unit.morale = int(new_unit_dict["morale"])
    new_unit.command = int(new_unit_dict["command"])
    new_unit.damage = int(new_unit_dict["damage"])
    new_unit.attacks = int(new_unit_dict["attacks"])
    new_unit.ancestry = new_unit_dict["ancestry"]
    return new_unit


def parse_type(type_string: str) -> UnitType:
    if len(type_string) == 1:
        type_int = int(type_string)
        if type_int < 1 or type_int > 4:
            raise NoSuchUnitTypeError()
        return UnitEnums.Type(type_int)
    type_name = type_string.upper().replace("TYPE.", "")
    if type_name not in ["INFANTRY", "ARTILLERY", "AERIAL", "CAVALRY"]:
        raise NoSuchUnitTypeError()
    return UnitEnums.Type[type_name]


def parse_experience(experience_string: str) -> UnitEnums.Experience:
    if len(experience_string) == 1:
        type_int = int(experience_string)
        if type_int < 1 or type_int > 5:
            raise NoSuchUnitExperienceError()
        return UnitEnums.Experience(type_int)
    type_name = experience_string.upper().replace("EXPERIENCE.", "")
    if type_name not in ["LEVIES", "REGULAR", "VETERAN", "ELITE", "SUPER_ELITE"]:
        raise NoSuchUnitExperienceError()
    return UnitEnums.Experience[type_name]


def parse_equipment(equipment_string: str) -> UnitEnums.Equipment:
    if len(equipment_string) == 1:
        type_int = int(equipment_string)
        if type_int < 1 or type_int > 4:
            raise NoSuchUnitEquipmentError()
        return UnitEnums.Equipment(type_int)
    type_name = equipment_string.upper().replace("EQUIPMENT.", "")
    if type_name not in ["LIGHT", "MEDIUM", "HEAVY", "SUPER_HEAVY"]:
        raise NoSuchUnitEquipmentError()
    return UnitEnums.Equipment[type_name]


class UnitError(Exception):
    pass


class NoSuchUnitTypeError(UnitError):
    pass


class NoSuchUnitExperienceError(UnitError):
    pass


class NoSuchUnitEquipmentError(UnitError):
    pass
