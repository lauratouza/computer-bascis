def main():
    # Ask for the user's name
    name = input("What's your name? ")

    # Ask for the user's date of birth
    date_of_birth = input("When is your birthday? (dd/mm/yyyy) ")

    # Ask for the user's hobbies
    hobbies = input("What are your hobbies? ")

    # Print the user's information
    print(f"\nNice to meet you, {name}!")
    print(f"Your birthday is on {date_of_birth}.")
    print(f"And you enjoy {hobbies}.")

# Run the main function
if __name__ == "__main__":
    main()
