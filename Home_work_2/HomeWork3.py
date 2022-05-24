num = int(input('Введіть число: '))

a = int(num % 10 * 100)
b = int(num % 100 - num % 10)
c = int((num - num % 100) / 100)

print( num, '=> ' + str(a+b+c))

input()