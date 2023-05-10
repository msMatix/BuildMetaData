import json
import os
from dataclasses import dataclass

from ..common import FILE_JSON, IMAGE_WEBP, PATH_META_DATA, URL_LINK, equipment_mapping
from ..exception import NFTAlreadyExist, NoValidBaseStatSelected, NoValidMetaData


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

    def validate_meta_data(self, equipment):
        equipment_stats = self.check_stats(equipment)
        base_stats = self.check_stats("base")

        result_equipment = any(not attr for attr in equipment_stats)
        result_base = any(not attr for attr in base_stats)

        return result_base or result_equipment

    def check_stats(self, equipment):
        if "armor" in equipment:
            return [str(self.defense), self.equipment_set]
        elif "shield" in equipment:
            return [str(self.defense), self.equipment_set]
        elif "weapon" in equipment:
            return [str(self.power), str(self.attack_speed)]
        elif "base" in equipment:
            return [
                self.name,
                self.description,
                self.rarity,
                self.equipment_type,
                str(self.weight),
            ]
        else:
            raise NoValidBaseStatSelected(
                "Select a correct base stat."
            )  # pragma no cover

    def save(self):
        if self.validate_meta_data(equipment_mapping[self.equipment_type]):
            raise NoValidMetaData

        data_json_format = self.generate_meta_data()
        file_name = str(self.name)
        path = PATH_META_DATA + file_name + FILE_JSON

        if os.path.isfile(path):
            raise NFTAlreadyExist("NFT name already awarded.")

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(data_json_format, f, indent=2)

        return True
