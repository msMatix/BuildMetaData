from .models.meta_model import ImageMetaModel
from .views.view_image_explorer import ImageExplorerView


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
            self.views[ImageExplorerView].show_success("SUCCESS")

        except ValueError as error:
            self.views[ImageExplorerView].show_error(error)

    # PATH MODEL
    def save_path_to_images(self, path):
        try:
            self.path_model.save_path(path)
            self.views[ImageExplorerView].show_success("SUCCESS")

        except ValueError as error:
            self.views[ImageExplorerView].show_error(error)

    def get_path_to_images(self):
        return self.path_model.get_path()
