string = input('Enter text: ')

string1 = string[string.find(" "):string.rfind(" ")]

string1 = string1.replace('n', 'N')

result = string[:string.find(" ")] + string1 + string[string.rfind(" "):]

print(result)

input()