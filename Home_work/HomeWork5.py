count = 0
sum = 0
max = 0
min = None
while True:
    user_input = input( 'Enter number: ' )
    if user_input == '':
        break
    num = int(user_input)
    sum += num
    count += 1
    if num > max:
        max = num
    if min == None or num < min:
        min = num

print('Sum:', sum)
print('Max:', max)
print('Min:',min)
print('Average:', sum / count)

input()