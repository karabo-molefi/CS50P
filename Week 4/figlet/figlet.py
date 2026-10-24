import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

font = random.choice(figlet.getFonts())

try:
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f" or sys.argv[1] != "--font":
            sys.exit("Invalid use")
        if sys.argv[2] in figlet.getFonts():
                font = sys.argv[2]
        else:
            sys.exit("Invalid use")
    else:
        sys.exit("Invalid use")

except IndexError:
    pass

figlet.setFont(font=font)

s = input("Input: ")
print(f"Output:\n{figlet.renderText(s)}")


exit()
import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

font = random.choice(figlet.getFonts())

try:
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f":
            if sys.argv[1] != "--font":
                sys.exit("Invalid use")
        if sys.argv[2] in figlet.getFonts():
                font = sys.argv[2]
        else:
            sys.exit("Invalid use")
    else:
        sys.exit("Invalid use")

except IndexError:
    pass

figlet.setFont(font=font)

s = input("Input: ")
print(f"Output:\n{figlet.renderText(s)}")