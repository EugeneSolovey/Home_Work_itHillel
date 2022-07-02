print("PyCharm")
print(3)
print(3, 4, "something", 4.25)

password = input("Please give a password: ")
print("Your password: ", password)

# Dynamic typing.
a = 5
print(type(a), id(a))
a = "five"
print(type(a), id(a))

b = a
print(type(b))

# Strong typing.
print(3 == "3")

print(type(3), type(3.5))
print(3 + 3.5)

# Runtime error.
# a = 3 / 0

# Calculator with user input.
x = int(input("Enter a number: "))
result = x ** 2
print("Result: ", result)