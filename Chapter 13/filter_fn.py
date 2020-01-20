def is_even(s):
    return s % 2 == 0


numbers = [2, 3, 4, 5, 4, 3, 2, 5, 6, 4]


is_even1 = list(filter(is_even, numbers))
print(is_even1)

# lambda

is_even1 = filter(lambda a: a % 2 == 0, numbers)
for i in is_even1:
    print(i)


for i in is_even1:
    print(i)


