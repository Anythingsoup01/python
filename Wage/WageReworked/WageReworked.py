def checkvar(var, against = 1, by = 1):
    if "exit" in var: quit()
    else: 
        var = var or 0
        return round(float(var) / against * by, 2)
        
base_wage = checkvar(input("Enter your hourly rate: $"))
overtime_wage = round(float(base_wage) * 1.5, 2)
shift_bonus = checkvar(input("Enter shift bonus \"if applicable\": %"), 100, base_wage)
total_tax_deduction = checkvar(input("What percentage of your income is taxed? %"), 100)

while True:
    weeksofwork = int(checkvar(input("\nWeeks / Pay period: ")))
    total = {'wage' : 0, 'shift_bonus' : 0, 'overtime' : 0, 'nonstandard' : 0, 'gross' : 0, 'net' : 0, 'taxes' : 0}
    
    for week in range(1, weeksofwork + 1):
        if weeksofwork > 4: print("I'm sorry, to get a more reliable number, please stay within the limit of 1-4")
        else:
            week_hours = checkvar(input(f"\n\nHow many hours did you work for Week {week}? "))
            week_nonstandard = checkvar(input("Any sick, holiday or vacation time?: "))
            if week_hours >= 40:
                week_wage = round(base_wage * 40, 2)
                week_shift_bonus = round(shift_bonus * (week_hours + week_nonstandard), 2)
                week_overtime = round(week_hours - 40, 2)
                week_overtime = round(week_overtime * overtime_wage, 2)
            else :
                week_wage = round(base_wage * week_hours, 2)
                week_shift_bonus = round(shift_bonus * week_hours, 2)
                week_overtime = 0
            week_nonstandard = round(week_nonstandard * base_wage, 2)
            week_gross = round(week_wage + week_shift_bonus + week_overtime + week_nonstandard, 2)
            week_net = round(week_gross * (1.0 - total_tax_deduction), 2)
            week_taxes = round(week_gross - week_net, 2)
        
        total['wage'] += round(week_wage, 2)
        total['shift_bonus'] += round(week_shift_bonus, 2)
        total['overtime'] += round(week_overtime, 2)
        total['nonstandard'] += round(week_nonstandard, 2)
        total['gross'] += round(week_gross, 2)
        total['net'] += round(week_net, 2)
        total['taxes'] += round(week_taxes, 2)
        
        print(f"\nBase Pay: ${week_wage:,}\nShift Pay: ${week_shift_bonus:,}\nOvertime: ${week_overtime:,}\nNonstandard Pay: ${week_nonstandard:,}\nGross Pay: ${week_gross:,}\nNet Pay: ${week_net:,}\nTaxes and deductibles: ${week_taxes:,}")
    print(f"\nBase Pay: ${total['wage']:,}\nShift Pay: ${total['shift_bonus']:,}\nOvertime: ${total['overtime']:,}\nNonstandard Pay: ${total['nonstandard']:,}\nGross Pay: ${total['gross']:,}\nNet Pay: ${total['net']:,}\nTaxes and deductibles: ${total['taxes']:,}")
    pay_period_to_salary = round(52 / weeksofwork)
    while True:
        check_salary = input("Would you like to check your salary? Y/n\n")
        if "y" in check_salary.lower():
            total['wage']  = round(total['wage']  * pay_period_to_salary, 2)
            total['shift_bonus'] = round(total['shift_bonus'] * pay_period_to_salary, 2)
            total['overtime'] = round(total['overtime'] * pay_period_to_salary, 2)
            total['nonstandard'] = round(total['nonstandard'] * pay_period_to_salary, 2)
            total['gross'] = round(total['gross'] * pay_period_to_salary, 2)
            total['net'] = round(total['net'] * pay_period_to_salary, 2)
            total['taxes'] = round(total['taxes'] * pay_period_to_salary, 2)
            print(f"\nBase Pay: ${total['wage']:,}\nShift Pay: ${total['shift_bonus']:,}\nOvertime: ${total['overtime']:,}\nNonstandard Pay: ${total['nonstandard']:,}\nGross Pay: ${total['gross']:,}\nNet Pay: ${total['net']:,}\nTaxes and deductibles: ${total['taxes']:,}")
            break
        else:
            break
            