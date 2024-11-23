import sys

def initial_slambook():
    try:
        row = int(input("Enter the number of people that will be answering the questions: "))
        cols = 6

        slam_book = []

        for i in range(row):
            print(f"\nEnter contact {i+1} details in the following order (ONLY):")
            print("NOTE: * indicates mandatory fields")
            print("..................................................................................")
            temp = []
            for j in range(cols):
                if j == 0:  # Name
                    name = input("Enter name*: ").strip()
                    if not name:
                        sys.exit("Name is a mandatory field. Exiting due to blank field...")
                    temp.append(name)
                elif j == 1:  # Age
                    age = input("Enter age: ").strip()
                    temp.append(age if age else None)
                elif j == 2:  # Hobbies
                    hobbies = input("Enter your hobbies: ").strip()
                    temp.append(hobbies if hobbies else None)
                elif j == 3:  # Favorites
                    favorites = input("Enter your favorite color, animal, number, sport, B.F.F, and grade: ").strip()
                    temp.append(favorites if favorites else None)
                elif j == 4:  # Likes/Dislikes
                    likes_dislikes = input("Enter something you hate and like about the person who made this slambook: ").strip()
                    temp.append(likes_dislikes if likes_dislikes else None)
            slam_book.append(temp)

        print("\nSlam Book Entries:")
        for entry in slam_book:
            print(entry)
        return slam_book
    except ValueError:
        sys.exit("Invalid input! Please enter a valid number for the rows.")

def thanks():
    print("***********************************************************************************")
    print("Thank you for checking out the slam book!")
    print("Please visit again!")
    print("***********************************************************************************")
    sys.exit("Goodbye, have a nice day!")

def instructions():
    print("..................................................................................")
    print("\tHOW TO USE A SLAM BOOK:")
    print("It's simple! Answer the questions and pass the slam book to the next person.")
    print("Have fun!")
    print("..................................................................................")

def menu():
    print("***********************************************************************************")
    print("\t\t\t\t\tSLAM BOOK DIRECTORY")
    print("***********************************************************************************")
    print("\tYou can now perform the following actions in this slam book:\n")
    print("1. Answer questions")
    print("Other numbers. Exit slambook")
    try:
        choice = int(input("Please enter your choice: "))
        return choice
    except ValueError:
        return -1  # Exit for invalid input

def main():
    print("..................................................................................")
    print("Hello dear friend, welcome to my slam book!")
    print("You may now proceed to explore my slam book.")
    print("..................................................................................")

    instructions()

    while True:
        choice = menu()
        if choice == 1:
            initial_slambook()
        else:
            thanks()

# Run the main function
if __name__ == "__main__":
    main()
