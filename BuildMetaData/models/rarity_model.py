import json
import os
import re
from dataclasses import dataclass

from ..common import FILE_RARITY
from ..exception import NFTAlreadyExist
from ..views.meta_data_types import ERarity


@dataclass
class RarityMetaModel:
    rarity: str = ""
    item: str = ""

    @staticmethod
    def generate_init_data():
        # rarity_dict = {}
        init_data = ""
        for enum_value in ERarity:
            # generate json sections which store a dict
            # rarity_dict[enum_value.value] = list([])
            # init_data += f"{enum_value.value}{{\n}}\n"
            init_data += f"export enum {enum_value.value}{{\n}}\n"

        with open(FILE_RARITY, "w") as f:
            # json.dump(rarity_dict, f)
            f.write(init_data)

    @staticmethod
    # def nft_name_available(entry, file):
    def nft_name_available(entry, input):
        res = all(entry not in input[enum_value.value] for enum_value in ERarity)
        return res

    @staticmethod
    def append_data(FILE_RARITY, rarity, new_data):
        data_input = {}
        current_section = None
        # read file and store in a dict
        with open(FILE_RARITY, "r") as f:
            # data = json.load(f)
            for line in f:
                line = line.strip()

                if line.endswith("{"):
                    words = line.split()
                    modified_line = " ".join(words[2:])
                    current_section = modified_line[:-1]
                    data_input[current_section] = list([])  # war {}
                elif line.endswith("}"):
                    current_section = None
                elif line:
                    key, value = line.split("=")
                    key = key.strip()
                    value = value.strip().strip('"')
                    if current_section:
                        data_input[current_section].append({key: value})

        if RarityMetaModel.nft_name_available(new_data, data_input):
            data_input[ERarity(rarity).value].append(dict({new_data: new_data}))
            # f.seek(0)
            # json.dump(data, f, indent=2)
            with open(FILE_RARITY, "w") as f:
                for section, items in data_input.items():
                    f.write(f"export enum {section}{{\n")
                    for item in items:
                        for key, value in item.items():
                            f.write(f'    {key} = "{value}"\n')
                    f.write("}\n")
            return True
        else:  # pragma no cover
            raise NFTAlreadyExist("NFT name already awarded.")

    def save(self):
        if not os.path.isfile(FILE_RARITY):
            RarityMetaModel.generate_init_data()
        return RarityMetaModel.append_data(FILE_RARITY, self.rarity, self.item)
