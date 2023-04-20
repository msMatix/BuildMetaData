import os

from PIL import Image

from .common import IMAGE_FORMAT, PATH_IMAGE_BG_STORE, PATH_IMAGES_BG
from .models.meta_model import ImageMetaModel
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

    # META DATA MODEL
    def save_data(self, data):
        self.__save_meta_data(data)

        if self.meta_model.rarity == "":
            self.views[ImageExplorerView].show_error("Please select a rarity.")
            return

        self.__save_image_data(
            color_of_rarity[self.meta_model.rarity],
            str(self.meta_model.index),
            self.meta_model.image_path,
        )

        self.views[ImageExplorerView].show_success("SUCCESS")

    def __save_meta_data(self, data):
        try:
            self.meta_model = ImageMetaModel(*data)
            self.meta_model.save()
        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"error: {e}")

    def __save_image_data(self, rarity, idx, image_path):
        if not os.path.exists(PATH_IMAGE_BG_STORE):  # pragma no cover
            os.mkdir(PATH_IMAGE_BG_STORE)

        cwd = os.getcwd()
        image_path_bg = os.path.join(cwd, f"{PATH_IMAGES_BG}/{rarity}.{IMAGE_FORMAT}")
        image_path_item = os.path.join(cwd, f"{image_path}.{IMAGE_FORMAT}")
        image_path_output = os.path.join(
            cwd, f"{PATH_IMAGE_BG_STORE}/{idx}.{IMAGE_FORMAT}"
        )

        try:  # pragma no cover
            img_item = Image.open(image_path_item)
            img_bg = Image.open(image_path_bg)
            img_bg.paste(img_item, (0, 0), mask=img_item)
            img_bg.save(image_path_output, format="PNG")

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

    # PATH MODEL
    def save_path_to_images(self, path):
        try:
            self.path_model.save_path(path)

        except Exception as e:  # pragma no cover
            self.views[ImageExplorerView].show_error(f"Error {e} occured.")

    def get_path_to_images(self):
        return self.path_model.get_path()
