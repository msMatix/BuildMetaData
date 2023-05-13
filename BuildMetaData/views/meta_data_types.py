from enum import Enum


class EBaseEquipment(Enum):
    ARMOR = "armor"
    SHIELD = "shield"
    WEAPON = "weapon"
    BASE = "base"


class EEquipmentType(Enum):
    NONE = ""
    Helmet = "Helmet"
    Armor = "Armor"
    Bracers = "Bracers"
    Boots = "Boots"
    Bow = "Bow"
    Sword = "Sword"
    Axe = "Axe"
    Hammer = "Hammer"
    Lance = "Lance"
    Gun = "Gun"
    Shield = "Shield"
    Wand = "Wand"


class ERarity(Enum):
    NONE = ""
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"
    UNIQUE = "Unique"


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
    SP_FIREBALL = "FIREBALL_1"
    SP_WATERBREATH = "WATERBREATH_1"


class EEquipmentSet(Enum):
    NONE = ""
    DIVINE = "Divine"
    DARK_METAL = "DarkMetal"


class EEquipmentRange(Enum):
    NONE = ""
    RANGE_1 = "1"
    RANGE_5 = "5"
