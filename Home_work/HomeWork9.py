import random

num1 = int(input("Enter number: "))
list1 = [random.randint(0, num1) for i in range(num1)]
# print(list1)
num2 = input("Enter number: ")
if num1 > 1 and num2 != "":
    num2 = int(num2)
    for i, num in enumerate(list1):
        if num == num2:
            if 0 < i < len(list1) - 1:
                print(list1[i-1], list1[i+1])
            elif i == 0:
                print(list1[i+1])
            elif i == len(list1) - 1:
                print(list1[i-1])
            break

        elif num2 not in list1:
            print('The entered number is not in the list')
            break

else:
    print('You did not enter a number or the number you entered does not have adjacent numbers in the list')

input()