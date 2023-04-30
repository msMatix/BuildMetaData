import os
from dataclasses import dataclass

from ..common import PATH_IMAGES_BG


@dataclass
class FilePathModel:
    path_equipment: str = ""
    path_bg: str = ""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save_path(self, new_path: str):
        self.path_equipment = new_path

        path_components = new_path.split(os.path.sep)
        path_components.pop()
        file_path_bg = os.path.sep.join(path_components)
        file_path_bg = os.path.join(file_path_bg, PATH_IMAGES_BG)
        self.path_bg = file_path_bg

    def get_path_equipment(self) -> str:
        return self.path_equipment

    def get_path_bg(self) -> str:
        return self.path_bg
