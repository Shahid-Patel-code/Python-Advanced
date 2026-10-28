import datetime as dt

candidates = ["Alice", "Bob", "Charlie", "Diana"]


def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                return age
        except ValueError:
            print("Please enter a valid number for age.")


def get_valid_candidate():
    while True:
        print("Choose a candidate:")
        for index, candidate in enumerate(candidates, start=1):
            print(f"{index}. {candidate}")

        try:
            choice = int(input("Enter the number of your candidate: "))
            if 1 <= choice <= len(candidates):
                return candidates[choice - 1]
            print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Please enter a valid number.")


def voter_registration():
    print("\n=== PVM (Python Voting Machine) ===")
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    age = get_valid_age()

    if age < 18:
        print(f"{name}, you are not eligible to vote.")
        return

    candidate = get_valid_candidate()
    print(f"\nThank you, {name}!")
    print(f"Your vote for {candidate} has been recorded.")


if __name__ == "__main__":
    voter_registration()
