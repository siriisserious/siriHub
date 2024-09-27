letters = input("Input: ")

print("Out put: ", end="")
for letter in letters:
    if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        print(letter.strip(letter), end="")
    else:
        print(letter, end="")

print()
