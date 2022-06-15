User_input = int(input("Enter a number: "))

def mySqrt(User_input: int) -> int:
    if User_input == 0 or User_input == 1:
        return User_input

    a = 1
    b = User_input
    square = 0

    while (a <= b):
        mid = (a + b) // 2
        if mid * mid == User_input:
            return mid
        elif mid * mid < User_input:
            a = mid + 1
            square = mid
        else:
            b = mid - 1
    return square


print(mySqrt(User_input))

input()