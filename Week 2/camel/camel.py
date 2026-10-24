camel_case = input("camelCase: ").strip()

for letter in camel_case:
    if letter.islower():
        print(letter, end="")
    else:
        print("_" + letter.lower(), end="")

print()