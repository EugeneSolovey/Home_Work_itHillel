text = input('Please, write your text: ')
words_count = dict()

words = text.split()
for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1

print(words_count)
print('TOP 5: ', end='')
for key, value in sorted(words_count.items(), key=lambda para: -para[1])[:5]:
    print(key, '-', value, end=' ')
print()
for key, value in words_count.items():
    print(key, '-', value)

