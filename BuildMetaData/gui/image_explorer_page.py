import re
import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk

from ..common import path_model


class ImageExplorerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Image Page")
        label.pack(padx=10, pady=10)

        button_prev = tk.Button(
            self,
            text="<< PREV",
            command=lambda: self.shift(-1),
            width=30,
            height=5,
        )
        button_prev.pack(side="left")

        button_next = tk.Button(
            self,
            text="NEXT >>",
            command=lambda: self.shift(+1),
            width=30,
            height=5,
        )
        button_next.pack(side="left")

        self.image_folder = ""
        self.images = []
        self.names = []
        self.current_idx = 0

    # TODO: make general after image explorer works
    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.image_folder = path_model.get_path()
        self.get_images()
        self.show(self.current_idx)

    def get_images(self):
        global image_labels, name_labels

        for filepath in Path(self.image_folder).iterdir():
            image_path = Image.open(filepath)
            image = ImageTk.PhotoImage(image_path)
            image_name = re.search(r"[^\\/]+$", str(filepath)).group(0)

            self.images.append(image)
            self.names.append(image_name)

        image_labels, name_labels = [], []
        for i, (img, name) in enumerate(zip(self.images, self.names)):
            image_label = tk.Label(self, image=img)
            image_label.pack(side="left")
            image_labels.append(image_label)

            name_label = tk.Label(self, text=name)
            name_label.pack(side="left")
            name_labels.append(name_label)

            self.hide(i)

    def hide(self, i):
        image_labels[i].pack_forget()
        name_labels[i].pack_forget()

    def show(self, i):
        image_labels[i].pack()
        name_labels[i].pack()

    def shift(self, direction):
        self.hide(self.current_idx)
        self.current_idx = (self.current_idx + direction) % len(self.images)
        self.show(self.current_idx)
