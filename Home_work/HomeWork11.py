user_names = input("Enter name: ")
names = list(user_names)
names2 = names.copy()
count = 0
print(names)
print(names2)
'''for i in names:
    if i in names2:
        count += 1
        if count == 2:
            names2.discard(i)
'''




print("Children's names without namesake", set(names) - set(names2))

