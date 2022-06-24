"""
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.

Note that you will need to use the random library’s randint function.

Remember:
- Use functions to group code
- Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
- Check for invalid inputs, notifying the user and re-prompting for a valid input
"""

# import random lib to generate random number
import random


def display():
    """
     This function displays prompt messages
    """

    print('Welcome to guessing game.\nYou will guess a number between 1 and 100')


def generate_random_number():
    """
    This function generate a random number between 1 and 100
    """
    # generate number between 1 and 100 by randint
    random_number = random.randint(1, 100)
    return random_number


def get_input():
    """
    This function gets the user input and validates it.
    """
    # check if input is an integer by using try and except.
    try:
        guess = int(input('Please take a guess (type a number and hit enter)'))
        # if input is an integer, check if the input is between 1 and 100.
        if guess > 100 or guess < 1:
            print('number should be between 1 and 100')
            # if it's not between 1 and 100, ask user to input again
            get_input()
        # every requirement matches. return the guess.
        return guess

    # if input is not an integer prompt the user and run this function again
    except ValueError:
        print('please type a number')
        get_input()


def check_guess(guess, random_number):
    """
    This function check if the guess matches and give proper feedbacks.
    """
    if guess < random_number:
        print('The guess is lower')
    elif guess > random_number:
        print('The guess is higher')
    else:
        print('congrats. You are right!')


def main():
    """
    main function. run all functions one by one.
    """
    display()
    random_number = generate_random_number()
    guess = get_input()
    check_guess(guess, random_number)


main()

# e.g. random_number = 98, guess = 4  output: The guess is lower
#      random_number = 52, guess = 77  output: The guess is higher
#      random_number = 52, guess = 52  output: congrats. You are right!
