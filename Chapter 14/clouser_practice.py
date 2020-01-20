# first class fn or clouser

# square
# cube
#


def to_power(x):
    def cal_power(n):
        return print(f"{n**x}")

    return cal_power


cube = to_power(3)
cube(5)


squre = to_power(2)
squre(5)

