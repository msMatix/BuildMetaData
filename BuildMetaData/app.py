import os
import sys
import tkinter as tk

from .app_controller import AppController
from .common import FOLDER_METADATA, PATH_RESULT_PNG, PATH_RESULT_WEBP
from .models.meta_model import ImageMetaModel
from .models.path_model import FilePathModel
from .views.view_image_explorer import ImageExplorerView

available_pages = (ImageExplorerView,)


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.wm_title("Build Meta Data (JSON)")

        # create output folders
        self.create_folders()

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create models
        meta_model = ImageMetaModel()
        path_model = FilePathModel()
        models = (meta_model, path_model)

        # create and init views
        self.views = {}
        for F in available_pages:
            frame = F(container)
            self.views[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # create and set controller
        controller = AppController(models, self.views)
        for F in available_pages:
            self.views[F].set_controller(controller)

        self.show_frame("ImageExplorerView")

    def show_frame(self, page):
        page_to_show = getattr(sys.modules[__name__], page)
        frame = self.views[page_to_show]
        frame.tkraise()

    def create_folders(self):
        # folder images
        if not os.path.exists(PATH_RESULT_PNG):  # pragma no cover
            os.mkdir(PATH_RESULT_PNG)
        if not os.path.exists(PATH_RESULT_WEBP):  # pragma no cover
            os.mkdir(PATH_RESULT_WEBP)

        # folder metadata
        if not os.path.exists(FOLDER_METADATA):  # pragma no cover
            os.mkdir(FOLDER_METADATA)
