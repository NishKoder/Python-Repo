from functools import wraps
def decorator_fn(any_fn):
    @wraps(any_fn)
    def wrapper_funtion(*args, **kwargs):
        print("this is awesome")
        return any_fn(*args, **kwargs)

    return wrapper_funtion


@decorator_fn
def func(a, b):
    print(f"this is fn {a + b}")


func(2, 5)
