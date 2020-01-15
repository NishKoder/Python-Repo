# Take three input from user by comma seprated & show  avg b/w them

number1, number2, number3 = input("Please enter three number seprated by comma").split(
    ","
)
avg = (int(number1) + int(number2) + int(number3)) / 3
print(f"Average Of {number1}, {number2} & {number3} is = {round(avg,2)}")

