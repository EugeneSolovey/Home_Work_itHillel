# !*-* utf-8 *-*

# Unicode - encoding standard
# Encodings: utf-8, utf-16, utf-32

# \u - 2 bytes \U - 4 bytes
print(chr(0x0001f600))
print("\U0001f600")
print(hex(ord("😀")))

# 4
print("\U00000034")
print("\u0034")

# str
string = 'The book is "Harry Potter"'

# Iterable object
for s in string:
    if s == ' ':
        break
else:
    print("The end")

# Iterator
it = iter(string)
print(it, next(it), next(it))

print(len(string))

# Indexable object
print(string[0], string[3], string[5], string[7])
print("Last: ", string[len(string) - 1])
print("Last: ", string[-1])

# Immutable object.
# string[5] = "w"
print("Copied with changed o: ", string[:5] + "w" + string[6:])

# Slicing
# as in range
print(string[0:len(string):1])
print(string[20:])

string = 'The boook is "Harry Pootter"'
# Functions and methods
len("asd")
print(string.count("oo", 10, 12))
print(string.find("Harry"), string[14:14+len("Harry")])
print(string.find("oo"), string.rfind("oo"), string.find("-"))
print(string[-1:])

print(string.replace(" ", "-", 2))

# python3.9 feature
string.removeprefix
string.removesuffix

string.startswith
string.endswith

print(string.lower())
print(string.upper())
print(string.title())
print(string.capitalize())

string += '.'
if not string.endswith("."):
    string += '.'
print(string)