import json
import os
from dataclasses import dataclass

from ..common import FILE_RARITY
from ..views.meta_data_types import ERarity


@dataclass
class RarityMetaModel:
    rarity: str = ""
    item: str = ""

    @staticmethod
    def generate_init_data():
        rarity_dict = {}
        for enum_value in ERarity:
            # generate json sections which store a list
            rarity_dict[enum_value.name] = []

        with open(FILE_RARITY, "w") as f:
            json.dump(rarity_dict, f)

    @staticmethod
    def append_data(FILE_RARITY, rarity, new_data):
        with open(FILE_RARITY, "r+") as f:
            data = json.load(f)
            data[ERarity(rarity).name].append(new_data)
            f.seek(0)
            json.dump(data, f, indent=2)

    def save(self):
        if not os.path.isfile(FILE_RARITY):
            RarityMetaModel.generate_init_data()
        RarityMetaModel.append_data(FILE_RARITY, self.rarity, self.item)