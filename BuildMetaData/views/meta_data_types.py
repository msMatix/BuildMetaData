from enum import Enum


class EWeaponType(Enum):
    NONE = ""
    GUN = "GUN"
    BOW = "BOW"
    MELEE = "MELEE"
    WAND = "WAND"


class EArmorType(Enum):
    NONE = ""
    HELMET = "HELMET"
    BRACERS = "BRACERS"
    LEGGINGS = "LEGGINGS"
    CHEST = "CHEST"
    WAIST = "WAIST"


class ERarity(Enum):
    NONE = ""
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"


class EDamage(Enum):
    NONE = 0
    LOW = 1
    MED = 2
    NORMAL = 3
    HIGH = 4
    VERY_HIGH = 5


class ERange(Enum):
    NONE = 0
    FIELD_1 = 1
    FIELD_2 = 2
    FIELD_3 = 3
    FIELD_5 = 5
    FIELD_7 = 7
    FIELD_10 = 10


class EMovementSpeed(Enum):
    NONE = 0
    M_SPEED_1 = 1
    M_SPEED_2 = 2
    M_SPEED_3 = 3
    M_SPEED_5 = 5


class EAttackSpeed(Enum):
    NONE = 0
    A_SPEED_1 = 1
    A_SPEED_2 = 2
    A_SPEED_3 = 3
    A_SPEED_5 = 5
