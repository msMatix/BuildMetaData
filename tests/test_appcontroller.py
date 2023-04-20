import json
import os
from os.path import isfile

import pytest

from .fixtures import (
    meta_data_correct,
    meta_data_correct_json,
    meta_data_file_not_found,
    meta_data_none,
    meta_data_none_json,
    meta_data_rarity_none,
    mock_app_controller,
    mock_meta_model,
    mock_path_model,
    mock_show_error,
    mock_show_success,
    mock_views,
)


class TestAppControllerPathModell:
    def test_okay_save_path_to_images(self, mock_app_controller):
        res = mock_app_controller.save_path_to_images("test/path/")
        saved_path = mock_app_controller.get_path_to_images()

        assert saved_path == "test/path/"


class TestAppControllerImageModell:
    @classmethod
    def setup_class(cls):
        path_to_file = "./metadata/99999999.json"
        if os.path.isfile(path_to_file):
            os.remove(path_to_file)

    @classmethod
    def teardown_class(cls):
        path_to_file = "./metadata/99999999.json"
        os.remove(path_to_file)

    def test_okay_save_meta_data(
        self, mock_app_controller, meta_data_correct, meta_data_correct_json
    ):
        path_to_file = "./metadata/99999999.json"
        # get sure file does not exist
        assert not os.path.isfile(path_to_file)
        # generate file
        mock_app_controller.save_data(meta_data_correct)
        # read file
        with open(path_to_file) as f:
            data = json.load(f)
        assert data == json.dumps(meta_data_correct_json)

    def test_okay_save_meta_data_none_input(
        self, mock_app_controller, meta_data_none, meta_data_none_json
    ):
        path_to_file = "./metadata/99999999.json"
        # update file
        mock_app_controller.save_data(meta_data_none)
        # read file
        with open(path_to_file) as f:
            data = json.load(f)
        assert data == json.dumps(meta_data_none_json)

    def test_false_no_rarity_selected(self, mock_app_controller, meta_data_rarity_none):
        mock_app_controller.save_data(meta_data_rarity_none)
        path_to_file = "./image_bg/99999999.png"
        assert not os.path.isfile(path_to_file)

    def test_false_exception_file_not_found(
        self, mock_app_controller, meta_data_file_not_found
    ):
        mock_app_controller.save_data(meta_data_file_not_found)
        path_to_file = "./image_bg/99999999.png"
        assert not os.path.isfile(path_to_file)
