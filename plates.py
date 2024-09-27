def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#----------- no. of lettes and digits counter ------------
def detect(string):
    alphacount, digitcount = 0, 0
    entries = list(string)

    for entry in entries:         #go over every element in the "entries" list
        if entry.isalpha():       #if = letter -> add to count
            alphacount += 1

        elif entry.isdigit():     #if = digit -> add to count
            digitcount += 1
    return alphacount, digitcount  #return the no. of letters & digits

#--------- condition 1,2 : no digits in middle, no zero on first ---------
def no_mid_zero(x):
    alpha, digit = detect(x)
    if x[0:alpha+digit].isalpha():
        return True
    else:
    #number = the first digit of the sequence
        firstdigit = x[alpha:alpha+1]
   #d1_end = from first digit to last char of the sequence
        d1_end = x[alpha:digit+alpha]
        if  d1_end.isdigit() and firstdigit != "0":
            return True
        else:
            return False

#------------ if all conditions cleared ---------------
def is_valid(plate):
    alpha, digit = detect(plate)
    #condition 1,2,       3,:no of alpha ={2,3,4,5,6} & digit < 6      4,:no special chars
    if no_mid_zero(plate) and 2 <= alpha <= 6 and digit < 6 and plate.isalnum():
        return True
    else:
        return False

main()
