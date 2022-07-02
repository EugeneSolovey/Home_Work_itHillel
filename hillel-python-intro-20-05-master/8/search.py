import random


# 1. Ordered
digits = [1, 5, 8, 10, 12, 27, 30, 69, 100]

# to find: 5
"""
[1, 5, 8, 10, 12, 27, 30, 69, 100]
5 < 12 : [1, 5, 8, 10]
5 < 8 : [1, 5]
(5 < 5 = False) -> 5 == 5 = True
"""

to_find = int(input("Enter number to find: "))

# Linear search. (перебор)
# Complexity: O(n)
i = 0
for x in digits:
    i += 1
    if x == to_find:
        print(f"Linear: found by {i} iterations")
        break

# 1. Ordered
digits = [1, 5, 8, 10, 12, 27, 30, 69, 100]

def binary_search_iterative(sequence, value) -> int:
    i = 0
    left = 0
    right = len(sequence) - 1
    while left <= right:
        print("Searching in:", sequence[left:right+1])
        middle = (left + right) // 2
        i += 1
        if sequence[middle] < value:
            left = middle + 1
        elif sequence[middle] > value:
            right = middle - 1
        else:
            index = middle
            break
    else:
        index = -1
    print(f"Binary iterative: found by {i} iterations")
    return index

binary_search_iterative(digits, to_find)


"""
data = [100, ..., 1000000]
to_find = 144512
index = 144512 - 100
"""