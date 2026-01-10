#create a program for number guessing game
import random


def start_game():
    print("--- Welcome to the Number Guessing Game! ---")
    print("I'm thinking of a number between 1 and 100.")

    # The computer picks a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1

            # Logic check (Standard "Binary Search" style feedback)
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    if guess != secret_number:
        print(f"Game Over! The number was {secret_number}. Better luck next time!")


if __name__ == "__main__":
    start_game()