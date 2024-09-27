list = {}

#get user input
#put all user's input into the dict with a value
try:
    while True:
        item = input("").strip().upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

except EOFError:
    sorted_list = sorted(list)

    for item in sorted_list:
        print(list[item], item)
