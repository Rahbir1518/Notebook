import os

def screenshot_organize():
    file_path = "C:\\SS\\"

    # current directory
    work_directory = os.chdir(file_path)
    files_in_folder = os.listdir(file_path)

    for files in files_in_folder:
        new_name = "text.png"
        new_path_directory = os.path.join(file_path, new_name)
        os.rename(files, new_path_directory)
    
if __name__ == "__main__":
    screenshot_organize()