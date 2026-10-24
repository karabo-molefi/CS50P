import validators

def main():
    if validators.email(input("What's your email address? ")):
        print("valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()