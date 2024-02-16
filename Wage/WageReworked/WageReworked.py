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
    weeksofwork = checkvar(input("\nPay Period Schedule: "))
    
    total_wage = 0
    total_shift_bonus = 0
    total_overtime = 0
    total_nonstandard = 0
    total_gross = 0
    total_net = 0
    total_taxes = 0
    
    for week in range(1, int(weeksofwork) + 1):
        if weeksofwork > 4: print("I'm sorry, to get a more reliable number, please stay within the limit of 1-4")
        else:
            week_hours = checkvar(input(f"\n\nHow many hours did you work for Week {week}? "))
        
            if week_hours >= 40:
                week_wage = round(base_wage * 40, 2)
                week_shift_bonus = round(shift_bonus * week_hours, 2)
                week_overtime = round(week_hours - 40, 2)
                week_overtime = round(week_overtime * overtime_wage, 2)
            else :
                week_wage = round(base_wage * week_hours, 2)
                week_shift_bonus = round(shift_bonus * week_hours, 2)
                week_overtime = 0
            week_nonstandard = round(checkvar(input("Any sick, holiday or vacation time?: ")) * base_wage, 2)
            week_gross = round(week_wage + week_shift_bonus + week_overtime + week_nonstandard, 2)
            week_net = round(week_gross * (1.0 - total_tax_deduction), 2)
            week_taxes = round(week_gross - week_net, 2)
        
        total_wage += week_wage
        total_shift_bonus += week_shift_bonus
        total_overtime += week_overtime
        total_nonstandard += week_nonstandard
        total_gross += week_gross
        total_net += week_net
        total_taxes += week_taxes
        
        print(f"\nBase Pay: ${week_wage:,}\nShift Pay: ${week_shift_bonus:,}\nOvertime: ${week_overtime:,}\nNonstandard Pay: ${week_nonstandard:,}\nGross Pay: ${week_gross:,}\nNet Pay: ${week_net:,}\nTaxes and deductibles: ${week_taxes:,}")
    print(f"\nBase Pay: ${total_wage:,}\nShift Pay: ${total_shift_bonus:,}\nOvertime: ${total_overtime:,}\nNonstandard Pay: ${total_nonstandard:,}\nGross Pay: ${total_gross:,}\nNet Pay: ${total_net:,}\nTaxes and deductibles: ${total_taxes:,}")
    pay_period_to_salary = round(52 / weeksofwork)
    ask_to_check_salary = True
    while ask_to_check_salary:
        check_salary = input("Would you like to check your salary? Y/n")
        if "y" in check_salary.lower():
            total_wage = total_wage * pay_period_to_salary
            total_shift_bonus = total_shift_bonus * pay_period_to_salary
            total_overtime = total_overtime * pay_period_to_salary
            total_nonstandard = total_nonstandard * pay_period_to_salary
            total_gross = total_gross * pay_period_to_salary
            total_net = total_net * pay_period_to_salary
            total_taxes = total_taxes * pay_period_to_salary
            print(f"\nBase Pay: ${total_wage:,}\nShift Pay: ${total_shift_bonus:,}\nOvertime: ${total_overtime:,}\nNonstandard Pay: ${total_nonstandard:,}\nGross Pay: ${total_gross:,}\nNet Pay: ${total_net:,}\nTaxes and deductibles: ${total_taxes:,}")
        else:
            ask_to_check_salary = False    
            