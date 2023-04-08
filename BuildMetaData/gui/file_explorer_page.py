import tkinter as tk
from tkinter import filedialog

from ..common import path_model


class FileExplorerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # open file explorer to get the correct path
        button_file_explorer = tk.Button(
            self, text="Browse Files", command=self.browse_files
        )
        button_file_explorer.pack(side="top")

        self.selected_file_label = tk.Label(self, text="")
        self.selected_file_label.pack()
        self.controller = controller

    def browse_files(self):
        file_path = filedialog.askdirectory()
        path_model.set_path(file_path)

        self.selected_file_label.config(text=file_path)
        self.controller.show_frame("ImageExplorerPage")
