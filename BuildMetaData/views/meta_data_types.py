from enum import Enum


class EEquipmentType(Enum):
    NONE = ""
    HELMET = ("Helmet",)
    CHEST_ARMOR = ("ChestArmor",)
    BRACERS = ("Bracers",)
    BOOTS = ("Boots",)
    BOW_2H = ("Bow_2H",)
    SWORD_2H = ("Sword_2H",)
    SWORD_1H = ("Sword_1H",)
    AXE_2H = ("Axe_2H",)
    AXE_1H = ("Axe_1H",)
    HAMMER_2H = ("Hammer_2H",)
    HAMMER_1H = ("Hammer_1H",)
    LANCE_1H = ("Lance_1H",)
    GUN_1H = ("Gun_1H",)
    SHIELD_1H = ("Shield_1H",)
    WAND_1H = "Wand_1H"


class ERarity(Enum):
    NONE = ""
    COMMON = "Common"
    UNCOMMON = "Uncommen"
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
    SP_FIREBALL = "FIREBALL"
    SP_WATERBREATH = "WATERBREATH"
