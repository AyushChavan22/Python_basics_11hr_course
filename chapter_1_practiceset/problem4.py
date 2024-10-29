import os

def list_directory_contents(path='C:\\'):
    try:
        # list all files in the directory
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except Exception as e:
        print(f"An error occurred: {e}")
# example
list_directory_contents() #shows files in c drive

