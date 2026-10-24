from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    today = date.today()
    birthday = input("Date: ")
    birthday = get_bday(birthday)
    print(get_time(today, birthday))

def get_time(now, then):
    time = abs(now - then)
    t = time.days
    t = int(t) * 24 * 60
    words = p.number_to_words(t, andword="")
    return f"{words.capitalize()} minutes"


def get_bday(b):
    try:
        birthday = date.fromisoformat(b)
    except:
        sys.exit("Invalid date")
    else:
        return birthday



if __name__ == "__main__":
    main()