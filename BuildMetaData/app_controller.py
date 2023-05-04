import os

from PIL import Image

from .common import (
    IMAGE_PNG,
    IMAGE_WEBP,
    PATH_RESULT_PNG,
    PATH_RESULT_WEBP,
    equipment_mapping,
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
        res_meta_rarity = self.__save_meta_rarity_data()
        res_image_date = self.__save_image_data()

        if res_meta_data and res_image_date and res_meta_rarity:  # pragma no cover
            self.views[ImageExplorerView].show_success("SUCCESS")

    def get_base_equipment(self, selected_equipment):
        return self.meta_model.enable_stats(equipment_mapping[selected_equipment])

    ################################################################################
    # SAVE META DATA
    def __save_meta_data(self, data):
        try:
            self.meta_model = ImageMetaModel(*data)
            return self.meta_model.save()

        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"error: {e}")

    def __save_meta_rarity_data(self):
        try:
            self.meta_rarity = RarityMetaModel(
                self.meta_model.rarity, self.meta_model.name
            )
            return self.meta_rarity.save()
        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"error: {e}")

    ################################################################################
    # SAVE IMAGE DATA
    def __save_image_data(self):
        [
            image_path_bg,
            image_path_output_png,
            image_path_output_webp,
        ] = self.__build_image_paths()

        try:  # pragma no cover
            img_item = Image.open(self.meta_model.image_path)
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

    def __build_image_paths(self):
        cwd = os.getcwd()
        name = str(self.meta_model.name)

        # input
        path_bg = os.path.join(
            cwd,
            f"{self.path_model.get_path_bg()}/{color_of_rarity[self.meta_model.rarity]}{IMAGE_PNG}",
        )
        # output
        path_png = os.path.join(cwd, f"{PATH_RESULT_PNG}/{name}{IMAGE_PNG}")
        path_webp = os.path.join(cwd, f"{PATH_RESULT_WEBP}/{name}{IMAGE_WEBP}")

        return [path_bg, path_png, path_webp]

    ################################################################################
    # PATH MODEL
    def save_path_to_images(self, path):
        try:
            self.path_model.save_path(path)

        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"Error {e} occured.")

    def get_path_to_equipment(self):
        return self.path_model.get_path_equipment()
