# Plan
1. Quick sort
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

2. Modules
    1. Rationale: simplicity, maintainability, reusability and scoping
    2. syntax - `import`, `from`, `as`, `*`
    3. ImportError
    4. `dir()` - local symbol table
    5. `sys.path`
    6. `if __name__ == "__main__":`
3. Packages - for the next lesson
    1. `__init__.py`
    2. relative/absolute imports
