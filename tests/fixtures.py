import tkinter as tk
from unittest.mock import Mock

import pytest

from BuildMetaData.app_controller import AppController
from BuildMetaData.models.meta_model import ImageMetaModel
from BuildMetaData.models.path_model import FilePathModel
from BuildMetaData.views.view_image_explorer import ImageExplorerView


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
