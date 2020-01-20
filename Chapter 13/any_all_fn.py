# all() check list have all value is true or not

print(all([True, True, True, True]))  # True
print(all([True, False, True, True]))  # False

# any() check list have atleast one value is true

print(any([False, False, False, False]))  # False
print(any([False, False, False, True]))  # True


# Practice
def sun_fn(*agrs):
    if all([type(arg) == int or type(arg) == float for arg in agrs]):
        total = 0
        for num in agrs:
            total += num
        return total
    else:
        return "Wrong Type"


print(sun_fn(3, 5, 3.2))

