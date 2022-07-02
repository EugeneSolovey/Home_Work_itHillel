# Dict
# {key: value}

pronunciations = {"one": 1}
pronunciations = {"two": 2, "three": 3}

# Key - only hashable
# Value - any type
some_key = 1, 2,
test_dict = {some_key: [1,2]}
# some_key[0] = 3  # Impossible
print(test_dict)

# KeyError if no such key exists
#print(pronunciations[2])
print(pronunciations["two"])

pronunciations["four"] = 4
print(pronunciations)

# Dict comprehension
some_dict = {
    number: number ** 2
    for number in range(0, 10)
    if number % 2 == 0
}
print(some_dict)

# 3 forms of iterations over dict

# 1. Over keys (the same)
for key in some_dict:
    print("key: ", key)
for key in some_dict.keys():
    print("key: ", key)

# 2. Over values
for value in some_dict.values():
    print("value: ", value)

# 3. Over pairs
for tup in some_dict.items():
    print("pair: ", tup, type(tup))

for key, value in some_dict.items():
    print("pair: ", key, value)


# Pros:

# 1. Ordered (since python3.7)
#user_dict = {i: input("...: ") for i in range(3)}
user_dict = {}
user_dict["name"] = "Alex"
for key, value in user_dict.items():
    print(key, value)

# 2. Fast getting values
dict_imitation = [(i, i ** 2) for i in range(10)]
print(dict_imitation)


# No duplicates in keys:
a = {"somelist": []}
a["somelist"] = 5

# Deletion:
# del a["somelist"]
print("Deleted value: ", a.pop("somelist"))


result = {"is_url_verified": True}
print(result)
is_verified = result.pop("is_url_verified", False)
print("is verified: ", is_verified, result)

is_verified = result.pop("is_url_verified", False)
print("is verified: ", is_verified, result)

somedict = {"a": 1, "b": 2, "c": 3}

try:
    print(somedict["z"])
except KeyError:
    print("no Z")

print(somedict.get("z", "no Z"))

some_dict = {"a": 1, "b": 2, "c": 3}
some_dict["d"] = 4
some_dict["e"] = 5
some_dict.update({"z": 26})
some_dict.update(one=1, two=2, three=3)
print(some_dict)

# Dict creations
somedict = {1:1}  # Literal ({:})
somedict = dict(a=1)  # By keyword arguments
print(somedict)


# Creation of empty dict (or set)
x = {}  # Dict by default
print(type(x))

# To create set:
someset = set()
print(type(someset))


# Sorting dicts.
somedict = {"z": 26, "y": 25}

for key in sorted(somedict.keys()):
    print(key, somedict[key])


print(new_dict := dict(sorted(somedict.items())))

new_dict.update({"z": 26, "y": 25})

print("walrus: ", new_dict)

# Walrus operator
x = 2
if is_even := (x % 2 == 0):
    print(is_even)
    