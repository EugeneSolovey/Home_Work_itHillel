import random

num1 = int(input("Enter number: "))
list1 = [random.randint(0, num1) for i in range(num1)]

# print(list1)

num2 = int(input("Enter number: "))

for i, num in enumerate(list1):
    for j in range(i+1, len(list1)):
        if list1[i] + list1[j] == num2:
            print('Index of numbers whose sum is equal to the entered: ', i, 'and', j)
            break

    if list1.index(num) == len(list1) - 1:
        print('There are no numbers in the list whose sum is equal to the one entered')
        break

input()