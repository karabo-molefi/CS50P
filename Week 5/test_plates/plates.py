def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if first_two_alpha(s) and \
    length(s) and \
    first_not_zero(s) and \
    number_at_end(s) and \
    check_punctuation(s):
        return True
    else:
        return False

def first_two_alpha(n):
    if n[0:2].isalpha():
        return True

def length(n):
    if 2 <=  len(n) <= 6:
        return True

def first_not_zero(n):
    for char in n:
        if char.isdigit():
            break

    if char != "0":
        return True

def number_at_end(num):
    if num.isalpha():
        return True
    else:
        first_digit = None
        for i in num:
            if i.isdigit():
                first_digit = i
                break

        _, end = num.split(first_digit, 1)

        for j in end:
            if j.isalpha():
                return False
    return True


def check_punctuation(p):
    for char in p:
        if char.lower() not in ["a", "b", "c", "d", "e", "f", "g", "h",
                            "i", "j", "k", "l", "m", "n", "o", "p",
                            "q", "r", "s", "t", "u", "v", "w", "x",
                            "y", "z", "0", "1", "2", "3", "4", "5",
                            "6", "7", "8", "9"]:
            return False
    return True


if __name__ == "__main__":
    main()