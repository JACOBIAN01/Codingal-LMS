# Copy content from one file to another
with open("example.txt", "r") as source_file:
    content = source_file.read()

with open("copy_example.txt", "w") as destination_file:
    destination_file.write(content)

print("File content copied successfully.")
