import os

from modules.detect_os import detect_os


def create_data_folder():
    os_name = detect_os()

    # Get the path to the desktop based on the operating system
    if os_name == "Windows":
        desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
    elif os_name == "Linux" or os_name == "Darwin":
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    else:
        print("Unsupported operating system. Cannot determine desktop path.")
        return

    # Define the path to the data folder
    data_folder_path = os.path.join(desktop_path, "data")

    # Create the data folder if it doesn't exist
    if not os.path.exists(data_folder_path):
        os.makedirs(data_folder_path)
        print(f"Created folder: {data_folder_path}")
    else:
        print(f"Folder already exists: {data_folder_path}")

    # List of subfolders to create within the data folder
    subfolders = ["indice", "stock", "ma", "broad"]

    for subfolder in subfolders:
        subfolder_path = os.path.join(data_folder_path, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            print(f"Created folder: {subfolder_path}")
        else:
            print(f"Folder already exists: {subfolder_path}")