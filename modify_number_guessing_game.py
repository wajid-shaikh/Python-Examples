# MODIFY NUMBER GUESSING GAME
import random
winning_number = 43 #random.randint(1,100)
guess = 1
number = int(input("enter number = "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess}")
        game_over = True
    else:
        if number < winning_number:
            print("too low")
            guess = guess + 1 
            number = int(input("guess again = "))
        else:
            print("too high")
            guess = guess + 1 
            number = int(input("guess again = "))
