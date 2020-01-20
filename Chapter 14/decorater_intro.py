# decorater - enhance functionality of other functions
# @ for decorator
def decorator_fn(any_fn):
    def wrapper_funtion():
        print("tihs is awesome")
        any_fn()

    return wrapper_funtion


# this is awesome fn
@decorator_fn
def func1():
    print("this is fn 1")


# this is awesome fn
def func2():
    print("this is fn 2")


func1()
func2()

