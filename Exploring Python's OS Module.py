#Question 1 Task 1
import os

def list_directory_contents(path):
# List and print all files and subdirectories in the given path
    try:
        for entry in os.scandir(path):
            if entry.is_file():
                print(f"File: {entry.path}")
            elif entry.is_dir():
                print(f"Directory: {entry.path}")
            list_directory_contents(entry.path)
    except Exception as e:
        print(f"An Error Occurred!: {e}")

if __name__ == "__main__":
    target_path = "."
    list_directory_contents(target_path)