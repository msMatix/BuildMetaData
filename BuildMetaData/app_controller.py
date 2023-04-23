import os

from PIL import Image

from .common import (
    IMAGE_FORMAT_PNG,
    IMAGE_FORMAT_WEBP,
    PATH_IMAGE_BG_STORE_PNG,
    PATH_IMAGE_BG_STORE_WEBP,
    PATH_IMAGES_BG,
)
from .models.meta_model import ImageMetaModel
from .models.rarity_model import RarityMetaModel
from .views.meta_data_types import ERarity
from .views.view_image_explorer import ImageExplorerView

color_of_rarity = dict(
    {
        ERarity.COMMON.value: "grey",
        ERarity.UNCOMMON.value: "green",
        ERarity.RARE.value: "blue",
        ERarity.EPIC.value: "purple",
        ERarity.LEGENDARY.value: "orange",
        ERarity.UNIQUE.value: "red",
    }
)


class AppController:
    def __init__(self, models, views):
        # init models and views
        self.meta_model, self.path_model = models
        self.views = views

    ################################################################################
    # META DATA MODEL
    def save_data(self, data):
        res_meta_data = self.__save_meta_data(data)

        if not res_meta_data:
            self.views[ImageExplorerView].show_error("Please provide missing data.")
            return

        res_meta_rarity = self.__save_meta_rarity_data(
            self.meta_model.rarity, self.meta_model.name
        )

        res_image_date = self.__save_image_data(
            color_of_rarity[self.meta_model.rarity],
            str(self.meta_model.name),
            self.meta_model.image_path,
        )

        if res_meta_data and res_image_date and res_meta_rarity:  # pragma no cover
            self.views[ImageExplorerView].show_success("SUCCESS")

    ################################################################################
    # SAVE META DATA
    def __save_meta_data(self, data):
        try:
            self.meta_model = ImageMetaModel(*data)
            # check if all necessary information are available
            if not self.meta_model.save():
                return False
            return True
        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"error: {e}")

    def __save_meta_rarity_data(self, rarity, data):
        try:
            self.meta_rarity = RarityMetaModel(rarity, data)
            self.meta_rarity.save()
            return True
        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"error: {e}")

    ################################################################################
    # SAVE IMAGE DATA
    def __save_image_data(self, rarity, name, image_path):
        # create output folders
        if not os.path.exists(PATH_IMAGE_BG_STORE_PNG):  # pragma no cover
            os.mkdir(PATH_IMAGE_BG_STORE_PNG)
        if not os.path.exists(PATH_IMAGE_BG_STORE_WEBP):  # pragma no cover
            os.mkdir(PATH_IMAGE_BG_STORE_WEBP)

        # DECLARE PATHS
        # input
        cwd = os.getcwd()
        image_path_bg = os.path.join(
            cwd, f"{PATH_IMAGES_BG}/{rarity}.{IMAGE_FORMAT_PNG}"
        )
        image_path_item = os.path.join(cwd, f"{image_path}")

        # output
        image_path_output_png = os.path.join(
            cwd, f"{PATH_IMAGE_BG_STORE_PNG}/{name}.{IMAGE_FORMAT_PNG}"
        )
        image_path_output_webp = os.path.join(
            cwd, f"{PATH_IMAGE_BG_STORE_WEBP}/{name}.{IMAGE_FORMAT_WEBP}"
        )

        try:  # pragma no cover
            img_item = Image.open(image_path_item)
            img_bg = Image.open(image_path_bg)
            img_bg.paste(img_item, (0, 0), mask=img_item)
            img_bg.save(image_path_output_png, format="PNG")
            img_bg.save(image_path_output_webp, format="webp")
            return True

        except FileNotFoundError:
            self.views[ImageExplorerView].show_error(
                "Error: The image file cannot be found."
            )
        except IOError:  # pragma no cover
            self.views[ImageExplorerView].show_error(
                "Error: An IOError occured while opening the image file."
            )
        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"Unknown Error occured: {e}.")

    ################################################################################
    # PATH MODEL
    def save_path_to_images(self, path):
        try:
            self.path_model.save_path(path)

        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"Error {e} occured.")

    def get_path_to_images(self):
        return self.path_model.get_path()
