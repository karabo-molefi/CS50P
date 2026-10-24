import emoji

code = input("Input: ")
emojis = emoji.emojize(code, language='alias')
print(f"Output: {emojis}")