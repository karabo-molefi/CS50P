import csv
import sys
from tabulate import tabulate

table =[]

def main():
    file_name = cmd_arg()
    if csv_file(file_name):
        table = make_table(file_name)
    else:
        sys.exit("Not a CSV file")

    print(tabulate(table, headers="keys", tablefmt="grid"))

def make_table(f):
    try:
        file = open(f)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)
    return table

def cmd_arg():
    arg = sys.argv
    if len(arg) < 2:
        sys.exit("Too few command-line arguments")
    if len(arg) > 2:
        sys.exit("Too many command-line arguments")
    else:
        return arg[1]

def csv_file(f):
    return f.endswith(".csv")

if __name__ == "__main__":
    main()