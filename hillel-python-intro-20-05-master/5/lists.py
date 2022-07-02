"""
Collections:
str ""
list []
tuple (,)
set {,}
dict {1:2}
"""

a = 3
b = 5
c = 10

some_list = []
some_list = list()

some_list = [1, 2, 3, "hello", True, None, 3.0, print, ["nested_list", ]]

x = 5
some_list = [5, 1, 2, 3, 4]
# list pros (преимущества)
# ([-1],[5],[1],[2],[3],[4],[10],[100])
# 1. Fast indexing
# 2. Ordered

# list cons (минусы)
# 1. is_present = 5 in some_list
# 2. slow insertions in the middle or beginning
 
for value in some_list:
    print("value in list: ", value)

# Indexing
s = "hello world"
s[4]
s[0]

l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1 + l2
print("l1 id: ", id(l1))
print("l2 id: ", id(l2))
print("l3 id: ", id(l3))
print(l3)

l4 = l3 * 2
print("l3 id: ", id(l3))
print("l4 id: ", id(l4))
print(l4)

# List functions
l1 = [1,2,3]
l2 = [4,5,6]
print(max(l1), min(l1))
print(max(l1[0], l1[1]))
print(max([], default="no max value"))
# print(max([]))

print(max("Peter Johnson", "Alex Zetman", key=lambda s: s.split()[-1]))
print("Alex Zetman".split())

print(sum(l1), 1)
print(sum(l1 + l2))

some_list = [5, 1, 2, 3, 4]

# sorted
sorted_list = sorted(some_list)
print("some_list id: ", id(some_list))
print("sorted_list id: ", id(sorted_list))
print(sorted_list, some_list, sorted(some_list, reverse=True))

# reversed
reversed_iter = reversed(some_list)
print(next(reversed_iter), next(reversed_iter), some_list, some_list[::-1])
print(list(reversed(some_list)) == some_list[::-1])

# methods
some_list = [5, 1, 2, 3, 4]

# mutable
print(id(some_list))
some_list[0] = 50
print(id(some_list), some_list)

del some_list[0]
print(some_list)

# insertions
some_list.append(100)
print(id(some_list), some_list)
some_list.insert(0, "inserted")
print(id(some_list), some_list)

# extend
l1 = [1,2,3]
l2 = [4,5,6]
print(id(l1))
l1.extend(l2)
print(id(l1), l1, l2)

l2.extend(l1)
print(l2)

value = l2.pop(0)
print(value, l2)

l2.clear()
print(l2)

l2_copy = l2.copy()
l2_copy = l2[:]
print(id(l2), id(l2_copy), l2, l2_copy)

import copy

l = [1, 2, ["something"]]
new_l = l.copy()
print(l, new_l)
print(id(l), id(new_l))
print(id(l[-1]), id(new_l[-1]))
l[-1].append(" happened!")
print(l, new_l)

# quicksort
l = [4,6,2,123,261,3,4123,13123]
print(id(l), l)
l.sort(reverse=True)
print(id(l), l)

["Ivan Ivanenko", "Misha Zygar", ].sort()
