import random

"""
2 forms of list comprehension:

    1. [x | for x in "hello"[:3]]
    2. [x | for x in iterable | if condition]
"""

# Usual list creation.
mylist = []
for _ in range(10):
    mylist.append(random.randint(1, 100))
print(mylist)

# List comprehension.
mylist = [
    -random.randint(1, 100) + random.randint(60, 100) 
    for _ in range(10)
]
print(mylist)

# List comprehension with conditional.
mylist = [
    random.randint(1, 100)
    for i in range(10)
    if i % 2 == 0
]
print(mylist)

"""
capital_letters = [
    char
    for char in input("Enter some text: ")
    if char.isupper()
    and char > "B"
]
print(capital_letters)
"""

text_for_2_lists = input("Enter some text for 2 lists: ")
odd_chars = [
    char
    for i, char in enumerate(text_for_2_lists, start=0)
    if i % 2 != 0
]
even_chars = [
    char
    for i, char in enumerate(text_for_2_lists, start=0)
    if i % 2 == 0
]
print(odd_chars)
print(even_chars)

# Dealing with nested lists.
"""
erroneous_list = [
    *sublist
    for sublist in [[1,2,3], [4,5,6]]
]
"""
values_from_nested_lists = [
    digit
    for sublist in [[1,2,3], [4,5,6], [1023012031203], [0, 1]]
    for digit in sublist
]
print(values_from_nested_lists)