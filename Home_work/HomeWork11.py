names = input("Enter a name after \" \": ")

names_list1 = names.strip().split()
names2 = set(names_list1)
names1 = set(name for name in names_list1 if names_list1.count(name) > 1)



print('Names that are not repeated: ', names2 - names1)

input()
