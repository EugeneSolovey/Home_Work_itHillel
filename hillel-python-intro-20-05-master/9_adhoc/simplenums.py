x = int(input("Enter a number: "))

"""
def is_number_prime(number: int) -> bool:
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    else:
        is_prime = True
    return is_prime
"""

# any(), all()
# is_prime = not any(number % i == 0 for i in range(2, number))
def is_number_prime(number: int) -> bool:
    if number < 2:
        return False
    is_prime = all(number % i != 0 for i in range(2, number))
    return is_prime


print("Is prime: ", is_number_prime(x))
print()
print("Simple numbers in range:")
for i in range(2, x):
    if is_number_prime(i):
        print(i)