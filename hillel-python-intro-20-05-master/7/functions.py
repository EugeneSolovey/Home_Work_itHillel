# Functions

# DRY - Don't Repeat Yourself (Не повторяйся)

# def - define (объявить)
def get_currency_amount():  # arguments list in ()
    pass


def get_currency_amount(currency_a, rate=29.5):  # arguments list in ()
    # optional docstring
    """
    Returns the amount of money in the currency.
    """
    return currency_a // rate

# Identical to:
# get_currency_amount = function definition ...


# In python everything is object (functions too)
print(id(get_currency_amount), hash(get_currency_amount))
print("Amount: ", get_currency_amount(8000, 35), type(get_currency_amount))
print("Amount: ", get_currency_amount(rate=29.25, currency_a=8000), type(get_currency_amount))

print("Amount: ", get_currency_amount(currency_a=10000), type(get_currency_amount))


# Default print argument value - sep
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, 5, sep=", ")



message = "Enter number: "
def insert_new_number(numbers_list=None):
    if numbers_list is None:
        numbers_list = []
    message = "Please give me a number: "

    new_number = int(input(message))
    numbers_list.append(new_number)
    print("All locals: ", locals())
    return numbers_list

#l = []
#print(insert_new_number(l), l)

print(insert_new_number())
#print(numbers_list)
# print(insert_new_number())

print(message)

# globals() locals()
print("All variables: ", type(globals()), globals())


# Namespaces:
# 1. Global namespace
# 2. Local namespace