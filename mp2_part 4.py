import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\nGuess the number between 1 and 100:")

    while True:
        try:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number within the range 1 to 100.")
            elif guess > number_to_guess:
                print("Too high!")
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\nMenu:")
        print("1. Play Number Guessing Game")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            play_game()
        elif choice == '2':
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
