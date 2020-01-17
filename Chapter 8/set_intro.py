# set data type
# unordered collection of unique items
sets = {4,2,3}
# print(sets)


# # list conveert to sets & remove duplicate value
# l = [3,3,3,3,1,1,13,3,55,55,55,1]
# s2 = list(set(l))
# print(s2)

sets.add(44)

sets.remove(3)

# if you want not error
sets.discard(54)

print(sets.clear())

# not store list , dict, tuple
sets = {4,2,3}
s1 = sets.copy()
print(s1)


# set math
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s2.union(s1))
print(s2.intersection(s1))