translations = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}

for key, value in translations.items():
    if type(value) == list:
        translations[key] = ' '.join(value)

some_dict = {y : x for x, y in translations.items()}




print(some_dict)


input()