s = "Pythonist 2"

for char in s:
    if char.isupper():
        print(char.lower(), end="")
    else:
        print(char.upper(), end="")