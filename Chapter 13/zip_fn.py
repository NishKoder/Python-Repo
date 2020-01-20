users = ["user1", "user2", "user3"]
names = ["name1", "name2", "name3"]

# zip fn return tuple

print(zip(users, names))

# we can change zip to dict easly

print(dict(zip(users, names)))


# more about zip function

# l1 = [1, 3, 5, 7]
# l2 = [2, 4, 6, 8]

l = [(1, 2), (3, 4), (5, 6), (7, 8)]


# unzip ur zip output

print(list(zip(*l)))
l1, l2 = list(zip(*l))
print(l1)
print(l2)
new_list = []

for pair in zip(l1, l2):
    new_list.append(min(pair))
print(f"Last  - {new_list}")

