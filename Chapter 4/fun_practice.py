# func to return last value of string
def last_letter(strings):
    print(strings[-1])


last_letter(str(12322))


# func check number is odd or even
# def even_ood(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"


# print(even_ood(64))


def even_ood(num):  # paramenter
    if num % 2 == 0:
        return "even"
    return "odd"


print(even_ood(64))  # agrument


def is_even(num):
    return num % 2 == 0


print(is_even(23))



# which number is greater
def which_great(num1,num2):
    if num1 > num2:
        return num1
    return num2
print(which_great(23,43))