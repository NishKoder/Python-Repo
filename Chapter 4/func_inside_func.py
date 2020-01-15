def which_great(num1, num2):
    if num1 > num2:
        return num1
    return num2


# print(which_great(23,43))


def greatest(num1, num2, num3):
    biggest = which_great(num1, num2)
    return which_great(biggest, num3)


print(greatest(23, 431, 121))
