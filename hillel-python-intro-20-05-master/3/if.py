# If condition

x = int(input("Enter a number: "))


# Ternary operator (C)
# condition ? true_value : false_value

# Ternary operator (Python)
message = "Even" if x % 2 == 0 else "Odd"
print(message)

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

if x > 0:
    print("Bigger")
elif x == -100:
    print("its -100")
elif x < 0:
    print("Smaller")
else:
    print("Zero")

if x < 0:
    x *= -1
print("Absolute x: ", x)

if x > 10:
    print("Bigger than 10")
elif x > 0:
    print("Bigger than 0")
elif x < 0:
    print("Smaller")
else:
    print("Zero")

print("Done")


# Good - expected flow comes in if, not in else
password = "somepassword"
user_password = input("Enter password: ")
if user_password == password:
    print("Access granted")
else:
    print("Access denied")


# Bad
if user_password != password:
    print("Access denied")
else:
    print("Access granted")