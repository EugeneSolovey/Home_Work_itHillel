# *args **kwargs

num1, num2 = (5, 10)
print(num1)
print(num2)

print([5, *[10,11,12]])
print({"a": 5, **{"b": 10, "c": 11, "d": 12}})
print(dict(a=5, **{"b": 10, "c": 11, "d": 12}))

def f(*args, **kwargs):
    print(args)
    print(kwargs)


print(1, 5, 3, 123)


def custom_sum(x, *numbers, **params):
    print(params, type(params))
    print(numbers, type(numbers))
    print("Got numbers:", *numbers)
    return sum(numbers)


print(custom_sum(1,2,3, reverse=True, name="John"))
print(custom_sum(0))



def print_setting(setting: bool):
    print("Setting:", setting)


def start_app(**kwargs):
    print_setting(**kwargs)
    print_setting(setting=True)


start_app(setting=True)

