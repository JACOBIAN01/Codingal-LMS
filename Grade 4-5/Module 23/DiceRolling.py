import random

def roll_dice():
    while True:
        print(f"You rolled: {random.randint(1, 6)}")
        roll_again = input("Roll again? (yes/no): ").strip().lower()
        if roll_again != 'yes':
            break

roll_dice()
