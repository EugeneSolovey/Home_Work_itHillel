"""
File opening modes:
    r - DEFAULT - read
    w - write
    a - append
    x - exclusive write

    t - DEFAULT - text content
    b - binary content

    + - OPTIONAL - read/write at 1 time
"""

#file = open("dogs.txt", mode="r")

#print(type(file))
#print(file)

# returns list
# lines = file.readlines()
# print(lines)

# iterate by line

# Context manager
with open("dogs.txt", mode="r") as dogs_file, open("result.txt", mode="w") as result_file:
    result_file.writelines(dogs_file)

print("Done")

# file.close()
# result_file.close()
