import random

"""
randrange
randint
random
uniform
"""

for _ in range(15):
    print(random.randrange(0, 2, 1), end=", ")
print()

for _ in range(15):
    print(random.randint(0, 2), end=", ")
print()

for _ in range(15):
    print(round(random.random(), 2), end=", ")
print()

for _ in range(15):
    print(round(random.uniform(0, 1), 2), end=", ")
print()
