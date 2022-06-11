names = input("Enter a name after \",\": ")
names = names.replace(" ", "")

names_list1 = names.split(',')
names2 = set(names_list1)
names1 = []

for i, name in enumerate(names_list1):
    while names_list1.count(name) > 1:
        names1.append(names_list1.pop(i))


print('Names that are not repeated: ',names2 - set(names1))

input()
