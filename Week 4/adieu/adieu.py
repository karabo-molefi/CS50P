import inflect
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break
print()
print("Adieu, adieu, to ", end="")

if len(names) == 1:
    for n in names:
        print(n)
else:
    names = p.join(names)
    print(names)