# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number.
# if user guessed correctly then print "YOU WIN !!!!"
# if user didn't guessed correctly then :
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"
# google "how to generate random number in python " to generate random
# winning number

winning_number = 7

number = int(input('guess and enter the number between(1 - 10) = '))

if number == winning_number :
    print('YOU WIN !!!!')
else:
    if number < winning_number :
        print('too low')
    else:
        print('too high')