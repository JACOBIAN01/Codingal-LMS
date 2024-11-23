import os

# Delete the file
file_name = "example.txt"
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"The file '{file_name}' has been deleted.")
else:
    print(f"The file '{file_name}' does not exist.")
