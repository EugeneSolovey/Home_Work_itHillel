string = input('Enter text: ')

count = string.count(".")

if not string.endswith("."):
    count += 1

print('Number of sentences in the text:', count)