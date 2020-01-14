# Create Program for gussing correct number
import random

winner_number = random.randint(0,10)

guss_number = int(input("Enter your gussing number (1 - 10): "))

if guss_number == winner_number:
    print("Congratulation! You Won.")
else:
    if guss_number > winner_number:
        print("Too high")
    else:
        print("Too Low")
