#Promts user for input then convert answer into all lowercase letters
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()
if "42" in answer:
    print("Yes")
elif "forty two" in answer:
    print("Yes")
elif "forty-two" in answer:
    print("Yes")
else:
    print("No")
