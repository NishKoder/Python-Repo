# Take two comma seprated inputs from two
# 1 - user name
# 2 - a single character

# Output - two line print
# 1 - user name length
# 2 - count the character that user inputed(bonus: case insentive count)


name, onechar = input("Enter name & One Character Splited by Comma: ").split(",")
print(len(name) + 1)
print(name.lower().count(onechar))
