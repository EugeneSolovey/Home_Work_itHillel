import random
import sys

import quicksort as qs

# import random, sys, re, time


if __name__ == "__main__":
    a = [1,5,3,-2,0]
    print("module: ", qs)
    print("A: ", qs.quicksort(a))
    #for p in sys.path:
    #print(*sys.path, sep="\n")

    from quicksort import *
    from sys import *
    print(rlist)

    # qs.rlist
    # sys.rlist


"""
print(dir())
print(dir(quicksort))

print(__file__)
print(quicksort.__file__)

print(__name__, quicksort.__name__)
"""

"""
import quicksort
import quicksort as qs
from quicksort import quicksort
from quicksort import quicksort as quicksort_function

from quicksort import *
"""

import quicksort
print(type(quicksort))
from quicksort import quicksort, rlist
print(type(quicksort))

print(quicksort(a))

print('rlist', rlist)
