file = open('HomeWork.txt', mode='w+', encoding='utf-8')

while True:
    line = input()
    if line == '':
        break
    file.write(line+'\n')

file.close()
