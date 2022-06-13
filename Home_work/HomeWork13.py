translations = {
   'apple': ['malum', 'pomum', 'popula'],
   'fruit': ['baca', 'bacca', 'popum'],
   'punishment': ['malum', 'multa']
}

some_dict = {' '.join(value): key for key, value in translations.items()}

print(some_dict)


input()