# ask user for input
user_input = input("Input: ")

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

print("Output: ",end="")

for letter in user_input:
    if letter in vowels:
        continue
    print(letter, end="")
    
print()