# Divide and qonquer (Разделяй и властвуй)
import random


#O(n log n)
"""
64, 75, 88, 95, 9, 63, 93, 67, 76, 84

pivot = 64
quicksort([9, 63]) + [64] + quicksort([75, 88, 95, 93, 67, 76, 84])
= [9, 63, 67, 75, 76, 84, 88, 93, 95]

# [9, 63]
1. pivot = 9
   quicksort([]) + quicksort([9]) + quicksort([63]) = [9, 63]

# [75, 88, 95, 93, 67, 76, 84]
2. pivot = 75
   quicksort([67]) + [75] + quicksort([88, 95, 93, 76, 84]) = [67, 75, 76, 84, 88, 93, 95]

# [88, 95, 93, 76, 84]
2.1 pivot = 88
    quicksort([76, 84]) + [88] + quicksort([95, 93]) = [76, 84, 88, 93, 95]

# [76, 84]
2.1.1  pivot = 76
        quicksort([]) + quicksort([76]) + quicksort([84]) = [76, 84]

# [95, 93]
2.1.2  pivot = 95
       quicksort([93]) + quicksort([95]) + quicksort([]) = [93, 95]


"""

rlist = [random.randint(0, 100) for i in range(15)]


def quicksort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array

    less_than, equal, greater_than = [], [], []
    pivot = array[0]  # random.choice(array)
    for item in array:
        if item < pivot:
            less_than.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            greater_than.append(item)

    return quicksort(less_than) + equal + quicksort(greater_than)


if __name__ == "__main__":
    print(rlist)
    print(quicksort(rlist))
    print()

    print(__name__)
