import os
import shutil
import tkinter as tk
from tkinter import filedialog

MAX_DEPTH = 2

def create_numbered_folders(root_folder):
    folder_counter = {"G": 1, "D": 1}

    for parent_dir, _, files in os.walk(root_folder):
        # Calculate the current depth relative to the root folder
        depth = parent_dir[len(root_folder):].count(os.path.sep)

        # Skip if the current depth exceeds the limit or is not 1 (second depth)
        if depth > MAX_DEPTH or depth != 2:
            continue

        # Get the first character of the parent folder name
        folder_type = parent_dir.split()[-1][0]

        # Get the existing numbered folders at the second level
        existing_folders = [folder for folder in os.listdir(parent_dir) if folder.startswith((folder_type))]
        existing_numbers = [int(folder[1:]) for folder in existing_folders if folder[1:].isdigit()]

        # Find the maximum existing number or start from 1 if there are no existing folders
        max_existing_number = max(existing_numbers) if existing_numbers else 0

        # Get the folder counter based on the folder type
        current_counter = max(folder_counter.get(folder_type, 1), max_existing_number + 1)

        # Create the new folder name
        folder_prefix = "G" if folder_type == "G" else "D"
        new_folder_name = f"{folder_prefix}{current_counter:02d}"
        new_folder_path = os.path.join(parent_dir, new_folder_name)

        # Remove the existing folder if it exists
        if os.path.exists(new_folder_path):
            shutil.rmtree(new_folder_path)

        # Create the new folder
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
