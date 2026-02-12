# Import random module to generate a random number
import random

# Function to get a valid integer input with error handling
def get_valid_integer(prompt): 
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Function to get a valid 'yes' or 'no' response from the user
def get_yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['yes', 'no']:
            return response
        else:
            print("Not correct!. Please enter 'yes' for yes to play again or 'no' for no not to play again.")

# Function to play one round of the game
def play_game():
    # Ask for number range 
    low_number = get_valid_integer("Enter the lowest number of your choice in the range: ")
    high_number = get_valid_integer("Enter the highest number of your choice in the range: ")
    while low_number >= high_number:
        print("The lowest number must be lower than the highest number.")
        low_number = get_valid_integer(" Please enter the lowest number in the range: ")
        high_number = get_valid_integer("Please enter the highest number in the range: ")  

    # Ask for number of attempts
    max_attempts = get_valid_integer("Enter the number of attempts you want to have: ") 

    # Generate random number
    random_number = random.randint(low_number, high_number) 
 
    # Track number of attempts
    attempts = 0

    # Loop for user guesses 
    while attempts < max_attempts:
        guess = get_valid_integer("Enter your guess: ")
        attempts += 1

        # Check if guess is too low or too high
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.") 
            return  # Exit the function if the guess is correct

    # If max attempts are used up, reveal the correct number
    print(f"you've used all {max_attempts} attempts. The correct number was {random_number}.") 

# Main game loop
def main():
    print("Welcome to the Number Guessing Game!")
    name = input("Please enter your name: ") 
    print(f"Hello, {name}! Let's start the game.") 
    
    while True:
        play_game()
        # Ask if they want to play again, only accepting 'yes' or 'no'
        play_again = get_yes_no("Do you want to play again? (yes/no): ")
        if play_again == 'no':
            print("Thank you for playing!") 
            break

# Run the game
if __name__ == "__main__":
    main() 