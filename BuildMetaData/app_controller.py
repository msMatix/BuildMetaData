import os

from PIL import Image

from .common import IMAGE_FORMAT, PATH_IMAGE_BG_STORE, PATH_IMAGES_BG
from .models.meta_model import ImageMetaModel
from .views.meta_data_types import ERarity
from .views.view_image_explorer import ImageExplorerView

color_of_rarity = dict(
    {
        ERarity.COMMON.value: "blue",
        ERarity.UNCOMMON.value: "green",
        ERarity.RARE.value: "yellow",
        ERarity.EPIC.value: "orange",
        ERarity.LEGENDARY.value: "red",
    }
)


class AppController:
    def __init__(self, models, views):
        # init models and views
        self.meta_model, self.path_model = models
        self.views = views

    # META DATA MODEL
    def save_meta_data_on_disk(self, data):
        try:
            self.meta_model = ImageMetaModel(*data)
            self.meta_model.save()

            if self.meta_model.rarity == "NONE":
                self.views[ImageExplorerView].show_error("Please select a rarity.")
                return
            self.save_image_with_background(
                color_of_rarity[self.meta_model.rarity], str(self.meta_model.index)
            )

            self.views[ImageExplorerView].show_success("SUCCESS")

        except Exception as e:
            self.views[ImageExplorerView].show_error(f"Error: {e}")

    def save_image_with_background(self, rarity, idx):
        if not os.path.exists(PATH_IMAGE_BG_STORE):
            os.mkdir(PATH_IMAGE_BG_STORE)

        cwd = os.getcwd()
        image_path_bg = os.path.join(cwd, f"{PATH_IMAGES_BG}/{rarity}.{IMAGE_FORMAT}")
        # TODO: Store path sould be a parameter of item -> BuildMetaData muss weg
        image_path_item = os.path.join(cwd, f"BuildMetaData/{idx}.{IMAGE_FORMAT}")
        image_path_output = os.path.join(
            cwd, f"{PATH_IMAGE_BG_STORE}/{idx}.{IMAGE_FORMAT}"
        )

        try:
            img_item = Image.open(image_path_item)
            img_bg = Image.open(image_path_bg)
            img_bg.paste(img_item, (0, 0), mask=img_item)
            img_bg.save(image_path_output, format="PNG")

            # TODO: show log message in app
            self.views[ImageExplorerView].show_success("SUCCESS")
        except FileNotFoundError:
            # TODO: show log message in app
            self.views[ImageExplorerView].show_error(
                "Error: The image file cannot be found."
            )
        except IOError:
            # TODO: show log message in app
            self.views[ImageExplorerView].show_error(
                "An IOError occured while opening the image file."
            )
        except Exception as e:
            self.views[ImageExplorerView].show_error(f"Unknown Error occured: {e}.")

    # PATH MODEL
    def save_path_to_images(self, path):
        try:
            self.path_model.save_path(path)
            # TODO: show log message in app
            self.views[ImageExplorerView].show_success("SUCCESS")

        except Exception as e:
            # TODO: show log message in app
            self.views[ImageExplorerView].show_error(f"Error {e} occured.")

    def get_path_to_images(self):
        return self.path_model.get_path()