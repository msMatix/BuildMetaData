import json
import os
from dataclasses import dataclass

from ..common import FILE_FORMAT, FOLDER_NAME, PATH_META_DATA


@dataclass
class ImageMetaModel:
    name: str = ""
    description: str = ""
    image_url: str = ""
    rarity: str = ""
    equipment_type: str = ""
    power: int = 0
    attack_speed: int = 0
    weight: int = 0
    defense: int = 0
    special_effect: str = ""
    # DATA only for app
    index: int = 0
    image_path: str = ""

    def generate_meta_data(self) -> str:
        meta_data = {
            "name": self.name,
            "description": self.description,
            "image_url": self.image_url,
            "rarity": self.rarity,
            "equipment_type": self.equipment_type,
            "power": self.power,
            "attack_speed": self.attack_speed,
            "weight": self.weight,
            "defense": self.defense,
            "special_effect": self.special_effect,
        }
        return json.dumps(meta_data)

    def save(self):
        data_json_format = self.generate_meta_data()
        file_name = str(self.index)

        if not os.path.exists(FOLDER_NAME):  # pragma no cover
            os.mkdir(FOLDER_NAME)
        with open(
            PATH_META_DATA + file_name + FILE_FORMAT,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(data_json_format, f)
