import os
import tkinter as tk
from tkinter import filedialog

def create_numbered_folders(root_folder):
    folder_counter = {"G": 1, "J": 1}

    for parent_dir, sub_dirs, files in os.walk(root_folder):
        # Skip the direct children of the root folder
        if parent_dir == root_folder:
            continue

        # Skip if the current subdirectory has no files
        if not files:
            continue

        # Get the first character of the parent folder name
        folder_type = parent_dir.split()[-1][0]

        # Determine the folder prefix based on the first character
        folder_prefix = "G" if folder_type == "G" else "D"

        # Get the folder counter based on the folder type
        current_counter = folder_counter.get(folder_type, 1)

        # Create the new folder name
        new_folder_name = f"{folder_prefix}{current_counter:02d}"
        new_folder_path = os.path.join(parent_dir, new_folder_name)
        os.makedirs(new_folder_path)

        # Increment the folder counter for the folder type
        folder_counter[folder_type] = current_counter + 1

def get_folder_from_user():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder_selected = filedialog.askdirectory(title="Select Parent Folder")
    return folder_selected

if __name__ == "__main__":
    parent_folder = get_folder_from_user()

    if parent_folder:
        create_numbered_folders(parent_folder)