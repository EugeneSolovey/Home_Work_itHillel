names = input("Enter names: ").split()


unique_names = [i for i in names if names.count(i) == 1]
print(unique_names)


# Proposed solution:
seen = set()
duplicates = set()

for name in names:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

print("Duplicates: ", duplicates)
print(seen - duplicates)
