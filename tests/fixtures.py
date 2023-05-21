import tkinter as tk
from unittest.mock import Mock

import pytest

from BuildMetaData.app_controller import AppController
from BuildMetaData.models.meta_model import ImageMetaModel
from BuildMetaData.models.path_model import FilePathModel
from BuildMetaData.views.view_image_explorer import ImageExplorerView


################################################################################
# FIXTURES - OBJECTS
@pytest.fixture(scope="function")
def mock_meta_model():
    meta_model = ImageMetaModel()
    return meta_model


@pytest.fixture(scope="function")
def mock_path_model():
    path_model = FilePathModel()
    return path_model


@pytest.fixture(scope="function")
def mock_views():
    views = {}
    views[ImageExplorerView] = ImageExplorerView(tk.Frame())
    return views


@pytest.fixture(scope="function")
def mock_app_controller(mock_meta_model, mock_path_model, mock_views):
    models = (mock_meta_model, mock_path_model)
    views = mock_views
    controller = AppController(models, views)

    return controller


################################################################################
# SIMULATION USER INPUTS
@pytest.fixture(scope="function")
def meta_data_correct():
    data = list(
        [
            "DARKFIRE",
            "description",
            "Epic",
            "Gun",
            1,
            1,
            1,
            1,
            "fireball",
            "",
            1,
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_duplicate():
    data = list(
        [
            "DARKFIRE_DUPLICATE",
            "description",
            "Epic",
            "Gun",
            1,
            1,
            1,
            1,
            "fireball",
            "",
            1,
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_uncommon():
    data = list(
        [
            "DARKFIRE",
            "description",
            "Uncommon",
            "Gun",
            1,
            1,
            1,
            1,
            "fireball",
            "",
            1,
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_duplicate_uncommon():
    data = list(
        [
            "DARKFIRE_DUPLICATE",
            "description",
            "Uncommon",
            "Gun",
            1,
            1,
            1,
            1,
            "fireball",
            "",
            1,
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_armor():
    data = list(
        [
            "DARKFIRE_ARMOR",
            "description",
            "Uncommon",
            "Armor",
            "",
            "",
            "1",
            "1",
            "",
            "metal",
            "",
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_wrong_armor():
    data = list(
        [
            "DARKFIRE_WRONG_ARMOR",
            "description",
            "Uncommon",
            "Armor",
            "",
            "",
            "1",
            "",
            "",
            "metal",
            "",
            99999999,
            "no/path/necessary",
        ]
    )

    return data


@pytest.fixture(scope="function")
def meta_data_correct_shield():
    data = list(
        [
            "DARKFIRE_SHIELD",
            "description",
            "Uncommon",
            "Shield",
            "",
            "",
            "1",
            "1",
            "",
            "metal",
            "",
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_wrong_shield():
    data = list(
        [
            "DARKFIRE_SHIELD",
            "description",
            "Uncommon",
            "Shield",
            "",
            "",
            "1",
            "",
            "",
            "metal",
            "",
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_weapon():
    data = list(
        [
            "DARKFIRE_WEAPON",
            "description",
            "Uncommon",
            "Bow",
            "1",
            "1",
            "1",
            "",
            "",
            "",
            "",
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_wrong_weapon():
    data = list(
        [
            "DARKFIRE_WEAPON",
            "description",
            "Uncommon",
            "Bow",
            "",
            "1",
            "1",
            "",
            "",
            "",
            "",
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_no_special_attack():
    data = list(
        [
            "DARKFIRE_NO_SPECIAL",
            "description",
            "Epic",
            "Gun",
            1,
            1,
            1,
            1,
            "",
            "",
            1,
            99999999,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_no_optional():
    data = list(
        [
            "DARKFIRE2",
            "description",
            "Epic",
            "Gun",
            "1",
            "1",
            "1",
            "",
            "",
            "",
            "1",
            99999998,
            "no/path/necessary",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_rarity_none():
    data = list(
        [
            "DARKFIRE",
            "description",
            "",
            "Gun",
            1,
            1,
            1,
            1,
            "fireball",
            "",
            1,
            99999999,
            "path",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_file_not_found():
    data = list(
        [
            "DARKFIRE",
            "description",
            "Epic",
            "Gun",
            1,
            1,
            1,
            1,
            "fireball",
            "",
            1,
            99999999,
            "wrong/path/to/image",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_none():
    data = list(
        [
            "DARKFIRE_NONE",
            "",
            "Epic",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            99999999,
            "wrong/path/to/image",
        ]
    )
    return data


################################################################################
# RESULT META DATA GENERATION
@pytest.fixture(scope="function")
def meta_data_correct_json():
    data = dict(
        {
            "name": "DARKFIRE",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE",
            "rarity": "Epic",
            "type": "Gun",
            "damage": 1,
            "attackSpeed": 1,
            "weight": 1,
            "defense": 1,
            "effect": "fireball",
            "set": "",
            "range": 1,
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_duplicate_json():
    data = dict(
        {
            "name": "DARKFIRE_DUPLICATE",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE_DUPLICATE",
            "rarity": "Epic",
            "type": "Gun",
            "damage": 1,
            "attackSpeed": 1,
            "weight": 1,
            "defense": 1,
            "effect": "fireball",
            "set": "",
            "range": 1,
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_armor_json():
    data = dict(
        {
            "name": "DARKFIRE_ARMOR",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE_ARMOR",
            "rarity": "Uncommon",
            "type": "Armor",
            "damage": "",
            "attackSpeed": "",
            "weight": "1",
            "defense": "1",
            "effect": "",
            "set": "metal",
            "range": "",
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_shield_json():
    data = dict(
        {
            "name": "DARKFIRE_SHIELD",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE_SHIELD",
            "rarity": "Uncommon",
            "type": "Shield",
            "damage": "",
            "attackSpeed": "",
            "weight": "1",
            "defense": "1",
            "effect": "",
            "set": "metal",
            "range": "",
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_weapon_json():
    data = dict(
        {
            "name": "DARKFIRE_WEAPON",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE_WEAPON",
            "rarity": "Uncommon",
            "type": "Bow",
            "damage": "1",
            "attackSpeed": "1",
            "weight": "1",
            "defense": "",
            "effect": "",
            "set": "",
            "range": "",
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_no_special_attack_json():
    data = dict(
        {
            "name": "DARKFIRE_NO_SPECIAL",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE_NO_SPECIAL",
            "rarity": "Epic",
            "type": "Gun",
            "damage": 1,
            "attackSpeed": 1,
            "weight": 1,
            "defense": 1,
            "effect": "",
            "set": "",
            "range": 1,
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_no_optional_json():
    data = dict(
        {
            "name": "DARKFIRE2",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE2",
            "rarity": "Epic",
            "type": "Gun",
            "damage": "1",
            "attackSpeed": "1",
            "weight": "1",
            "defense": "",
            "effect": "",
            "set": "",
            "range": "1",
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_none_json():
    data = dict(
        {
            "name": "DARKFIRE_NONE",
            "description": "",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE",
            "rarity": "Epic",
            "type": "",
            "damage": "",
            "attackSpeed": "",
            "weight": "",
            "defense": "",
            "effect": "",
            "set": "",
            "range": "",
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_rarity_json():
    data = dict(
        {
            "NONE": [],
            "COMMON": [],
            "UNCOMMON": [],
            "RARE": [],
            "EPIC": [{"DARKFIRE_DUPLICATE": "DARKFIRE_DUPLICATE"}],
            "LEGENDARY": [],
            "UNIQUE": [],
        }
    )
    return data


################################################################################
# MOCKS
@pytest.fixture(scope="function")
def mock_show_error(mocker):
    mocker.patch(
        "BuildMetaData.views.view_image_explorer.ImageExplorerView.show_error",
        return_value="ERROR",
    )


@pytest.fixture(scope="function")
def mock_show_success(mocker):
    mocker.patch(
        "BuildMetaData.views.view_image_explorer.ImageExplorerView.show_success",
        return_value="SUCCESS",
    )
