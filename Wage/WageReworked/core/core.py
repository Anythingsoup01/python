def checkvar(var, against = 1, by = 1):
    if "exit" in var: quit()
    elif "%" in var:
        return round(float(var.replace("%", "")), 2)
    else: 
        var = var or 0
        return round(float(var) / against * by, 2)
    
def checkbool(string):
    if "%" in string:
        return True
    else : return False

def calculate_federal(gross_pay):
    if gross_pay <= 11600: return .1
    if gross_pay <= 47150: return .12
    if gross_pay <= 100525: return .22
    
def calculate_401k(gross_pay, four01k, is_percent):
    if is_percent:
        return round(gross_pay * (four01k/100), 2)
    else:
        return four01k
