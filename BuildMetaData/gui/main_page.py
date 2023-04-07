import tkinter as tk


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Config Page",
            command=lambda: controller.show_frame("ConfigPage"),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

        button_file_explorer = tk.Button(
            self,
            text="FileExplorer",
            command=lambda: controller.show_frame("FileExplorerPage"),
        )
        button_file_explorer.pack(side="bottom", fill=tk.X)
