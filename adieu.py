#import and activate inflect
import inflect
p = inflect.engine()

#create a list
names = []

while True:
    try:
        add = input("Name: ")
        names.append(add)

    except EOFError:
        print()
        break

output = p.join(names)
print( "Adieu, adieu, to " + output)
