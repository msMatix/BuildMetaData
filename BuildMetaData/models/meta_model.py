import json
from dataclasses import dataclass


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

    def generate_meta_data(self) -> str:
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
