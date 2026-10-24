import sys
import csv

details=[]

def main():
    before, after = cmd_arg()
    before = convert(before)
    after = write(after)

def cmd_arg():
    arg = sys.argv
    if len(arg) < 3:
        sys.exit("Too few command-line arguments")
    if len(arg) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return list((arg[1], arg[2]))

def convert(f):
    try:
        file = open(f)
    except IOError:
        sys.exit(f"could not read {f}")
    else:
        reader = csv.reader(file)
        for name, house in reader:
            name = name.rstrip().split(", ")
            first = name[-1]
            last = name[0]
            details.append(list((first, last, house)))
    return details

def write(a):
    details.pop(0)
    with open(a, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for d in details:
            writer.writerow({"first": d[0], "last": d[1], "house": d[2]})

if __name__ == "__main__":
    main()