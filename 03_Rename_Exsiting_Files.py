# What would happen if :
## we try to rename a file that does not exist
### we try to rename a file to a name that already exists in the folder

import os

def rename_files():
    # (1) get file name from a folder
    file_list = os.listdir("/Users/waqaskhan/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " +saved_path)
    path = "/Users/waqaskhan/Downloads/prank"
    change_dir = os.chdir(path)
    print(change_dir)

    # (2) for each file, rename filename
    for file_name in file_list:
       # remove = "0123456789"
        os.rename(file_name, file_name.lstrip(None, "0123456789"))
    os.chdir(saved_path)

rename_files()