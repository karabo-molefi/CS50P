import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        numbers = matches.groups()
        for n in numbers:
            if int(n) >=0 and int(n) <= 255:
                continue
            else:
                return False
    else:
        sys.exit("False")
    return True


if __name__ == "__main__":
    main()