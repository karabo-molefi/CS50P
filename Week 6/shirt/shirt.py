import os
import sys
from PIL import Image, ImageOps

shirt = Image.open("shirt.png")
size = shirt.size

def main():
    if valid():
        before = sys.argv[1]
        after = sys.argv[2]
        edit(before, after)

def edit(b,a):
    with Image.open(b) as im:
        im = ImageOps.fit(im, size)
        im.paste(shirt, shirt)
        im.save(a)

def valid():
    arg1, arg2 = cmd_arg()
    if exists(arg1):
        if extension(arg1, arg2):
            return True
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit()

def cmd_arg():
    arg = sys.argv
    if len(arg) < 3:
        sys.exit("Too few command-line arguments")
    if len(arg) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return list((arg[1], arg[2]))

def exists(i):
    return os.path.isfile(i)

def extension(a, b):
    path = os.path.splitext(a)
    path2 = os.path.splitext(b)
    return path[1] == path2[1]


if __name__ == "__main__":
    main()