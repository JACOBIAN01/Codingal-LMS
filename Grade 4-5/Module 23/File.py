# Creating and writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("File handling in Python is simple and useful.\n")

# Reading from the file
with open("example.txt", "r") as file:
    content = file.read()
    print("Reading the file:")
    print(content)

# Appending to the file
with open("example.txt", "a") as file:
    file.write("This line is added later.\n")

# Reading the updated file
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("Reading the updated file:")
    print(updated_content)
