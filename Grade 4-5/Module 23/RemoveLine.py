# Remove specific lines (e.g., remove line 2)
with open("example.txt", "r") as file:
    lines = file.readlines()

with open("example.txt", "w") as file:
    for i, line in enumerate(lines):
        if i != 1:  # Skipping the second line (index 1)
            file.write(line)

print("Line 2 removed successfully.")
