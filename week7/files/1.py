import os
import shutil


# 1. List only directories, files, and all directories & files in a specified path
def list_contents(path):
    print("Directories:", [d for d in os.listdir(path)
          if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path)
          if os.path.isfile(os.path.join(path, f))])
    print("All Contents:", os.listdir(path))


list_contents(".")  
# 2. Check access to a specified path


def check_access(path):
    print(f"Path exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")


check_access("example.txt") 

# 3. Test if a path exists, then find filename and directory portion
def path_info(path):
    if os.path.exists(path):
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else:
        print("Path does not exist.")


path_info("example.txt")

# 4. Count the number of lines in a text file


def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            print(f"Number of lines: {sum(1 for _ in file)}")
    except FileNotFoundError:
        print("File not found.")


count_lines("example.txt") 

# 5. Write a list to a file
def write_list_to_file(file_path, data_list):
    with open(file_path, "w") as file:
        file.write("\n".join(data_list))


write_list_to_file("output.txt", ["Apple", "Banana", "Cherry"])

# 6. Generate 26 text files named A.txt to Z.txt
def create_alphabet_files():
    for letter in range(65, 91):  # ASCII values for A-Z
        with open(f"{chr(letter)}.txt", "w") as file:
            file.write(f"This is file {chr(letter)}")


create_alphabet_files()

# 7. Copy the contents of one file to another
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")
    except FileNotFoundError:
        print("Source file not found.")

copy_file("example.txt", "copy_example.txt")  



# 8. Delete a file after checking access and existence


def delete_file(file_path):
    if os.path.exists(file_path) and os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    else:
        print("File does not exist or cannot be deleted.")


delete_file("example.txt") 
