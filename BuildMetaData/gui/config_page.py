import tkinter as tk


class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Config Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go back to main page",
            command=lambda: controller.show_frame("MainPage"),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)
