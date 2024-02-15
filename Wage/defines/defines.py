def round2M(wage, hours):
    return(round(wage * hours,2))
def round2A(wage1, wage2):
    return(round(wage1 + wage2,2))
def round3A(wage1, wage2, wage3):
    return(round(wage1 +wage2 +wage3,2))
def round4A(num1, num2, num3, num4):
    return(round(num1 +num2 +num3 +num4, 2))

def checkfloat(floatvar, by):
    if floatvar.lower() == "exit":
        quit()
    else:
        floatvar = floatvar or 0
        floatvar = float(floatvar)
        return round2M(floatvar, by)

def checkint(integer):
    if integer.lower() == "exit":
        quit()
    else:
        integer = integer or 0
        return int(integer)


