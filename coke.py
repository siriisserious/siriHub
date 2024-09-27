due = 50
while due > 0:
    print("Amount Due:", due)
    paid = int(input("Insert coin: "))
    if paid not in [25, 10, 5]:
        continue
    else:
        due = due - paid

print("Change Owed:", due * -1)
