import os
import shutil
import argparse

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"]
}

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder does not exist.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            moved = False
            _, ext = os.path.splitext(file)

            for folder_name, extensions in FILE_TYPES.items():
                if ext.lower() in extensions:
                    destination = os.path.join(folder_path, folder_name)
                    os.makedirs(destination, exist_ok=True)
                    shutil.move(file_path, destination)
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, other_folder)

    print("✅ Folder organized successfully!")

def main():
    parser = argparse.ArgumentParser(description="Automatically organize files in a folder.")
    parser.add_argument("path", help="Path to the folder you want to organize")

    args = parser.parse_args()
    organize_folder(args.path)

if __name__ == "__main__":
    main()
