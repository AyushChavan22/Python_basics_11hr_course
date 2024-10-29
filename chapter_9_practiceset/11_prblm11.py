import os

def rename_file(current_file_path):
    new_file_name = "renamed_by_python.txt"
    directory = os.path.dirname(current_file_path)
    new_file_path = os.path.join(directory, new_file_name)

    try:
        os.rename(current_file_path, new_file_path)
        print(f"File renamed to {new_file_path}")
    except FileNotFoundError:
        print(f"File not found: {current_file_path}")
    except PermissionError:
        print(f"Permission denied: {current_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
current_file_path = r"C:\Users\AYUSH\OneDrive - Vidyalankar Institute of Technology\Desktop\python 10 hr course\chapter_9_practiceset\file.txt"
rename_file(current_file_path)
