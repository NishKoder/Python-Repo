name_list = ["ni", "sds", "sd", 3, 5]
for name in name_list:
    print(name)


# List inside List

matrix = [[1, 3, 4], [2, 5, 2], [4, 2, 4]]
print(matrix[1])
for i in matrix:
    for j in i:
        print(type(j))

# more about list
num = list(range(1, 21))
print(num)
num.pop()  # return pop value

print(num)
# index method
print(num.index(3, 2, 5))

