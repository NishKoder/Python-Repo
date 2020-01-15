# sum of digits of number

digit = "112"  # can use also input()
i = 0
total = 0
while i < len(digit):
    total += int(digit[i])
    i += 1
print(total)


# count string charater and show step by step

string = "String s"
i = 0
while i < len(string):
    print(f"{string[i]} - {i}")
    i += 1

