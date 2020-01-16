# create fn which take list as paramenter and return square of each element with list
def square_list(lists):
    templist = []
    for list in lists:
        if type(list) == str:
            templist.append(list)
        else:
            templist.append(round(list * list, 2))
    return templist


print(square_list([2, 4, "hi", 6, 221, 7, "ji", 1.3]))


# create fn which return reverse list without reverse method or [::-1]
def reverse_list(lists):
    temp_list = []
    for list in range(len(lists)):
        temp_list.append(lists.pop())
    return temp_list


print(reverse_list([2, 4, "hi", 6, 221, 7, "ji", 1.3]))


# create fn which return reverse each element
def reverse_element(lists):
    temp_list = []
    for list in lists:
        if type(list) == str:
            temp_list.append(list[::-1])
        elif type(list) == float:
            temp_list.append(float(str(list)[::-1]))
        else:
            temp_list.append(int(str(list)[::-1]))
    return temp_list


print(reverse_element(["hid", "jdi", 283, 323.2]))


# create fn which return list which have even and odd number list


def even_odd_list(lists):
    temp_even = []
    temp_odd = []
    tempp = []
    for list in lists:
        if list % 2 == 0:
            temp_even.append(list)
        else:
            temp_odd.append(list)
    tempp.append(temp_even)
    tempp.append(temp_odd)
    return tempp


print(even_odd_list([34, 283, 323, 44, 54, 3, 4, 67, 443]))


# create fn which return list of common item list in two list
def common_list(list1, list2):
    temp_list = []
    for j in list1:
        for k in list2:
            if j == k:
                temp_list.append(k)
    return temp_list


print(common_list([34, 4, 66, 355, 343, 323], [34, 283, 323, 3, 4]))

# create fn which return number of list presence in list
def num_list(lists):
    counts = 0
    for n in lists:
        if type(n) == list:
            counts += 1
    return counts


print(num_list([34, 4, 66, 355, 343, [2, 43, 4], [2, 23], 323]))
