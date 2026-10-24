import re
import sys


def main():
    print(convert(input("Hours: ")))


#def get_matches(s):
    #return re.search(r"^((([1-9]:[0-5][0-9]\s(AM|PM))|(1[0-2]:[0-5][0-9]\sAM)|(1[0-1]:[0-5][0-9]\sPM))|(((10|11|12)|[0-9])\s(AM|PM)))\sto\s((([1-9]:[0-5][0-9]\s(AM|PM))|(1[0-2]:[0-5][0-9]\sAM)|(1[0-1]:[0-5][0-9]\sPM))|(((10|11|12)|[0-9])\s(AM|PM)))$",s, re.IGNORECASE)

def convert(s):
    matches = re.search(r"^(1[0-2]|[0-9]):[0-5][0-9]\s(AM|PM)\sto\s(1[0-2]|[0-9]):[0-5][0-9]\s(AM|PM)$", s) or \
        re.search(r"^(1[0-2]|[0-9])\s(AM|PM)\sto\s(1[0-2]|[0-9])\s(AM|PM)$",s)
    if matches:
        if re.search(":", s):
            return process1(s)
        else:
            return process2(s)
    else:
        raise ValueError

def process1(s):
    new = []
    times = s.split(" to ")

    for time in times:
        if re.search("AM", time):
            time = time.replace(" AM","")
            hours, min = time.split(":")
            if int(hours) < 10:
                hours = "0" + hours
            elif int(hours) == 12:
                hours = "00"
            new.append(f"{hours}:{min}")
        else:
            time = time.replace(" PM","")
            hours, min = time.split(":")
            if int(hours) <= 10:
                hours = 12 + int(hours)
                hours = str(hours)
            elif int(hours) == 12:
                hours = "12"
            new.append(f"{hours}:{min}")

    return f"{new[0]} to {new[1]}"

def process2(s):
    new = []

    times = s.split(" to ")

    for time in times:
        if re.search("AM", time):
            time = time.replace(" AM", "")
            if int(time) < 10:
                time = "0" + time + ":00"
            elif int(time) == 12:
                time = "00:00"
            else:
                time = time + ":00"
            new.append(time)
        else:
            time = time.replace(" PM", "")
            if int(time) != 12:
                time = 12 + int(time)
                time = str(time) + ":00"
            else:
                time = "12:00"
            new.append(time)

    return f"{new[0]} to {new[1]}"


if __name__ == "__main__":
    main()