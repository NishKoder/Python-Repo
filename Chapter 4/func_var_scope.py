# scope

x = 5  # globle variable


def finc(x):
    global x  # now its become globle
    x = 7
    return x  # local variable


# print(x)# show error not define x
print(finc(x))
