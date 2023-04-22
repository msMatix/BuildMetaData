import json
import os
from os.path import isfile

import pytest

from BuildMetaData.common import (
    FILE_FORMAT,
    IMAGE_FORMAT_PNG,
    IMAGE_FORMAT_WEBP,
    PATH_IMAGE_BG_STORE_PNG,
    PATH_IMAGE_BG_STORE_WEBP,
    PATH_META_DATA,
)

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
    ################################################################################
    # TESTS
    def test_okay_save_path_to_images(self, mock_app_controller):
        res = mock_app_controller.save_path_to_images("test/path/")
        saved_path = mock_app_controller.get_path_to_images()

        assert saved_path == "test/path/"


class TestAppControllerImageModell:
    ################################################################################
    # TEST SETUP
    @classmethod
    def setup_class(cls):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_FORMAT}"
        if os.path.isfile(path_to_file):
            os.remove(path_to_file)

    @classmethod
    def teardown_class(cls):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_FORMAT}"
        os.remove(path_to_file)

    ################################################################################
    # TESTS
    def test_okay_save_meta_data_and_images(
        self, mock_app_controller, meta_data_correct, meta_data_correct_json
    ):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_FORMAT}"
        # get sure file does not exist
        assert not os.path.isfile(path_to_file)
        # generate file
        mock_app_controller.save_data(meta_data_correct)
        # read file
        with open(path_to_file) as f:
            data = json.load(f)
        assert data == meta_data_correct_json

        # NOT USEFUL -> item/background image paths are not fixed
        # cwd = os.getcwd()
        # path_image_png = os.path.join(
        #     cwd, f"{PATH_IMAGE_BG_STORE_PNG}/DARKFIRE.{IMAGE_FORMAT_PNG}"
        # )
        # path_image_webp = os.path.join(
        #     cwd, f"{PATH_IMAGE_BG_STORE_WEBP}/DARKFIRE.{IMAGE_FORMAT_WEBP}"
        # )
        # assert os.path.isfile(path_image_png)
        # assert os.path.isfile(path_image_webp)

    def test_okay_save_meta_data_none_input(
        self, mock_app_controller, meta_data_none, meta_data_none_json
    ):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_FORMAT}"
        # update file
        mock_app_controller.save_data(meta_data_none)
        # read file
        with open(path_to_file) as f:
            data = json.load(f)
        assert data == meta_data_none_json

    def test_false_no_rarity_selected(self, mock_app_controller, meta_data_rarity_none):
        mock_app_controller.save_data(meta_data_rarity_none)
        path_to_file_png = f"./{PATH_IMAGE_BG_STORE_PNG}/DARKFIRE.{IMAGE_FORMAT_PNG}"
        path_to_file_webp = f"./{PATH_IMAGE_BG_STORE_WEBP}/DARKFIRE.{IMAGE_FORMAT_WEBP}"

        assert not os.path.isfile(path_to_file_png)
        assert not os.path.isfile(path_to_file_webp)

    def test_false_exception_file_not_found(
        self, mock_app_controller, meta_data_file_not_found
    ):
        mock_app_controller.save_data(meta_data_file_not_found)
        path_to_file_png = f"./{PATH_IMAGE_BG_STORE_PNG}/DARKFIRE.{IMAGE_FORMAT_PNG}"
        path_to_file_webp = f"./{PATH_IMAGE_BG_STORE_WEBP}/DARKFIRE.{IMAGE_FORMAT_WEBP}"

        assert not os.path.isfile(path_to_file_png)
        assert not os.path.isfile(path_to_file_webp)
