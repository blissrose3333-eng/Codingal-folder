import string
ch = input("Enter a character: ")
if ch in string.ascii_letters:
    print(f"The character {ch} is an alphabet.")
else:
    print(f"The character {ch} is not an alphabet.")
