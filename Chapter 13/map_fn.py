number = [3, 4, 6, 2, 9, 7, 3]


def squaore(a):
    return a ** 2


sq = list(map(squaore, number))
print(sq)

sq1 = list(map(lambda a: a ** 2, number))

print(sq)

# Map fn is iterator

