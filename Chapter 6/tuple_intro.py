# is same as list but its imutable and use ()
# No(pop , append , insert, remove)
# its faster rather than list

name = (23, 34, "34")  # when u not want to change ur data means WeekDays, Months etc

# Tuple Methods
# Count
# index
# len
# slice - [:3]

# More About Tuple

# For Loop in tuple
mixed = (2, 4, 5, 2.3)
for i in mixed:
    print(i, end=" ")

# tuple with one element
# num = (1)# Not a tuple need to put comma
num = (1,)
print(type(num))

# tuple without paranthesis
num1 = 2, 3, 5
print(type(num1))

# tuple unpacking
unpack = (3, 4)
a, b = unpack
print(a, end=" ")
print(b)


# final tuple
numss = tuple(range(1, 10))
print(list(numss))  # tuple to list

