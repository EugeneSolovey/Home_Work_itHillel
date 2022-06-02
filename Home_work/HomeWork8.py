string = input('Enter text: ')

even = ''
odd = ''

for i in range(len(string)):
    if i == 0 or i % 2 == 0:
        even += string[i]
    if i != 0 and i % 2 == 1:
        odd += string[i]

print("Symbols with even index: ", even)
print("Symbols with odd index: ", odd)
print("The fifth symbol: ", string[4])
print("Up to the tenth symbols: ", string[:10])
print("Last 5 symbols: ", string[-5:])
print("String in reverse order: ", string[::-1])
print("-II- through one symbols: ", string[::-2])
print("String length: ", len(string))

input()
