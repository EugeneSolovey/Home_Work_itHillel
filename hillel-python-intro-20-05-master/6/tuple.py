# Tuple - immutable data structure
some_tuple = (1, 2, 3, 4, 5)
print(some_tuple)

# can not be modified
some_tuple = (100, *some_tuple[1:])  # == (100, 2, 3, 4, 5)
#some_tuple[0] = 100
print(some_tuple)

# Packing and unpacking
some_tuple = ("hello", "world")
s1, s2 = some_tuple
print(s1, s2)

# length, width = (100, 200)

some_tuple = (1, 2, 3, 4, 5)
reversed_tuple = tuple(reversed(some_tuple))
print(reversed_tuple)
print(id(some_tuple), id(reversed_tuple))

# tuple() expects one iterable as argument
# print(tuple(1,2,3,4,5))  # error
print((1,2,3,4,5))

# tuple may be created without brackets `()`, only comma `,` is required
list = [1,2,3,4,5]
x = 1, 2, 3, 4, 5
print("The type of x is ", type(x))

# empty tuple
empty_list = []
x = ()
print("The type of x is ", type(x))

# one-element tuple
x = 2,
print("The type of x is ", type(x))

luggage = ("bag", "suitcase", "backpack")
luggage = ()

# WARNING: tuple is immutable, but tuple contents may be mutable
some_tuple = (1, "hi", [])
some_tuple[2].append("changed!")
print(some_tuple)