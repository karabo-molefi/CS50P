""" """ # ask user for answer
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if check_answer(answer):
        print("Yes")
    else:
        print("No")
# check if answer is correct or not

def check_answer(a):
    if a == "42":
        return True
    elif a == "forty-two":
        return True
    elif a == "forty two":
        return True
    else:
        return False


main()

""" answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()

if answer == "42":
    print("Yes")
elif answer == "forty two":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
else:
    print("No") """
