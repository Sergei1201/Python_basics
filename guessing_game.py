import math
import random

# Enter a range of numbers for starting a guessing game
lower_number = int(input('Enter a lower number: '))
upper_number = int(input('Enter an upper number: '))

# Generate a random integer number in the range between lower_numbber and upper_number
x = random.randint(lower_number, upper_number)
print(
    f'You have only {round(math.log(upper_number - lower_number +1 ,2))} guesses')

# Implement a while loop to start the game and check the following condition which says that
# The number of guesses can't be more than the minimum number of guesses to find out the number in the range
# The number of guesses depends upon the range and calculates according to the formula
# Minimum number of guessing = log2(Upper bound - lower bound + 1)

# Initializing the number of guesses
count = 0
while count <= math.log(upper_number - lower_number + 1, 2):
    count += 1
    # Taking a number from input
    guess = int(input('Guess a number: '))
    if x == guess:
        print(
            f'Congratulations! You have guessed the number in {count} tries ')
        break
    elif x > guess:
        print('Your guess is too small. Try again')
    elif x < guess:
        print('You guess is too high. Try again')
# If guessing is more than allowed guesses, show the output
if count > math.log(upper_number - lower_number + 1, 2):
    print(
        f'You have exceeded the number of possible guesses. The number you have been looking for is {x}')
    print('\n Good luck next time')
