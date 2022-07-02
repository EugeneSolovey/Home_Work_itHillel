text = input("Enter text: ")

for character in text:
    if character == " ":
        continue
    if character == ".":
        print("Found dot! Break")
        break
    print("Character is: ", character)
print()

number = input("Enter num: ")
for digit in number:
    print(int(digit) ** 2, end=" ")
print()

string = "qwerty"
for i in range(6):
    print(string[i])

for i in range(10):
    if i % 2 != 0:
        continue
    print(i)
