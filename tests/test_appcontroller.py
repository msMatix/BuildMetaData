import json
import os
import shutil

from BuildMetaData.common import (
    FILE_JSON,
    FILE_RARITY,
    FOLDER_METADATA,
    IMAGE_PNG,
    IMAGE_WEBP,
    PATH_META_DATA,
    PATH_RESULT_PNG,
    PATH_RESULT_WEBP,
)

from .fixtures import (
    meta_data_correct,
    meta_data_correct_json,
    meta_data_correct_no_special_attack,
    meta_data_correct_no_special_attack_json,
    meta_data_correct_uncommon,
    meta_data_file_not_found,
    meta_data_none,
    meta_data_none_json,
    meta_data_rarity_json,
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
        saved_path = mock_app_controller.get_path_to_equipment()

        assert saved_path == "test/path/"


class TestAppControllerImageModell:
    ################################################################################
    # TEST SETUP
    @classmethod
    def setup_class(cls):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_JSON}"
        if os.path.isfile(path_to_file):
            os.remove(path_to_file)

        # create test metadata folder
        if not os.path.exists(FOLDER_METADATA):
            os.mkdir(FOLDER_METADATA)

    @classmethod
    def teardown_class(cls):
        path = "./tests/metadata"
        shutil.rmtree(path)

    # @classmethod
    # def teardown_method(cls):
    #     path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_JSON}"
    #     os.remove(path_to_file)

    ################################################################################
    # TESTS
    def test_okay_save_meta_data_none_input(self, mock_app_controller, meta_data_none):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_JSON}"
        mock_app_controller.save_data(meta_data_none)
        assert not os.path.isfile(path_to_file)

    def test_okay_save_meta_data_and_images(
        self, mock_app_controller, meta_data_correct, meta_data_correct_json
    ):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_JSON}"
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
        #     cwd, f"{PATH_RESULT_PNG}/DARKFIRE{IMAGE_PNG}"
        # )
        # path_image_webp = os.path.join(
        #     cwd, f"{PATH_RESULT_WEBP}/DARKFIRE{IMAGE_WEBP}"
        # )
        # assert os.path.isfile(path_image_png)
        # assert os.path.isfile(path_image_webp)

    def test_okay_save_meta_data_and_images_no_special_attack_defined(
        self,
        mock_app_controller,
        meta_data_correct_no_special_attack,
        meta_data_correct_no_special_attack_json,
    ):
        path_to_file = f"./{PATH_META_DATA}DARKFIRE{FILE_JSON}"

        # generate file
        mock_app_controller.save_data(meta_data_correct_no_special_attack)

        # read file
        with open(path_to_file) as f:
            data = json.load(f)
        assert data == meta_data_correct_no_special_attack_json

    def test_okay_save_meta_data_and_images_and_no_duplicate_rarity(
        self,
        mock_app_controller,
        meta_data_correct,
        meta_data_rarity_json,
        meta_data_correct_uncommon,
    ):
        path_to_file = f"./{FILE_RARITY}"

        # generate file
        mock_app_controller.save_data(meta_data_correct)

        # check if nft exist two times in the same rarity
        mock_app_controller.save_data(meta_data_correct)
        with open(path_to_file) as f:
            data = json.load(f)
        assert data == meta_data_rarity_json

        # Check whether in the case of a new creation of an already existing nft only in the case of other rarity none is created
        mock_app_controller.save_data(meta_data_correct_uncommon)
        with open(path_to_file) as f:
            data = json.load(f)
        assert data == meta_data_rarity_json

    def test_false_no_rarity_selected(self, mock_app_controller, meta_data_rarity_none):
        mock_app_controller.save_data(meta_data_rarity_none)
        path_to_file_png = f"./{PATH_RESULT_PNG}/DARKFIRE{IMAGE_PNG}"
        path_to_file_webp = f"./{PATH_RESULT_WEBP}/DARKFIRE{IMAGE_WEBP}"

        assert not os.path.isfile(path_to_file_png)
        assert not os.path.isfile(path_to_file_webp)

    def test_false_exception_file_not_found(
        self, mock_app_controller, meta_data_file_not_found
    ):
        mock_app_controller.save_data(meta_data_file_not_found)
        path_to_file_png = f"./{PATH_RESULT_PNG}/DARKFIRE{IMAGE_PNG}"
        path_to_file_webp = f"./{PATH_RESULT_WEBP}/DARKFIRE{IMAGE_WEBP}"

        assert not os.path.isfile(path_to_file_png)
        assert not os.path.isfile(path_to_file_webp)
