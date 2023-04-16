import pytest

from .fixtures import mock_app_controller, mock_meta_model, mock_path_model, mock_views


class TestAppController:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_okay_save_path_to_images(self, mock_app_controller):
        mock_app_controller.save_path_to_images("test/path/")
        saved_path = mock_app_controller.get_path_to_images()

        assert saved_path == "test/path/"
