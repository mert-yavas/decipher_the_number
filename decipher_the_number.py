# This Python script is a number guessing game named "Decipher the Number".
# The game's main idea is for the player to guess a randomly selected number between 1 and 100 within a limited number of attempts.

from art import logo  # Imports the 'logo' function or variable from the 'art' library. This might be a visual displayed at the start of the game.
import random  # Imports the 'random' module for generating random numbers.

def main():
    print(logo)  # Displays the game logo.
    print("Welcome to the Decipher the Number!\nI'm thinking of a number between 1 and 100.")
    HEALTH = choose_level()  # Sets the number of attempts based on chosen difficulty level.
    guess_number = random.randint(1, 100)  # Randomly selects a number between 1 and 100.
    
    while HEALTH > 0:  # Continues the game as long as the player has remaining attempts.
        try:
            guess = int(input("Make a guess: "))  # Asks the player to enter a guess.
            if guess < guess_number:
                print("Too small!\nGuess again.")
                HEALTH -= 1  # Decreases the number of attempts after a wrong guess.
            elif guess > guess_number:
                print("Too large!\nGuess again.")
                HEALTH -= 1  # Decreases the number of attempts after a wrong guess.
            else:
                print(f"You got it! The answer was {guess}.")
                break  # Ends the loop if the guess is correct.

            if HEALTH > 0:
                print(f"You have {HEALTH} attempts remaining to guess the number.")
            else:
                print("You've run out of guesses, you lose.")
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handles invalid input (non-integer values).

def choose_level():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()  # Asks the player to choose a difficulty level.
        if difficulty == "easy":
            print("You have 10 attempts remaining to guess the number.")
            return 10  # Returns 10 attempts for 'easy' difficulty.
        elif difficulty == "hard":
            print("You have 5 attempts remaining to guess the number.")
            return 5  # Returns 5 attempts for 'hard' difficulty.
        else:
            print("Invalid input. Please select 'easy' or 'hard'.")  # Handles invalid input for difficulty level.

if __name__ == "__main__":
    main()  # Starts the game.
