#promts user for input
camel = input("camelCase: ")
split = list(camel)

if camel.islower():
    print(camel)
else:
    print("snake_case: ", end="")
    for letter in camel:
        if letter.islower():
            print(letter, end="")
        elif letter == letter.upper():
            modified = ("_" +letter.lower())
            print(modified, end="")

print()
