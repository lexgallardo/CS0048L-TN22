def main():
    scores = []

    while True:
        print("\nMenu:")
        print("1. Add Score")
        print("2. Calculate Average")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            subject = input("Enter the subject: ")
            try:
                score = float(input("Enter the score: "))
                if 0 <= score <= 100:
                    scores.append((subject, score))
                    print("Score added.")
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric score.")
        
        elif choice == '2':
            if scores:
                average = sum(score for _, score in scores) / len(scores)
                print(f"Average Grade: {average:.2f}")
            else:
                print("No scores available to calculate average.")
        
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
