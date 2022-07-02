import random

number = int(input('Print your range of numbers:'))
lst = [random.randint(0,number) for i in range (0,number)]
print(lst)

number_to_find = int(input('Print your number for find :'))

is_found = False

for i in range(number):
    if is_found:
        break
    for j in range(i+1, number):
        if lst[i] + lst[j] == number_to_find:
            print("indicies:", i, j)
            is_found = True
            break
