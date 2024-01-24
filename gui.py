import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import os
from ini_parser import (
    read_and_parse,
    extract_pairs,
    reconstruct_section,
    rewrite_file,
    load_settings,
    save_modified_pairs,
)
from difficultypresets import casual_settings, normal_settings, hard_settings
from descriptions import descriptions

descriptions_dict = dict(descriptions)


def locate_game_server():
    global default_file_path, modified_file_path
    game_server_directory = filedialog.askdirectory(
        title="Select Game Server Directory"
    )

    if game_server_directory:
        default_file_path = os.path.join(
            game_server_directory, "DefaultPalWorldSettings.ini"
        )
        modified_file_path = os.path.join(
            game_server_directory, "Pal/Saved/Config/WindowsServer/PalWorldSettings.ini"
        )
        load_settings_from_ini()


def load_settings_from_ini():
    global default_pairs, modified_pairs
    default_pairs = load_settings(default_file_path, default_file_path)
    modified_pairs = load_settings(default_file_path, modified_file_path)
    if isinstance(modified_pairs, list):
        modified_pairs = dict(modified_pairs)
    display_settings(default_pairs, modified_pairs)

    position_top = int(root.winfo_screenheight() / 2 - root.winfo_height() / 2)
    position_left = int(root.winfo_screenwidth() / 2 - root.winfo_width() / 2)
    root.geometry(f"+{position_left}+{position_top}")


def save_settings_to_ini():
    modified_pairs = get_modified_pairs()
    if modified_pairs:
        save_modified_pairs(default_file_path, modified_file_path, modified_pairs)
        messagebox.showinfo("Success", "Settings saved successfully.")
    else:
        messagebox.showwarning("No Changes", "No changes to save.")


def update_settings_preset(preset):
    radio_var.set(4)
    if preset == "Casual":
        preset_pairs = casual_settings.copy()
    elif preset == "Normal":
        preset_pairs = normal_settings.copy()
    elif preset == "Hard":
        preset_pairs = hard_settings.copy()
    else:
        preset_pairs = dict(modified_pairs)
    for key, value in preset_pairs.items():
        if key in modified_pairs:
            modified_pairs[key] = value
    display_settings(default_pairs, modified_pairs)


def display_settings(default_pairs, modified_pairs):
    column_widths = [235, 260, 260, 535]
    current_rows = tree_view.get_children()
    num_rows_needed = len(default_pairs)
    if len(current_rows) < num_rows_needed:
        for _ in range(num_rows_needed - len(current_rows)):
            tree_view.insert("", "end")
    current_rows = tree_view.get_children()
    for i, (Setting, default_value) in enumerate(default_pairs):
        description = descriptions_dict.get(Setting, "No description found")
        tree_view.item(
            current_rows[i],
            values=(
                Setting,
                default_value,
                modified_pairs.get(Setting, "No value found"),
                description,
            ),
        )
    for i, column in enumerate(tree_view["columns"]):
        tree_view.column(column, width=column_widths[i], stretch=False)

    total_column_width = sum(column_widths)
    additional_space = 100
    window_width = total_column_width + additional_space
    window_height = root.winfo_height()

    position_top = root.winfo_screenheight() // 2 - window_height // 2
    position_left = root.winfo_screenwidth() // 2 - window_width // 2

    root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

    root.update_idletasks()

    position_top = root.winfo_screenheight() // 2 - root.winfo_height() // 2
    position_left = root.winfo_screenwidth() // 2 - root.winfo_width() // 2

    root.geometry(f"+{position_left}+{position_top}")


def get_modified_pairs():
    modified_pairs = {}
    for item in tree_view.get_children():
        Settings = tree_view.item(item, "values")[0]
        modified_value = tree_view.item(item, "values")[2]
        modified_pairs[Settings] = modified_value
    return modified_pairs


def direct_update_preset(preset):
    if preset == "Casual":
        preset_pairs = casual_settings.copy()
    elif preset == "Normal":
        preset_pairs = normal_settings.copy()
    elif preset == "Hard":
        preset_pairs = hard_settings.copy()
    else:
        preset_pairs = dict(modified_pairs)
    for key, value in preset_pairs.items():
        if key in modified_pairs:
            modified_pairs[key] = value
    display_settings(default_pairs, modified_pairs)


def get_current_preset():
    presets = {1: "Casual", 2: "Normal", 3: "Hard", 4: "Custom"}
    return presets[radio_var.get()]


def edit_item(event):
    row_id = tree_view.selection()[0]
    cell_value = tree_view.item(row_id)["values"][0]
    modified_value = tree_view.item(row_id)["values"][2]
    description_text = tree_view.item(row_id)["values"][3]

    new_window = tk.Toplevel(root)
    new_window.wm_protocol("WM_DELETE_WINDOW", root.bell)
    new_window.update_idletasks()

    window_width = new_window.winfo_width()
    window_height = new_window.winfo_height()

    position_top = int(new_window.winfo_screenheight() / 2 - window_height / 2)
    position_left = int(new_window.winfo_screenwidth() / 2 - window_width / 2)

    new_window.geometry(f"+{position_left}+{position_top}")

    tk.Label(new_window, text=f"Description: {description_text}").grid(
        row=0, column=0, columnspan=2, sticky="w"
    )
    tk.Label(new_window, text="Enter new value").grid(row=1, column=0, sticky="w")

    new_value = tk.StringVar()
    new_value_entry = tk.Entry(new_window, textvariable=new_value)
    new_value_entry.grid(row=1, column=1)
    new_value_entry.insert(0, modified_value)

    save_button = tk.Button(
        new_window,
        text="Save",
        command=lambda: [save_new_value(get_current_preset()), new_window.destroy()],
    )
    save_button.grid(row=2, column=1, sticky="w")

    def save_new_value(current_preset):
        new_modified_value = new_value_entry.get()
        modified_pairs[cell_value] = new_modified_value
        tree_view.item(
            row_id,
            values=(
                cell_value,
                tree_view.item(row_id)["values"][1],
                new_modified_value,
                tree_view.item(row_id)["values"][3],
            ),
        )

    settings_presets = {
        "Casual": casual_settings,
        "Normal": normal_settings,
        "Hard": hard_settings,
    }

    if (
        current_preset != "Custom"
        and cell_value in settings_presets[current_preset]  # checks if key exists
        and settings_presets[current_preset][cell_value] != new_modified_value
    ):
        radio_var.set(4)
    new_window.destroy()


root = tk.Tk()
root.title("PalPyServer")
window_width = 1300
window_height = 800
position_top = int(root.winfo_screenheight() / 2 - window_height / 2)
position_left = int(root.winfo_screenwidth() / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, fill=tk.X)

locate_button = tk.Button(
    button_frame, text="Locate Game Server", command=locate_game_server
)
locate_button.pack(side=tk.LEFT, padx=10)

load_button = tk.Button(
    button_frame, text="Load Settings", command=load_settings_from_ini
)
load_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(
    button_frame, text="Save Settings", command=save_settings_to_ini
)
save_button.pack(side=tk.LEFT, padx=10)


radio_var = tk.IntVar()
radio_var.set(2)

casual_radio = tk.Radiobutton(
    button_frame,
    text="Casual",
    variable=radio_var,
    value=1,
    command=lambda: direct_update_preset("Casual"),
)
casual_radio.pack(side=tk.LEFT, padx=10)

normal_radio = tk.Radiobutton(
    button_frame,
    text="Normal",
    variable=radio_var,
    value=2,
    command=lambda: direct_update_preset("Normal"),
)
normal_radio.pack(side=tk.LEFT, padx=10)

hard_radio = tk.Radiobutton(
    button_frame,
    text="Hard",
    variable=radio_var,
    value=3,
    command=lambda: direct_update_preset("Hard"),
)
hard_radio.pack(side=tk.LEFT, padx=10)

custom_radio = tk.Radiobutton(
    button_frame,
    text="Custom",
    variable=radio_var,
    value=4,
    command=lambda: update_settings_preset("Custom"),
)
custom_radio.pack(side=tk.LEFT, padx=10)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

tree_view = ttk.Treeview(
    table_frame,
    columns=("Settings", "Default Values", "Modified Values", "Descriptions"),
    show="headings",
)
tree_view.heading("#1", text="Settings")
tree_view.heading("#2", text="Default Values")
tree_view.heading("#3", text="Modified Values")
tree_view.heading("#4", text="Descriptions")
tree_view.column("#1", width=235, anchor=tk.W)
tree_view.column("#2", width=260, anchor=tk.W)
tree_view.column("#3", width=260, anchor=tk.W)
tree_view.column("#4", width=535, anchor=tk.W)
tree_view.pack(fill=tk.BOTH, expand=True)
tree_view.bind("<Double-1>", edit_item)

tree_scrollbar = ttk.Scrollbar(tree_view, orient=tk.VERTICAL, command=tree_view.yview)
tree_view.configure(yscroll=tree_scrollbar.set)
tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

default_file_path = ""
modified_file_path = ""
default_pairs = []
modified_pairs = []


root.mainloop()
