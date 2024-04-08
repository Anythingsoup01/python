def checkFloat(opt, var, against = 1, by = 1) :
    if "x" in var : quit()
    elif "float" in opt and "%" in var :
        return round(float(var.replace("%", "")) / against, by)
    elif "float" in opt :
        var = var or 0
        return round(float(var) / against * by, 2)
    elif "rate" in opt :
        var = var or 1.5
        return round(float(var) * against, by)

def checkBool(var):
    if var <= 1.0 : return True
    else : return False

def calculateFederal(gross_pay):
    if gross_pay <= 11600: return .1
    if gross_pay <= 47150: return .12
    if gross_pay <= 100525: return .22

while True :

    baseWage = checkFloat("float", input("Hourly Rate: $"))
    overtimeRate = checkFloat("rate", input("Overtime Multiplier (1.5x) :"), baseWage, 4)
    shiftRate = checkFloat("float", input("Shift Rate: %"), 100, baseWage)
    four01K = checkFloat("float", input("401k? ($/%): "), 100)
    isPercent = checkBool(four01K)

    healthInsurance = int(checkFloat("float", input("How many insurances? :")))
    totalHealthInsurance = 0

    for insurances in range(1, healthInsurance + 1):
        insurance = checkFloat("float", input(f"How much do you pay for insurance {insurances}: $"))
        totalHealthInsurance += insurance

    stateIncomeTax = .0305
    localIncomeTax = .025
    ssiIncomeRate = .062
    medicareRate = .0145

    reset = True
    while reset :

        weeksOfWork = int(checkFloat("float", input("\nWeeks / Pay Period: ")))
        total = {'wage' : 0, 'shift_bonus' : 0, 'overtime' : 0, 'nonstandard' : 0, 'federal_taxes' : 0, 'state_taxes' : 0, 'local_taxes' : 0, 'ssi_rate' : 0, 'medicare_rate' : 0, 'taxes' : 0,'401k' : 0, 'gross' : 0, 'net' : 0}

        for week in range(1, weeksOfWork + 1) :

            if weeksOfWork > 4 or weeksOfWork < 0 :

                print("I'm sorry, Please stay within 1-4 Weeks")
                break

            else :

                weekHours = checkFloat("float", input(f"\n\nHow many hours for week {week}: "))
                weekNonstandard = checkFloat("float", input(f"Any PTO? :"))

                if weekHours >= 40:
                    weekWage = round(baseWage * 40, 2)
                    weekOvertime = round(float(weekHours - 40) * overtimeRate, 2)

                else :

                    weekWage = round(baseWage * weekHours, 2)
                    weekOvertime = 0
                weekShiftWage = round(shiftRate * (weekHours + weekNonstandard), 2)
                weekNonstandard = round(weekNonstandard * baseWage, 2)
                weekGross = round(weekWage + weekShiftWage + weekOvertime + weekNonstandard, 2)
                week401K = round(weekGross * four01K, 2)
                weekTaxable = round(weekGross - ((week401K + totalHealthInsurance) / weeksOfWork), 2)

                federalIncomeTax = round(calculateFederal(weekTaxable), 2)
                weekFederalTaxes = round(federalIncomeTax * weekTaxable, 2)
                weekStateTaxes = round(stateIncomeTax * weekTaxable, 2)
                weekLocalTaxes = round(localIncomeTax * weekTaxable, 2)
                weekSsiRate = round(ssiIncomeRate * weekTaxable, 2)
                weekMedicareRate = round(medicareRate * weekTaxable, 2)
                weekTaxes = round(weekFederalTaxes + weekStateTaxes + weekLocalTaxes + weekSsiRate + weekMedicareRate, 2)

                weekNet = round(weekTaxable - weekTaxes, 2)

            total['wage'] += round(weekWage, 2)
            total['shift_bonus'] += round(weekShiftWage, 2)
            total['overtime'] += round(weekOvertime, 2)
            total['nonstandard'] += round(weekNonstandard, 2)
            total['federal_taxes'] += round(weekFederalTaxes, 2)
            total['state_taxes'] += round(weekStateTaxes, 2)
            total['local_taxes'] += round(weekLocalTaxes, 2)
            total['ssi_rate'] += round(weekSsiRate, 2)
            total['medicare_rate'] += round(weekMedicareRate, 2)
            total['taxes'] += round(weekTaxes, 2)
            total['401k'] += round(week401K, 2)
            total['gross'] += round(weekGross, 2)
            total['net'] += round(weekNet, 2)

            print(f"\nBase Pay: ${weekWage:,}\nShift Pay: ${weekShiftWage:,}\nOvertime: ${weekOvertime:,}\nNonstandard Pay: ${weekNonstandard:,}\nTotal Taxes: ${weekTaxes:,}\n401k: ${week401K}\nGross Pay: ${weekGross:,}\nNet Pay: ${weekNet:,}")
        print(f"\nBase Pay: ${round(total['wage'], 2):,}\nShift Pay: ${round(total['shift_bonus'], 2):,}\nOvertime: ${round(total['overtime'], 2):,}\nNonstandard Pay: ${round(total['nonstandard'], 2):,}\nTotal Taxes: ${round(total['taxes'], 2):,}\n401k: ${round(total['401k'], 2)}\nTotal Health Coverage: ${round(totalHealthInsurance, 2):,}\nGross Pay: ${round(total['gross'], 2):,}\nNet Pay: ${round(total['net'], 2):,}")

        while True:
            paycheck_in_year = round (52 / weeksOfWork)
            opt = input("What would you like to do? (Redo) (Reset) (Details) (Salary) (Payments)")
            if "redo" in opt.lower():
                break
            elif "reset" in opt.lower():
                reset = False
                break
            elif "details" in opt.lower():
                print(f"\nFederal Taxes: ${round(total['federal_taxes'], 2):,}\nState Taxes: ${round(total['state_taxes'], 2):,}\nLocal Taxes: ${round(total['local_taxes'], 2):,}\nSocial Security: ${round(total['ssi_rate'], 2):,}\nMedicare: ${round(total['medicare_rate'], 2):,}\nTotal Taxes: ${round(total['taxes'], 2):,}")
            elif "salary" in opt.lower() :
                print(f"\nBase Pay: ${round(total['wage'] * paycheck_in_year, 2):,}\nShift Pay: ${round(total['shift_bonus'] * paycheck_in_year, 2):,}\nOvertime: ${round(total['overtime'] * paycheck_in_year, 2):,}\nNonstandard Pay: ${round(total['nonstandard'] * paycheck_in_year, 2):,}\nTotal Taxes: ${round(total['taxes'] * paycheck_in_year, 2):,}\nTotal 401k: ${round(total['401k'] * paycheck_in_year, 2)}\nTotal Health Coverage: ${round(totalHealthInsurance * paycheck_in_year, 2):,}\nGross Pay: ${round(total['gross'] * paycheck_in_year, 2):,}\nNet Pay: ${round(total['net'] * paycheck_in_year, 2):,}")
            elif "payment" in opt.lower() :
                payment = True
                while payment:
                    number_of_payments = int(checkFloat("float", input("\nHow many payments do you have? ")))
                    if number_of_payments > 0:
                        total_spent = 0
                        for payments in range(1, number_of_payments + 1) :
                            total_spent += checkFloat("float", input(f"\nHow much is your payment {payments}? $"))
                    print(f"\nYou have spent {round(total_spent, 2):,}\nYou will have {round((total['net'] * 2) - total_spent, 2):,}\n\n")
                    break
