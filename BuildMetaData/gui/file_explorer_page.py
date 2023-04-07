import tkinter as tk
from tkinter import filedialog


class FileExplorerPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="File Explorer Page")
        label.pack(padx=10, pady=10)

        file_explorer_button = tk.Button(
            self, text="Browse Files", command=self.browse_files
        )
        file_explorer_button.pack(side="top", fill=tk.X)

        self.selected_file_label = tk.Label(self, text="")
        self.selected_file_label.pack()

        self._selected_file_path = ""

    @property
    def selected_file_path(self):
        return self._selected_file_path

    def browse_files(self):
        self._selected_file_path = filedialog.askopenfilename()
        self.selected_file_label.config(text=self.selected_file_path)
        self.destroy()
