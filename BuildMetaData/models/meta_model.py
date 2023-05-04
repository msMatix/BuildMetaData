import json
from dataclasses import dataclass

from ..common import FILE_JSON, IMAGE_WEBP, PATH_META_DATA, URL_LINK
from ..exception import NoValidBaseStatSelected
from ..views.meta_data_types import EBaseEquipment, EEquipmentType

# from varname import nameof


equipment_mapping = dict(
    {
        EEquipmentType.HELMET.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.ARMOR.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.BRACERS.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.BOOTS.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.SHIELD_1H.value: EBaseEquipment.SHIELD.value,
        EEquipmentType.BOW_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.SWORD_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.SWORD_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.AXE_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.AXE_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.HAMMER_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.HAMMER_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.LANCE_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.GUN_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.WAND_1H.value: EBaseEquipment.WEAPON.value,
    }
)


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
        equipment_stats = self.get_necessary_stats(equipment)
        base_stats = self.get_necessary_stats("base")

        result_equipment = any(not attr for attr in equipment_stats)
        result_base = any(not attr for attr in base_stats)

        return result_base or result_equipment

    def get_necessary_stats(self, equipment):
        if "armor" in equipment:
            return [str(self.defense)]
        elif "shield" in equipment:
            return [str(self.defense)]
        elif "weapon" in equipment:
            return [str(self.power), str(self.attack_speed)]
        elif "base" in equipment:
            return [
                self.name,
                self.description,
                self.rarity,
                self.equipment_type,
                str(self.weight),
                self.equipment_set,
            ]
        else:
            raise NoValidBaseStatSelected(
                "Select a correct base stat."
            )  # pragma no cover

    def save(self):
        if self.validate_meta_data(equipment_mapping[self.equipment_type]):
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
