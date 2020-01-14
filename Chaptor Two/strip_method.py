name = "      pyt  hon     "
dots = "................."
# lstrip() method for remove left side space
# rstrip() method for remove right side space

print(name + dots)

print(name.lstrip() + dots)

print(name.rstrip() + dots)

print(name.strip() + dots)

print(name.replace(" ", ""))



# Output:

#       pyt  hon     .................
# pyt  hon     .................
#       pyt  hon.................
# pyt  hon.................
# python