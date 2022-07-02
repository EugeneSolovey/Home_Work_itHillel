num = int(input("enter number: "))

numbers_count = 0
numbers_max = 10

while numbers_count < numbers_max:
    if num % 2 == 0:
        print(num)
    num += 1
    numbers_count += 1

print("Done")

# break - выход из цикла
# continue - пропустить текущую итерацию цикла
