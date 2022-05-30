num = input('Enter numbers: ')
Quantity = len(num)
print(Quantity)
sum = 0
a = 0
b = 9
for i in range(Quantity):
    sum += int(num[i])
    if int(num[i]) > a:
        a = int(num[i])
    elif int(num[i]) < b:
        b = int(num[i])
    else:
        continue

print(sum)
print(a, b)
print(sum / Quantity)

input()