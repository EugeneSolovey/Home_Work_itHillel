# Plan
1. Bubble sort
    ```
    def bubble_sort(array):
        n = len(array)

        for i in range(n):
            already_sorted = True
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    already_sorted = False
            if already_sorted:
                break

        return array
    ```
2. Insertion sort
    ```
    def insertion_sort(array):
        for i in range(1, len(array)):
            key_item = array[i]
            j = i - 1
            while j >= 0 and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key_item
        return array
    ```
3. Recursion
4. Quick sort - to the next lesson
    ```
    def quicksort(array):
        if len(array) < 2:
            return array

        low = []
        same = []
        high = []
        pivot = array[0]
        for item in array:
            if item < pivot:
                low.append(item)
            elif item > pivot:
                high.append(item)
            else:
                same.append(item)
        return quicksort(low) + same + quicksort(high)
    ```
