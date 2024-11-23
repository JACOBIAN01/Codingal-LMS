def remove_duplicates(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    unique_lines = list(set(lines))
    with open(file_name, "w") as file:
        file.writelines(unique_lines)

# Provide the file name with duplicate lines
remove_duplicates("example.txt")
