# Sets pros
bad_years = {2019, 2022, 2014, 1991}

# Collisions:
# put 2019 in set -> 0x2315123
# put -123125123 in set -> 0x2315123
# then: create at 0x2315123 a list with [2019, -123125123]

#entered_year = int(input("Enter some year: "))
#print("Is enter bad? ", entered_year in bad_years)


all_users = {"Vasia", "Petia", "Vania"}
ukrainian_users = {"Petia", "Vasia"}
poland_users = {"Matek", "Krzysztof"}

# 6 lookup (len(all_user) x len(ukrainian_users))
for user in all_users:
    if user not in ukrainian_users:
        print("Non ukrainian: ", user)

print("Non-ukrainian users: ", all_users - ukrainian_users)

# Same - union (объединение)
print("Ukrainian-poland users", ukrainian_users | poland_users)
print("Ukrainian-poland users", ukrainian_users.union(poland_users))

# Hashable == immutable
l = (1,2,3)
print("Hash: ", hash(l))

#l = (1,2,[])
#print("Hash: ", hash(l))
print({(1,2,3)})
# print({(1,2,[])}) # error


some_set = {1,2,3}
some_set.copy()
some_set.add(4)
some_set.discard(3)
print(some_set)
# print(some_set[0]) # not indexable

for elem in some_set:
    print(elem)


"""
char_set = {
    char
    for char in input("Some text: ")
    if char.isupper()
}
c = input("Enter new char: ")
print(c in char_set)
"""

# Mutable and immutable sets
set  # mutable
frozenset  # immutable

currency_chars = frozenset({"$"})
print(currency_chars)

# Sets accept hashable (immutable) objects only.

# Set in-memory representation.
# 2014 - one place
# ...
# 2022 - different place
# ...


odesa_streets = ["deribasovskaia", "pushkinskaia", "miasoedovskaia", "24th line", "10th line"]
central_strees = ["deribasovskaia", "khreshchiatik"]

# Все ли улицы central_strees Одесские?
for street in central_strees:
    if street not in odesa_streets:
        print("Not Odesa street: ", street)
        break
else:
    print("All central streets are Odesa streets")


print("Is all from Odesa?", set(central_strees).issubset(odesa_streets))
print("Not Odesa streets:", set(central_strees) - set(odesa_streets))
print("Odesa central streets:", set(central_strees) & set(odesa_streets))
