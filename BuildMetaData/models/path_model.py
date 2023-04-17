from dataclasses import dataclass


@dataclass
class FilePathModel:
    path: str = ""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def save_path(self, new_path: str):
        self.path = new_path

    def get_path(self) -> str:
        return self.path
