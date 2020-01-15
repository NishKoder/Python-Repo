# Modify gussing Number

import random

winning_number = random.randint(1, 100)

gusse = 1
game_over = False
number = int(input("Enter gussing number: "))
while not game_over:
    if number == winning_number:
        print(f"you win, have guss {gusse}")
        game_over = True
    else:
        if number > winning_number:
            print("Too High")
            gusse += 1
            number = int(input("Enter gussing number: "))
        else:
            print("Too Low")
            gusse += 1
            number = int(input("Enter gussing number: "))

