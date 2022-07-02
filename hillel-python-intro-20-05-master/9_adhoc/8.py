# Print Nth char of string if present

s = input("Enter a string: ")
n = int(input("Enter N: "))

char = s[n] if n < len(s) else "not found" 
print(str(n) + "th index of string is:", char)