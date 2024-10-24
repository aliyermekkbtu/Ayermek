import os

def list_directories_files(path):
    # List only directories
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    # List only files
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    # List all directories and files
    print("\nAll Directories and Files:")
    for item in os.listdir(path):
        print(item)

# Specify the path
path = r"C:\Users\epmek\Desktop"  # You can change this to any valid path
list_directories_files(path)

