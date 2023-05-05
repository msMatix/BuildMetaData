import re
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

from PIL import Image, ImageTk

from ..common import equipment_mapping
from .meta_data_types import (
    EAttackSpeed,
    EDefense,
    EEquipmentRange,
    EEquipmentSet,
    EEquipmentType,
    EPower,
    ERarity,
    ESpecialEffect,
    EWeight,
)


class ImageExplorerView(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Image Page")
        label.pack(padx=10, pady=10)

        # image explorer
        self.current_idx = 0
        self.image_folder = ""
        self.image_path = ""
        (
            self.images,
            self.names,
            self.image_labels,
            self.name_labels,
            self.full_names,
        ) = ([], [], [], [], [])
        # meta data
        self.selected_option_equipment_type = tk.StringVar(self)
        self.selected_option_rarity = tk.StringVar(self)
        self.selected_option_power = tk.StringVar(self)
        self.selected_option_defense = tk.StringVar(self)
        self.selected_option_weight = tk.StringVar(self)
        self.selected_option_attack_speed = tk.StringVar(self)
        self.selected_option_special_effect = tk.StringVar(self)
        self.selected_option_equipment_set = tk.StringVar(self)
        self.selected_option_equipment_range = tk.StringVar(self)
        # controller
        self.controller = None

        # message for show_error/success
        self.message_label = tk.Label(self, text="", foreground="red")
        self.message_label.config(width=30)
        self.message_label.place(x=300, y=500, anchor="center")

        self.create_widgets_image_explorer()
        self.create_widgets_for_meta_data()

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.reset_image_explorer()

        if self.controller:
            self.image_folder = self.controller.get_path_to_equipment()

        if self.image_folder:
            self.get_images()
            self.show(self.current_idx)

    def set_controller(self, controller):
        self.controller = controller

    def show_error(self, message):
        self.message_label["text"] = message
        self.message_label["foreground"] = "red"
        self.message_label.after(3000, self.hide_message)
        print(message)

    def show_success(self, message):
        self.message_label["text"] = message
        self.message_label["foreground"] = "green"
        self.message_label.after(3000, self.hide_message)
        print(message)

    def hide_message(self):
        self.message_label["text"] = ""

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
        # EQUIPMENT TYPE
        self.selected_option_equipment_type.set(EEquipmentType.NONE.value)
        equipment_type_options = {
            equipment_type.value: equipment_type.value
            for equipment_type in EEquipmentType
        }
        dropdown_equipment_type = tk.OptionMenu(
            self,
            self.selected_option_equipment_type,
            *equipment_type_options,
            command=self.enable_equipment_stats,
        )
        dropdown_equipment_type.config(width=10)
        dropdown_equipment_type.place(x=100, y=100, anchor="center")

        label_equipment_type = tk.Label(self, text="Select a equipment type:")
        label_equipment_type.place(x=100, y=80, anchor="center")

        # RARITY
        self.selected_option_rarity.set(ERarity.NONE.value)
        rarity_options = {rarity.value: rarity.value for rarity in ERarity}
        dropdown_rarity = tk.OptionMenu(
            self, self.selected_option_rarity, *rarity_options
        )
        dropdown_rarity.config(width=10)
        dropdown_rarity.place(x=400, y=100, anchor="center")

        label_rarity = tk.Label(self, text="Select Rarity:")
        label_rarity.place(x=400, y=80, anchor="center")

        # POWER
        self.selected_option_power.set(EPower.NONE.value)
        power_options = {power.value: power.value for power in EPower}
        self.dropdown_power = tk.OptionMenu(
            self, self.selected_option_power, *power_options
        )
        self.dropdown_power.config(width=10, state="disabled")
        self.dropdown_power.place(x=250, y=100, anchor="center")

        label_power = tk.Label(self, text="Select Power:")
        label_power.place(x=250, y=80, anchor="center")

        # DEFENSE
        self.selected_option_defense.set(EDefense.NONE.value)
        defense_options = {defense.value: defense.value for defense in EDefense}
        self.dropdown_defense = tk.OptionMenu(
            self, self.selected_option_defense, *defense_options
        )
        self.dropdown_defense.config(width=10, state="disabled")
        self.dropdown_defense.place(x=100, y=150, anchor="center")

        label_defense = tk.Label(self, text="Select defense:")
        label_defense.place(x=100, y=130, anchor="center")

        # WEIGHT
        self.selected_option_weight.set(EWeight.NONE.value)
        weight_options = {weight.value: weight.value for weight in EWeight}
        dropdown_weight = tk.OptionMenu(
            self, self.selected_option_weight, *weight_options
        )
        dropdown_weight.config(width=10)
        dropdown_weight.place(x=250, y=150, anchor="center")

        label_weight = tk.Label(self, text="Select weight:")
        label_weight.place(x=250, y=130, anchor="center")

        # ATTACK SPEED
        self.selected_option_attack_speed.set(EAttackSpeed.NONE.value)
        attack_speed_options = {
            attack_speed.value: attack_speed.value for attack_speed in EAttackSpeed
        }
        self.dropdown_attack_speed = tk.OptionMenu(
            self, self.selected_option_attack_speed, *attack_speed_options
        )
        self.dropdown_attack_speed.config(width=10, state="disabled")
        self.dropdown_attack_speed.place(x=400, y=150, anchor="center")

        label_attack_speed = tk.Label(self, text="Select attack speed:")
        label_attack_speed.place(x=400, y=130, anchor="center")

        # SPECIAL ATTACK
        self.selected_option_special_effect.set(ESpecialEffect.NONE.value)
        special_effect_options = {
            special_effect.value: special_effect.value
            for special_effect in ESpecialEffect
        }
        dropdown_special_effect = tk.OptionMenu(
            self, self.selected_option_special_effect, *special_effect_options
        )
        dropdown_special_effect.config(width=10)
        dropdown_special_effect.place(x=550, y=100, anchor="center")

        label_special_effect = tk.Label(self, text="Select special effect:")
        label_special_effect.place(x=550, y=80, anchor="center")

        # SET
        self.selected_option_equipment_set.set(EEquipmentSet.NONE.value)
        equipment_set_options = {
            equipment_set.value: equipment_set.value for equipment_set in EEquipmentSet
        }
        dropdown_equipment_set = tk.OptionMenu(
            self, self.selected_option_equipment_set, *equipment_set_options
        )
        dropdown_equipment_set.config(width=10)
        dropdown_equipment_set.place(x=550, y=150, anchor="center")

        label_equipment_set = tk.Label(self, text="Select equipment set:")
        label_equipment_set.place(x=550, y=130, anchor="center")

        # EQUIPMENT RANGE
        self.selected_option_equipment_range.set(EEquipmentRange.NONE.value)
        equipment_range_options = {
            equipment_range.value: equipment_range.value
            for equipment_range in EEquipmentRange
        }
        self.dropdown_equipment_range = tk.OptionMenu(
            self, self.selected_option_equipment_range, *equipment_range_options
        )
        self.dropdown_equipment_range.config(width=10, state="disabled")
        self.dropdown_equipment_range.place(x=700, y=100, anchor="center")

        label_equipment_range = tk.Label(self, text="Select equipment range:")
        label_equipment_range.place(x=700, y=80, anchor="center")

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
            self.full_names.append(filepath)

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
        self.image_path = self.full_names[i]

    def shift(self, direction):
        self.reset_dropdown_menues()
        self.hide(self.current_idx)
        self.current_idx = (self.current_idx + direction) % len(self.images)
        self.show(self.current_idx)

    ################################################################################
    # META-DATA
    def save_meta_data_in_file(self):
        data = list(
            [
                self.input_field_name.get().strip(),
                self.input_field_description.get(),
                str(self.selected_option_rarity.get()),
                str(self.selected_option_equipment_type.get()),
                str(self.selected_option_power.get()),
                str(self.selected_option_attack_speed.get()),
                str(self.selected_option_weight.get()),
                str(self.selected_option_defense.get()),
                str(self.selected_option_special_effect.get()),
                str(self.selected_option_equipment_set.get()),
                str(self.selected_option_equipment_range.get()),
                self.current_idx,
                self.image_path,
            ]
        )
        if self.controller:
            self.controller.save_data(data)

    def reset_dropdown_menues(self):
        self.selected_option_equipment_type.set(EEquipmentType.NONE.value)
        self.selected_option_rarity.set(ERarity.NONE.value)
        self.selected_option_power.set(EPower.NONE.value)
        self.selected_option_defense.set(EDefense.NONE.value)
        self.selected_option_weight.set(EWeight.NONE.value)
        self.selected_option_attack_speed.set(EAttackSpeed.NONE.value)
        self.selected_option_special_effect.set(ESpecialEffect.NONE.value)
        self.selected_option_equipment_set.set(EEquipmentSet.NONE.value)
        self.selected_option_equipment_range.set(EEquipmentRange.NONE.value)

    def enable_equipment_stats(self, *args):
        self.set_stats_to_default()
        self.deactivate_all_changeable_equipments_stats()
        self.enable_stats_for_view(*args)

    def enable_stats_for_view(self, equipment):
        base_equipment = equipment_mapping[equipment]
        if "armor" in base_equipment:
            self.dropdown_defense.config(state="normal")
        elif "shield" in base_equipment:
            self.dropdown_defense.config(state="normal")
        elif "weapon" in base_equipment:
            self.dropdown_power.config(state="normal")
            self.dropdown_attack_speed.config(state="normal")
            self.dropdown_equipment_range.config(state="normal")

    def deactivate_all_changeable_equipments_stats(self):
        self.dropdown_power.config(state="disabled")
        self.dropdown_defense.config(state="disabled")
        self.dropdown_attack_speed.config(state="disabled")
        self.dropdown_equipment_range.config(state="disabled")

    def set_stats_to_default(self):
        self.selected_option_power.set(EPower.NONE.value)
        self.selected_option_defense.set(EDefense.NONE.value)
        self.selected_option_attack_speed.set(EAttackSpeed.NONE.value)
        self.selected_option_equipment_range.set(EEquipmentRange.NONE.value)

    ################################################################################
    # FILE EXPLORER
    def browse_files(self):
        file_path = filedialog.askdirectory()
        if self.controller:
            self.controller.save_path_to_images(file_path)
        self.tkraise()
