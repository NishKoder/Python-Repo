# use for track position of for loop

# without enumrate
names = ["abc", "abcd", "sss", "abcdef"]
pos = 0
for name in names:
    print(f"{pos} -- {name}", end=" & ")
    pos += 1
print("")
# with enumrate
for pos, name in enumerate(names):
    print(f"{pos} -- {name}")
