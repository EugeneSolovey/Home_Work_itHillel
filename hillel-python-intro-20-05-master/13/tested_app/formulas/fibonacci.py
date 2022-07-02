def fibonacci(number) -> int:
    a = 0
    b = 1
    for _ in range(number):
        a, b = b, a + b
    return b


"""
# Global vars - evil! Untestable.

a = 0
b = 1

def fibonacci(number) -> int:
    global a
    global b
    for _ in range(number):
        a, b = b, a + b
    return
"""
