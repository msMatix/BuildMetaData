from enum import Enum


class EEquipmentType(Enum):
    NONE = ""
    GUN = "GUN"
    BOW = "BOW"
    MELEE = "MELEE"
    WAND = "WAND"
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
    UNIQUE = "UNIQUE"


class EPower(Enum):
    NONE = ""
    LOW = "1"
    MED = "2"
    NORMAL = "3"
    HIGH = "4"
    VERY_HIGH = "5"


class EAttackSpeed(Enum):
    NONE = ""
    FIELD_1 = "1"
    FIELD_2 = "2"
    FIELD_3 = "3"
    FIELD_5 = "5"
    FIELD_7 = "7"
    FIELD_10 = "10"


class EWeight(Enum):
    NONE = ""
    M_WEIGHT_1 = "1"
    M_WEIGHT_2 = "2"
    M_WEIGHT_3 = "3"
    M_WEIGHT_5 = "5"


class EDefense(Enum):
    NONE = ""
    A_DEFENSE_1 = "1"
    A_DEFENSE_2 = "2"
    A_DEFENSE_3 = "3"
    A_DEFENSE_5 = "5"


class ESpecialEffect(Enum):
    NONE = ""
    SP_FIREBALL = "FIREBALL"
    SP_WATERBREATH = "WATERBREATH"
