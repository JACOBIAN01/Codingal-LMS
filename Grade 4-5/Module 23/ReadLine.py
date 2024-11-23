# Read file line by line
with open("example.txt", "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())
