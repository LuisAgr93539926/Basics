import os
import shutil
from tkinter import filedialog


def create_folder(path: str, extension: str) -> str:
    """Create folder based on the file extension"""
    folder_name: str = extension[
        1:
    ]  # returns the extension without the dot (e.g., .png -> png)
    folder_path: str = os.path.join(path, folder_name)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)  # makedirs()

    return folder_path


def sort_files(source_path: str):
    """Sort files based on the path"""
    for root_dir, sub_dir, filenames in os.walk(source_path):
        for filename in filenames:
            extension: str = os.path.splitext(filename)[1]
            file_path: str = os.path.join(root_dir, filename)

            if not os.path.exists(extension):
                folder: str = create_folder(source_path, extension)
                target_path: str = os.path.join(folder, filename)
                shutil.move(file_path, target_path)


def delete_empty_folders(path: str):
    for root_dir, sub_dir, filenames in os.walk(path, topdown=False):
        for directory in sub_dir:
            directory_path = os.path.join(path, directory)
            if not os.listdir(directory_path):
                os.removedirs(directory_path)


if __name__ == "__main__":
    source_path: str = filedialog.askdirectory()
    if os.path.exists(source_path):
        sort_files(source_path)
        delete_empty_folders(source_path)
        print("Files sorted by extension!")
    else:
        print("Invalid path")
