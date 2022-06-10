import random

num1 = int(input("Enter number: "))
list1 = [random.randint(0, num1) for i in range(num1)]

print(list1)

count = 0
num2 = int(input("Enter number: "))

for i, num in enumerate(list1):
 #   print(i, num, end=', ')
  #  print()
    if list1[count] + num == num2:
        if i > 0 and count == i:
            count += 1
            continue
        print(list1[count], num)
        print('Index of numbers whose sum is equal to the entered: ', count, 'and', i)
        break
  #  elif list1[count] + num != num2:
  #      print( list1[count], num )
   #     count += 1
    elif count == num1 - 1:
        print('There are no numbers in the list whose sum is equal to the one entered!')
        break

input()