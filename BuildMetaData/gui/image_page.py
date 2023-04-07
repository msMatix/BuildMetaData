import tkinter as tk


class ImagePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Image Page")
        label.pack(padx=10, pady=10)

        create_data = tk.Button(
            self,
            text="START",
            command=self.show_image_and_create_meta_data,
        )
        create_data.pack(side="top", fill=tk.X)

    def show_image_and_create_meta_data(self):
        print("HELLO")
        # TODO:
        # Show Pic with new Background
        # Return Back the user inputs of Metadata with the configured fields
