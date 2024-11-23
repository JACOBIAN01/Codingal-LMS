
def is_disarium(number):
    # Convert the number to a string for position indexing
    num_str = str(number)
    # Calculate the sum of each digit raised to the power of its position
    disarium_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    # Check if the sum equals the original number
    return disarium_sum == number

# Input from the user
num = int(input("Enter a number: "))

if is_disarium(num):
    print(f"{num} is a Disarium Number.")
else:
    print(f"{num} is not a Disarium Number.")
