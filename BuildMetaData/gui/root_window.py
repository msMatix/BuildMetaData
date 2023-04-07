import sys
import tkinter as tk

from .config_page import ConfigPage
from .main_page import MainPage

available_pages = (MainPage, ConfigPage)


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Build Meta Data (JSON)")

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in available_pages:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page):
        page_to_show = getattr(sys.modules[__name__], page)
        frame = self.frames[page_to_show]
        frame.tkraise()
