# make flexible fn - by me
# *operator
# *args


def all_total(*args):
    total = 0
    for i in args:
        total += i
    return total


print(f" Total - {all_total(2,42,23,4,3,2)}")


# args with normal parameter
def multi_num(num, *args):
    multi = 1
    for i in args:
        multi *= i
    return multi


print(f" Multiply - {multi_num(4,3,2)}")

# args as arguments
def multi_nums(*args):
    multi = 1
    for i in args:
        multi *= i
    return multi


nums = [4, 4, 3, 2]
print(multi_nums(*nums))  # if want to send list & tuple then * when u call mthd


# fn with number and args and make power of num
def power_num(num, *args):
    if args:
        return [i ** num for i in args]
    else:
        return "Din't pass"


print(power_num(4, *[1, 2, 3, 4]))
print(power_num(4))

# **kwargs (keyword agrument) - Key value
# **kwargs (double star oprator)

# kwargs as a parameter


def kwfunc(**kwargs):
    print(type(kwargs))  # type is dict


kwfunc()


def kwfuncb(**kwargs):
    return {f"{k} - {v}" for k, v in kwargs.items()}


print(kwfuncb(name="asd", aa="ads"))


def kwfuncbs(names, **kwargs):
    return {f"{k} - {v}" for k, v in kwargs.items()}


print(kwfuncbs("as", name="asd", aa="ads"))

# dict unpacking
d = {"name": "sds", "age": 32}
print(kwfuncbs("as", **d))


# paramenter order in Function

# paramenter
# *args
# default parameter
# **kwargs


# return string list with First letter capital
def first_cap(*args, **kwargs):
    return [name.title() if kwargs.get("reverses") == True else name for name in args]


num = ["nish", "coder"]
print(first_cap(*num, reverses=False))

