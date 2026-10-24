""" # prompt user for a fraction
while True:
    user_input = (input("Fraction: "))

    try:
        numerator, denominator = user_input.split('/')
    except ValueError:
        pass

    try:
        int(numerator), int(denominator)

    except ValueError:
        pass

    try:
        fraction = int(numerator)/int(denominator)
    except ZeroDivisionError:
        pass
    else:
        percentage = fraction * 100
        percentage = round(percentage)

        if percentage <= 1: # if 1% or less output E
            print("E")
        elif percentage >= 99: # if 99% or more output F
            print("F")
        else:
            print(f"{percentage}%")
    break

 """

# prompt user for a fraction
while True:
    user_input = (input("Fraction: "))

    try:
        numerator, denominator = user_input.split('/')
    except ValueError:
        pass
    else:
        try:
            int(numerator), int(denominator)

        except ValueError:
            pass
        else:
            if int(numerator) <= int(denominator):
                try:
                    fraction = int(numerator)/int(denominator)
                except ZeroDivisionError:
                    pass
                else:
                    percentage = fraction * 100
                    percentage = round(percentage)

                    if percentage <= 1: # if 1% or less output E
                        print("E")
                    elif percentage >= 99: # if 99% or more output F
                        print("F")
                    else:
                        print(f"{percentage}%")
                    break