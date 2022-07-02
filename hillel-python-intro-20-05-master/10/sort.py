"""
10 0 57 23 2 1
"""


# bubble sort

"""
10 0 57 23 2 1

iteration ( 0 , 0 ):  [0, 10, 57, 23, 2, 1]
iteration ( 0 , 1 ):  [0, 10, 57, 23, 2, 1]
iteration ( 0 , 2 ):  [0, 10, 23, 57, 2, 1]
iteration ( 0 , 3 ):  [0, 10, 23, 2, 57, 1]
iteration ( 0 , 4 ):  [0, 10, 23, 2, 1, 57]
iteration ( 1 , 0 ):  [0, 10, 23, 2, 1, 57]
iteration ( 1 , 1 ):  [0, 10, 23, 2, 1, 57]
iteration ( 1 , 2 ):  [0, 10, 2, 23, 1, 57]
iteration ( 1 , 3 ):  [0, 10, 2, 1, 23, 57]
iteration ( 2 , 0 ):  [0, 10, 2, 1, 23, 57]
iteration ( 2 , 1 ):  [0, 2, 10, 1, 23, 57]
iteration ( 2 , 2 ):  [0, 2, 1, 10, 23, 57]
iteration ( 3 , 0 ):  [0, 2, 1, 10, 23, 57]
iteration ( 3 , 1 ):  [0, 1, 2, 10, 23, 57]
iteration ( 4 , 0 ):  [0, 1, 2, 10, 23, 57]
"""

a = 5
b = 10

tmp = a
a = b
b = tmp

# swapping vars
a, b = b, a  # tuple([10, 5])
# a = 10, b = 5

x, y = (5, 10)
# x = 5, y = 10

unsorted_array = [10, 0, 57, 23, 1, 2, 5]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        is_sorted = True
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
            print("iteration (", i, ",", j, "): ", array)
        if is_sorted:
            break

bubble_sort(unsorted_array)
print("Sorted by bubble: ", unsorted_array)



"""
10 0 57 23 2 1

1. 0 10 57 23 2 1
2. 0 10 57 23 2 1
3. 0 10 23 57 2 1
4. 0 10 23 2 57 1
5. 0 10 2 23 57 1
6. 0 2 10 23 57 1
5. 0 2 10 23 1 57
5. 0 2 10 1 23 57
5. 0 2 1 10 23 57
5. 0 1 2 10 23 57
"""

unsorted_array = [10, 0, 57, 23, 1, 2, 5]
def insertion_sort(array):
    print('start with unsorted array: ', array)
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            print('inner iteration')
        array[j + 1] = key_item
        print("iteration (", i, "): ", array)

insertion_sort(unsorted_array)
print("Sorted by insertion: ", unsorted_array)

insertion_sort(sorted(unsorted_array, reverse=True))
print("Sorted by insertion: ", unsorted_array)


# recursion

import sys
print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)

counter = 0
def print_counter():
    global counter
    counter += 1
    print(counter)
    print_counter()

# Fails near recursion limit
# print_counter()


def factorial(x: int) -> int:
    factorial_value = 1
    for number in range(1, x+1):
        factorial_value *= number
    return factorial_value

def factorial_recursive(x: int) -> int:
    return 1 if x < 2 else x * factorial_recursive(x-1)

print("Fact", factorial(3))
print("Fact recursive", factorial_recursive(3))
# print("Fact recursive failed: ", factorial_recursive(1000))


def counter_to_zero(x: int):
    print('Enter recursive function with', x)
    if x == 0:
        return
    print(x)
    print('Call to recursive function with', x-1)
    counter_to_zero(x-1)
    print('Exit recursive function with', x)


counter_to_zero(3)
