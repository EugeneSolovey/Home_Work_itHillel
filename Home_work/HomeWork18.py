file = open('HomeWork.txt', mode='w')

while True:
    line = input()
    if line == '':
        break
    file.write(line+'\n')

file.close()
