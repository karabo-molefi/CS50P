import sys
lines =[]

def main():
    file_name = cmd_arg()
    if python_file(file_name):
        ans = get_lines(file_name)
    else:
        sys.exit("Not a Python file")

    ans = count(ans)

    print(ans)

def cmd_arg():
    arg = sys.argv
    if len(arg) < 2:
        sys.exit("Too few command-line arguments")
    if len(arg) > 2:
        sys.exit("Too many command-line arguments")
    else:
        return arg[1]

def python_file(f):
    return f.endswith(".py")

def get_lines(f):
    try:
        file = open(f)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        for line in file:
            lines.append(line)
    return lines

new_lines = []
def count(l):
    for line in l:
        line = line.strip()
        if line.lstrip() == "":
            continue
        elif line.startswith("#"):
            continue
        else:
            new_lines.append(line)
    return len(new_lines)


if __name__ == "__main__":
    main()