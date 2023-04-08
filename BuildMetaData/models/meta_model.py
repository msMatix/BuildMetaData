import json
from dataclasses import dataclass
from enum import Enum


class EWeaponType(Enum):
    GUN = "GUN"
    BOW = "BOW"
    MELEE = "MELEE"
    WAND = "WAND"


class EArmorType(Enum):
    HELMET = "HELMET"
    BRACERS = "BRACERS"
    LEGGINGS = "LEGGINGS"
    CHEST = "CHEST"
    WAIST = "WAIST"


class ERarity(Enum):
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"


@dataclass
class ImageMetaModel:
    name: str
    description: str
    image_url: str
    rarity: str
    weapon_type: str
    armor_type: str
    damage: int
    range: int
    movement_speed: int
    attack_speed: int

    def get_meta_data_of_nft(self) -> str:
        meta_data = {
            "name": self.name,
            "description": self.description,
            "image_url": self.image_url,
            "rarity": self.rarity,
            "weapon_type": self.weapon_type,
            "armor_type": self.armor_type,
            "damage": self.damage,
            "range": self.range,
            "movement_speed": self.movement_speed,
            "attack_speed": self.attack_speed,
        }
        return json.dumps(meta_data)
