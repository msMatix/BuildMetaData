import re
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

from PIL import Image, ImageTk

from .meta_data_types import (
    EArmorType,
    EAttackSpeed,
    EDamage,
    EMovementSpeed,
    ERange,
    ERarity,
    EWeaponType,
)


class ImageExplorerView(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Image Page")
        label.pack(padx=10, pady=10)

        # image explorer
        self.current_idx = 0
        self.image_folder = ""
        self.images, self.names, self.image_labels, self.name_labels = [], [], [], []
        # meta data
        self.selected_option_weapon_type = tk.StringVar(self)
        self.selected_option_armor_type = tk.StringVar(self)
        self.selected_option_rarity = tk.StringVar(self)
        self.selected_option_damage = tk.StringVar(self)
        self.selected_option_range = tk.StringVar(self)
        self.selected_option_movement_speed = tk.StringVar(self)
        self.selected_option_attack_speed = tk.StringVar(self)
        # controller
        self.controller = None

        self.create_widgets_image_explorer()
        self.create_widgets_for_meta_data()

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.reset_image_explorer()

        if self.controller:
            self.image_folder = self.controller.get_path_to_images()

        if self.image_folder:
            self.get_images()
            self.show(self.current_idx)

    def set_controller(self, controller):
        self.controller = controller

    def show_error(self, message):
        print(message)

    def show_success(self, message):
        print(message)

    def create_widgets_image_explorer(self):
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

        button_change_path = tk.Button(
            self,
            text="PATH",
            command=lambda: self.browse_files(),
            width=30,
            height=5,
        )
        button_change_path.pack(side="left")

    def create_widgets_for_meta_data(self):
        # WEAPON TYPE
        self.selected_option_weapon_type.set(EWeaponType.NONE.value)
        weapon_type_options = {
            weapon_type.value: weapon_type.value for weapon_type in EWeaponType
        }
        dropdown_weapon_type = tk.OptionMenu(
            self, self.selected_option_weapon_type, *weapon_type_options
        )
        dropdown_weapon_type.config(width=10)
        dropdown_weapon_type.place(x=100, y=100, anchor="center")

        label_weapon_type = tk.Label(self, text="Select a weapon type:")
        label_weapon_type.place(x=100, y=80, anchor="center")

        # ARMOR TYPE
        self.selected_option_armor_type.set(EArmorType.NONE.value)
        armor_type_options = {
            armor_type.value: armor_type.value for armor_type in EArmorType
        }
        dropdown_armor_type = tk.OptionMenu(
            self, self.selected_option_armor_type, *armor_type_options
        )
        dropdown_armor_type.config(width=10)
        dropdown_armor_type.place(x=250, y=100, anchor="center")

        label_armor_type = tk.Label(self, text="Select a armor type:")
        label_armor_type.place(x=250, y=80, anchor="center")

        # RARITY
        self.selected_option_rarity.set(EArmorType.NONE.value)
        rarity_options = {rarity.value: rarity.value for rarity in ERarity}
        dropdown_rarity = tk.OptionMenu(
            self, self.selected_option_rarity, *rarity_options
        )
        dropdown_rarity.config(width=10)
        dropdown_rarity.place(x=400, y=100, anchor="center")

        label_rarity = tk.Label(self, text="Select Rarity:")
        label_rarity.place(x=400, y=80, anchor="center")

        # DAMAGE
        self.selected_option_damage.set(str(EDamage.NONE.value))
        damage_options = {damage.value: damage.value for damage in EDamage}
        dropdown_damage = tk.OptionMenu(
            self, self.selected_option_damage, *damage_options
        )
        dropdown_damage.config(width=10)
        dropdown_damage.place(x=550, y=100, anchor="center")

        label_damage = tk.Label(self, text="Select Damage:")
        label_damage.place(x=550, y=80, anchor="center")

        # RANGE
        self.selected_option_range.set(str(ERange.NONE.value))
        range_options = {range.value: range.value for range in ERange}
        dropdown_range = tk.OptionMenu(self, self.selected_option_range, *range_options)
        dropdown_range.config(width=10)
        dropdown_range.place(x=100, y=150, anchor="center")

        label_range = tk.Label(self, text="Select Range:")
        label_range.place(x=100, y=130, anchor="center")

        # MOVEMENT SPEED
        self.selected_option_movement_speed.set(str(EMovementSpeed.NONE.value))
        movement_speed_options = {
            movement_speed.value: movement_speed.value
            for movement_speed in EMovementSpeed
        }
        dropdown_movement_speed = tk.OptionMenu(
            self, self.selected_option_movement_speed, *movement_speed_options
        )
        dropdown_movement_speed.config(width=10)
        dropdown_movement_speed.place(x=250, y=150, anchor="center")

        label_movement_speed = tk.Label(self, text="Select movement speed:")
        label_movement_speed.place(x=250, y=130, anchor="center")

        # ATTACK SPEED
        self.selected_option_attack_speed.set(str(EAttackSpeed.NONE.value))
        attack_speed_options = {
            attack_speed.value: attack_speed.value for attack_speed in EAttackSpeed
        }
        dropdown_attack_speed = tk.OptionMenu(
            self, self.selected_option_attack_speed, *attack_speed_options
        )
        dropdown_attack_speed.config(width=10)
        dropdown_attack_speed.place(x=400, y=150, anchor="center")

        label_attack_speed = tk.Label(self, text="Select attack speed:")
        label_attack_speed.place(x=400, y=130, anchor="center")

        # NAME
        self.input_field_name = tk.Entry(self)
        self.input_field_name.config(width=100)
        self.input_field_name.place(x=400, y=250, anchor="center")
        label_name = tk.Label(self, text="Name:")
        label_name.place(x=70, y=230, anchor="center")
        # DESCRIPTION
        self.input_field_description = tk.Entry(self)
        self.input_field_description.config(width=100)
        self.input_field_description.place(x=400, y=300, anchor="center")
        label_description = tk.Label(self, text="Description:")
        label_description.place(x=80, y=280, anchor="center")
        # URL
        self.input_field_url = tk.Entry(self)
        self.input_field_url.config(width=100)
        self.input_field_url.place(x=400, y=350, anchor="center")
        label_url = tk.Label(self, text="Url:")
        label_url.place(x=60, y=330, anchor="center")

        # STORE
        button_store = tk.Button(
            self,
            text="STORE",
            command=lambda: self.save_meta_data_in_file(),
            width=30,
            height=5,
        )
        button_store.config(width=10)
        button_store.place(x=100, y=500, anchor="center")

    ################################################################################
    # IMAGE EXPLORER
    def get_images(self):
        for filepath in Path(self.image_folder).iterdir():
            image_path = Image.open(filepath)
            image = ImageTk.PhotoImage(image_path)
            image_name = re.search(r"[^\\/]+$", str(filepath)).group(0)

            self.images.append(image)
            self.names.append(image_name)

        self.image_labels, self.name_labels = [], []
        for i, (img, name) in enumerate(zip(self.images, self.names)):
            image_label = tk.Label(self, image=img)
            image_label.pack(side="left")
            self.image_labels.append(image_label)

            name_label = tk.Label(self, text=name)
            name_label.pack(side="left")
            self.name_labels.append(name_label)
            self.hide(i)

    def reset_image_explorer(self):
        # check if the page is called the second time or so
        if self.current_idx:
            self.hide(self.current_idx)

        self.current_idx = 0
        self.images.clear()
        self.names.clear()

    def hide(self, i):
        self.image_labels[i].pack_forget()
        self.name_labels[i].pack_forget()

    def show(self, i):
        self.image_labels[i].pack()
        self.name_labels[i].pack()

    def shift(self, direction):
        self.reset_dropdown_menues()
        self.hide(self.current_idx)
        self.current_idx = (self.current_idx + direction) % len(self.images)
        self.show(self.current_idx)

    ################################################################################
    # GENERATE META-DATA
    def save_meta_data_in_file(self):
        data = list(
            [
                self.input_field_name.get(),
                self.input_field_description.get(),
                self.input_field_url.get(),
                str(self.selected_option_rarity.get()),
                str(self.selected_option_weapon_type.get()),
                str(self.selected_option_armor_type.get()),
                int(self.selected_option_damage.get()),
                int(self.selected_option_range.get()),
                int(self.selected_option_movement_speed.get()),
                int(self.selected_option_attack_speed.get()),
                self.current_idx,
            ]
        )
        if self.controller:
            self.controller.save_meta_data_on_disk(data)

    def reset_dropdown_menues(self):
        self.selected_option_weapon_type.set(EWeaponType.NONE.value)
        self.selected_option_armor_type.set(EArmorType.NONE.value)
        self.selected_option_rarity.set(EArmorType.NONE.value)
        self.selected_option_damage.set(str(EDamage.NONE.value))
        self.selected_option_range.set(str(ERange.NONE.value))
        self.selected_option_movement_speed.set(str(EMovementSpeed.NONE.value))
        self.selected_option_attack_speed.set(str(EAttackSpeed.NONE.value))

    ################################################################################
    # FILE EXPLORER
    def browse_files(self):
        file_path = filedialog.askdirectory()
        if self.controller:
            self.controller.save_path_to_images(file_path)
        self.tkraise()
