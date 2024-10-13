import os
import shutil

# Define the directory path to organize
root_dir = 'F:\Additionnn'

# Define a dictionary to map file extensions to their corresponding directories
extension_dirs = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'videos': ['mp4', 'avi', 'mov', 'wmv'],
    'documents': ['docx', 'doc', 'pdf', 'txt'],
    'audio': ['mp3', 'wav', 'ogg'],
    'archives': ['zip', 'rar', '7z', 'tar']
}

def organize_files(root_dir):
    """
    Organize files in the root directory based on their extensions.
    """
    for filename in os.listdir(root_dir):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1][1:].lower()

        # Find the corresponding directory for the file extension
        for dir_name, extensions in extension_dirs.items():
            if file_ext in extensions:
                # Create the directory if it doesn't exist
                dir_path = os.path.join(root_dir, dir_name)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                # Move the file to its corresponding directory
                file_path = os.path.join(root_dir, filename)
                shutil.move(file_path, os.path.join(dir_path, filename))
                print(f"Moved {filename} to {dir_name} directory")
                break

if __name__ == "__main__":
    organize_files(root_dir)