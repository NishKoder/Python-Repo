# map
def squre(a):
    return a ** 2


l = [2, 4, 3, 6, 8, 9]
print(list(map(squre, l)))

print([squre(item) for item in l])


# fun retrun fun
def outer_fn():
    def innner_fn():
        print("inside the func")

    return innner_fn


var = outer_fn()
var()


def outer_func2(msg):
    def inner_fun2():
        print(f"msg is {msg}")

    return inner_fun2


var2 = outer_func2("Hi their")
var2()
