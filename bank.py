greet = input("Greeting:")

if "Hello" in greet:
    print("$0")
elif greet.startswith("h") or greet.startswith("H"):
    print("$20")
else:
    print("$100")
