# main function
def main():
    # prompt user for input
    userInput = input("Enter input: ")
    # calls covert on input
    userInput = convert(userInput)
    # prints the result
    print(userInput)

# implement function called convert
def convert(strInput):
    ans = strInput.replace(":)","🙂").replace(":(","🙁")
    return ans

# call main
main()