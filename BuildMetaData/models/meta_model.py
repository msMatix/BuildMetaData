import json
from dataclasses import dataclass

from ..common import FILE_JSON, IMAGE_WEBP, PATH_META_DATA, URL_LINK


@dataclass
class ImageMetaModel:
    name: str = ""
    description: str = ""
    rarity: str = ""
    equipment_type: str = ""
    power: int = 0
    attack_speed: int = 0
    weight: int = 0
    defense: int = 0
    special_effect: str = ""
    equipment_set: str = ""
    equipment_range: int = 0
    # only for app
    index: int = 0
    image_path: str = ""

    def generate_meta_data(self) -> dict:
        meta_data = {
            "name": self.name,
            "description": self.description,
            "image_url": f"{URL_LINK}{self.name}{IMAGE_WEBP}",
            "rarity": self.rarity,
            "equipment_type": self.equipment_type,
            "power": self.power,
            "attack_speed": self.attack_speed,
            "weight": self.weight,
            "defense": self.defense,
            "special_effect": self.special_effect,
            "equipment_set": self.equipment_set,
            "equipment_range": self.equipment_range,
        }
        return meta_data

    def check_modell_correctness(self) -> bool:
        return any(
            not attr
            for attr in [
                self.name,
                self.description,
                self.rarity,
                self.equipment_type,
                self.weight,
                self.equipment_set,
            ]
        )

    def save(self):
        if self.check_modell_correctness():
            return False

        data_json_format = self.generate_meta_data()
        file_name = str(self.name)

        with open(
            PATH_META_DATA + file_name + FILE_JSON,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(data_json_format, f, indent=2)

        return True
