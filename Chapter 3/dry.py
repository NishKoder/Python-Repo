# DRY - Dont Repeat YourSelf Principle

import random

winning_number = random.randint(1, 100)

gusse = 1
game_over = False
number = int(input("Enter gussing number: "))
while not game_over:  # can use break also
    if number == winning_number:
        print(f"you win, have guss {gusse}")
        game_over = True
    else:
        if number > winning_number:
            print("Too High")
        else:
            print("Too Low")
        gusse += 1
        number = int(input("Enter gussing again number: "))

