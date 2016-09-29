#!/usr/bin/python3

from random import randint

answer = randint(0,50)    # Make a random number between 0 and 50
counter = 0               # Keep track of number of guesses
while True:
    try:
        guess = int(input('Guess an integer [0,50]: '))  # Get a value from user
    except ValueError:
        print('Please use a numeric type!')   # remind the user to input numbers
        continue

    counter+=1     # Add 1 to the counter
    if guess > answer:
        print('Too High!')

    elif guess < answer:
        print('Too Low!')

    else:
        print('You got it!')
        if counter < 10:    # if the player is good, let them know!
            print('Wow! that took you {} tries'.format(counter))
        else:
            print('It took you {} tries'.format(counter))
        break

print('Thanks for playing!')
