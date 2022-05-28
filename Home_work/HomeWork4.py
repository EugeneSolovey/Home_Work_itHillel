num = int(input('Enter number: '))
if num > 1:
    for i in range(2, int(num/2)+1):
         if(num % i) == 0:
            print("Number is not simple")
            break
    else:
        print("Number is simple")
count=0
for i in range(2, num+1):
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i, end=' ')
    else:
        count = 0

input()