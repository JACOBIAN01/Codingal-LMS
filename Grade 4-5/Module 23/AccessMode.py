# Example using "r+" mode (read and write)
with open("example.txt", "r+") as file:
    content = file.read()
    print("Original content:")
    print(content)
    file.write("\nNew content added in r+ mode.")
