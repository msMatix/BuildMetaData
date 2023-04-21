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
# SIMULATION OF USER INPUTS
@pytest.fixture(scope="function")
def meta_data_correct():
    data = list(
        [
            "DARKFIRE",
            "description",
            "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE",
            "EPIC",
            "GUN",
            1,
            1,
            1,
            1,
            "fireball",
            99999999,
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
            "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE",
            "",
            "GUN",
            1,
            1,
            1,
            1,
            "fireball",
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
            "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE",
            "EPIC",
            "GUN",
            1,
            1,
            1,
            1,
            "fireball",
            99999999,
            "wrong/path/to/image",
        ]
    )
    return data


@pytest.fixture(scope="function")
def meta_data_correct_json():
    data = dict(
        {
            "name": "DARKFIRE",
            "description": "description",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE.webp",
            "rarity": "EPIC",
            "equipment_type": "GUN",
            "power": 1,
            "attack_speed": 1,
            "weight": 1,
            "defense": 1,
            "special_effect": "fireball",
        }
    )
    return data


@pytest.fixture(scope="function")
def meta_data_none():
    data = list(
        [
            "DARKFIRE",
            "",
            "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE",
            "EPIC",
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


@pytest.fixture(scope="function")
def meta_data_none_json():
    data = dict(
        {
            "name": "DARKFIRE",
            "description": "",
            "image_url": "https://dev.api.valtreas.com/metadata/images/equipment/DARKFIRE.webp",
            "rarity": "EPIC",
            "equipment_type": "",
            "power": "",
            "attack_speed": "",
            "weight": "",
            "defense": "",
            "special_effect": "",
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
