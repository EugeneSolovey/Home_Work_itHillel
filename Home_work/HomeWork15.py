user_input = int( input( 'Enter number: ' ) )

previous = correct = 1

if user_input >= 2:
    for _ in range((user_input - 2)):
        previous, correct = correct, previous + correct
    print( 'Fibonacci number for', str( user_input ), 'is', str( correct ), '- through the cycle' )
else:
    print('Fibonacci number for', str(user_input), 'is', str(user_input), '- through the cycle')




def fibo_numb(num: int) -> int:
    correct2 = 1
    if num >= 2:
        correct2 = fibo_numb(num - 1) + fibo_numb(num - 2)
    else:
        return num
    return correct2


result = fibo_numb(user_input)

print('Fibonacci number for', str(user_input), 'is', str(result), '- through recursion')

input()
