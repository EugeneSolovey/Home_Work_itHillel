user_input = int(input('Enter degree for a number 2: '))
result = 1
for _ in range(abs(user_input)):
    if user_input > 0:
        result *= 2
    elif user_input < 0:
        result /= 2
    else:
        break

print('Result for ascension 2 in', str(user_input), 'degree, that', str(result), '- through the cycle')
print()


def degree(num):
    if num > 0:
        return 2*degree(num-1)
    elif num < 0:
        return degree(num +1) / 2
    else:
        return 1

value = degree(user_input)

print('Result for ascension 2 in', str(user_input), 'degree, that', str(value), '- through recursion')