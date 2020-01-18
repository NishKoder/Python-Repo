# list comprehension

# create list of square from 1 to 10
square = []
for i in range(1, 11):
    square.append(i ** 2)
print(square)

square2 = [i ** 2 for i in range(1, 11)]
print(square2)


# print negative number from 1 to 10
negative = []
for i in range(1, 11):
    negative.append(-i)
print(negative)

negative2 = [-i for i in range(1, 11)]
print(f"negative - {negative2}")


names = ["nish", "gupta", "jiiii"]
new_list = []
for name in names:
    new_list.append(name[0])
print(new_list)


new_list2 = [name[0] for name in names]
print(f"new list 2 : {new_list2}")


# reverse all string in list
new_list3 = [name[::-1] for name in names]
print(f"new list 3 : {new_list3}")


