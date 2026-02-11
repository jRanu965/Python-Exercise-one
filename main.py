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

# Function to get a valid 'y' or 'n' response from the user

# Function to play one round of the game

# Ask for number range

# Ensure low_number is less than high_number

# Ask for number of attempts

# Generate random number

# Track number of attempts

# Loop for user guesses

# Check if guess is too low or too high

# Display success message if guessed correctly

# If max attempts are used up, reveal the correct number

# Main game loop

# Ask for user's name and greet them

# Ask if they want to play again, only accepting 'y' or 'n'

# Run the game