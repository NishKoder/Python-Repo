# list comprehencsion in if statement
number_list = list(range(1, 11))


def normal_method_even_number(list):
    num = []
    for n in list:
        if n % 2 == 0:
            num.append(n)
    return num


print(normal_method_even_number(number_list))


def comprehence_list_with_if(list):
    return [i for i in list if i % 2 != 0]

print(comprehence_list_with_if(number_list))


# convert all int and float to string
def num_to_str(list):
    return [str(i) for i in list if type(i) == int or type(i) == float]
print(num_to_str([2,1.2,"we",[2,4]]))


# show list if odd number comes then put -1 and if even number occur then multiply it
def odd_even_if_else(list):
    return [i*2 if i%2 == 0 and type(i) == int or type(i) == float else -1 for i in list]

print(odd_even_if_else([2,1.2,3]))



