numbers = [3, 4, 5, 6, 1, 2]

square = map(lambda a: a ** 2, numbers)

for i in square:
    print(i)

print(square)


number_iter = iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
