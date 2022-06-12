user_text = input('Enter text: ')
some_dict = {}
some_list = []
for word in user_text.split():
    try:
        some_dict[word] += 1
    except KeyError:
        some_dict[word] = 1

# print(some_dict)

for key, value in some_dict.items():
    some_list.append((value, key))
    some_list.sort(reverse=True)

print('Top 5 most used words in the text:')
for count, word in some_list[0:5]:
    print(word + ' - ' + str(count))

input()
