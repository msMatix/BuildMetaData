import tkinter as tk


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # goto config page
        button_config_page = tk.Button(
            self,
            text="Go to the Config Page",
            command=lambda: controller.show_frame("ConfigPage"),
            width=30,
            height=5,
        )
        button_config_page.pack(side="left")

        # goto file explorer page
        button_file_explorer = tk.Button(
            self,
            text="FileExplorer",
            command=lambda: controller.show_frame("FileExplorerPage"),
            width=30,
            height=5,
        )
        button_file_explorer.pack(side="left")

        # goto image page
        button_image = tk.Button(
            self,
            text="CreateMetaData",
            command=lambda: controller.show_frame("ImagePage"),
            width=30,
            height=5,
        )
        button_image.pack(side="left")
