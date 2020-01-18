# lambdas expression or anonymous function
def add(a, b):
    return a + b


add2 = lambda a, b: a + b

print(add2(2, 4))

# use with builtin fn like map , reduce , filter


# more lambda


def even_fn(a):
    return a % 2 == 0


print(even_fn(3))

# in lambda
even_fn2 = lambda a: a % 2 == 0
print(even_fn2(4))

# ex2
def last_char(s):
    return s[-1]


# in lambda
last_char2 = lambda s: s[-1]
print(last_char2("shdsn"))


# if else with lambda

def len_str(s):
    if len(s) > 5:
        return True
    else:
        return False

# in Lambda

len_str2 = lambda s: True if len(s) > 5 else False
print(len_str2("sdshjdg"))

