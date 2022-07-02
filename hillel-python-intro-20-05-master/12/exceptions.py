# 3 keywords to exit function: return, yield, (await) and raise

import sys


def index(sequence, item) -> int:
    """
    Return index of item in sequence.
    If item is not in sequence, raise ValueError.
    """
    for i, element in enumerate(sequence):
        if element == item:
            return i
    else:
        # pythonic approach
        # raise ValueError
        raise ValueError(f"{item} is not in sequence")

        # Go approach
        # return -1, "{item} is not in sequence"



text = "today is a good day"
try:
    index_of_5 = index(text, "d")
    input("Awaiting...")
    # 3 / 0

except ValueError as e:
    print("Found error:", e)
    index_of_5 = -1
except KeyboardInterrupt as e:
    print("\nBye!")
    raise e
except: # except Exception:
    print('Unknown error occured!')

else:
    print("No error")

finally:
    print("Done!")


print(index_of_5)


"""
def run_app():
    1 / 0
    print('start app')
    input("Waiting")
    sys.exit(1)

try:
    run_app()
except KeyboardInterrupt:
    print("\nBye!")
except SystemExit:
    print("\nUplanned exit... Bye!")
"""

#Exception

"""
try:
    connection = Database("172.0.0.1")
    deduct_money_from_a(100)
    add_money_to_b(100)
except DatabaseConnectionError:
    connection.rollback()
else:
    print("Transaction is done!")
finally:  # Cleanup block
    connection.close()
"""


import os.path


# LBYL - Loop before you leap
if os.path.exists("file.txt"):
    file = open("file.txt")
else:
    print("no such file found")


# Pythonic-way
# EAFP - Easier to ask forgiveness than permission
try:
    file = open("file.txt")
except FileNotFoundError:
    print("no such file found")



dict = {}

if key in dict:
    print(dict[key])
else:
    print("no key")


try:
    print(dict[key])
except KeyError:
    print("no key")
