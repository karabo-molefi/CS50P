months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # prompt user for a date
    date = input("Date: ").strip()

    # if date is numeric format
    if "/" in date:
        # do this
        try:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        # check if month is not greater than 12 and day is not greater than 31
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        except ValueError:
            pass
    # if date is word format
    elif "," in date:
        # do this
        try:
            month_day, year2 = date.split(",")
            month2, day2 = month_day.split(" ")
        # convert str to int
            year2 = int(year2)
            day2 = int(day2)
            month2 = months.index(month2) + 1 # get the index of month3 in months list and add 1
        # check if month3 is not greater than 12 and day2 is not greater than 31
            if month2 <= 12 and day2 <= 31:
                print(f"{year2}-{month2:02}-{day2:02}")
                break
            else:
                continue
        except ValueError:
            pass
        # END OF ELIF
    else:
        continue


exit()
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # prompt user for a date
    date = input("Date: ").strip()

    # if date is numeric format
    if "/" in date:
        # do this
        try:
            month, day, year = date.split("/")
        except ValueError:
            pass
        # convert str to int
        try:
            month = int(month)
        except ValueError:
            pass

        try:
            day = int(day)
        except ValueError:
            pass
        try:
            year = int(year)
        except ValueError:
            pass

        # check if month is not greater than 12 and day is not greater than 31
        if month <= 12 and day <= 31:
            print(f"{year}-{month:02}-{day:02}")
            break
        else:
            continue
    # if date is word format
    elif "," in date:
        # do this
        try:
            month_day, year2 = date.split(",")
        except ValueError:
            pass

        try:
            month2, day2 = month_day.split(" ")
        except ValueError:
            pass
        # convert str to int
        try:
            year2 = int(year2)
        except ValueError:
            pass
        try:
            day2 = int(day2)
        except ValueError:
            pass

        try:
            month2 = months.index(month2) + 1 # get the index of month3 in months list and add 1
        except ValueError:
            pass
        # check if month3 is not greater than 12 and day2 is not greater than 31
        if month2 <= 12 and day2 <= 31:
            print(f"{year2}-{month2:02}-{day2:02}")
            break
        else:
            continue
        # END OF ELIF
    else:
        continue


exit()
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:

    # prompt user for input
    date = input("Date: ").strip()

    # evaluate the format that they entered the date (word or numeric)
    for char in date:
        # check if the first character is alphabetiacal
        if char.isalpha():
            # split the first string at the comma
            try:
                month_day, word_year = date.split(',')
            except ValueError:
                pass

            # split the second string at the space
            try:
                word_month, word_day = month_day.split(' ')
            except ValueError:
                pass
            # convert word_day to an int so it cann be formatted with a leading zero
            try:
                word_day = int(word_day)
            except ValueError:
                pass
            # evaluate if word_day is greater than 1 equal to or less than 31
            if 1 < word_day < 32:

            # covert word_year to int
                try:
                    word_year = int(word_year)
                except ValueError:
                    pass
                # get index for the inputted month in months list and add 1
                num_month = months.index(word_month) + 1

                print(f"{word_year}-{num_month:02}-{word_day:02}")
                break


        else: # if its not the month format check if its the numeric format
            try:
                month, day, year = date.split('/')
            except ValueError:
                pass

            try:
                year = int(year)
                month = int(month)
                day = int(day)

            except ValueError:
                pass


            print(f"{year}-{month:02}-{day:02}")
            break
    break