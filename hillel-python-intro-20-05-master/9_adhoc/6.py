s = "News from New York City! Nowadays..."

first_space = s.find(" ")
last_space = s.rfind(" ")

news = s[:first_space]
print(news, len(news))

nowadays = s[last_space+1:]
print(nowadays)

middle = s[first_space+1:last_space]
print(middle)

print(news, middle.replace("N", "n"), nowadays)
