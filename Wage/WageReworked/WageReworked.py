from core.core import *
        
base_wage = checkvar(input("Enter your hourly rate: $"))
overtime_wage = round(float(base_wage) * 1.5, 2)
shift_bonus = checkvar(input("Enter shift bonus \"if applicable\": %"), 100, base_wage)

four_01k = input("Do you have a 401k? If so please add the $Amount or %Amount: ($)")
is_percent_amount = checkbool(four_01k)
four_01k = checkvar(four_01k)

health_insurance = int(checkvar(input("How many health insurances do you pay for? ")))

total_health_insurance = 0

for insurances in range(1, health_insurance + 1):
    insurance = checkvar(input(f"How much do you pay for insurance {insurances}: $"))
    total_health_insurance += insurance

state_income_tax = .0305
local_income_tax = .025

ssi_income_rate = .062
medicare_rate = .0145



while True:

    weeksofwork = int(checkvar(input("\nWeeks / Pay period: ")))
    total = {'wage' : 0, 'shift_bonus' : 0, 'overtime' : 0, 'nonstandard' : 0, 'federal_taxes' : 0, 'state_taxes' : 0, 'local_taxes' : 0, 'ssi_rate' : 0, 'medicare_rate' : 0, 'taxes' : 0,'401k' : 0, 'gross' : 0, 'net' : 0}
    
    for week in range(1, weeksofwork + 1) :
        if weeksofwork > 4: 
            print("I'm sorry, to get a more reliable number, please stay within the limit of 1-4")
            break
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
            week_401k = round(calculate_401k(week_gross, four_01k, is_percent_amount), 2)
            
            week_taxable_gross_pay = round(week_gross - ((week_401k / weeksofwork) + (total_health_insurance / weeksofwork)), 2)
            federal_income_tax = round(calculate_federal(week_taxable_gross_pay), 2)
            total_tax_deduction = round(federal_income_tax + state_income_tax + local_income_tax + ssi_income_rate + medicare_rate, 4) 

            week_net = round(week_taxable_gross_pay * (1.0 - total_tax_deduction), 2)

            week_federal_taxes = round(federal_income_tax * week_taxable_gross_pay, 2)
            week_state_taxes = round(state_income_tax * week_taxable_gross_pay, 2)
            week_local_taxes = round(local_income_tax * week_taxable_gross_pay, 2)
            week_ssi_rate = round(ssi_income_rate * week_taxable_gross_pay, 2)
            week_medicare_rate = round(medicare_rate * week_taxable_gross_pay, 2)

            week_taxes = round(week_taxable_gross_pay - week_net, 2)

        total['wage'] += round(week_wage, 2)
        total['shift_bonus'] += round(week_shift_bonus, 2)
        total['overtime'] += round(week_overtime, 2)
        total['nonstandard'] += round(week_nonstandard, 2)
        total['federal_taxes'] += round(week_federal_taxes, 2)
        total['state_taxes'] += round(week_state_taxes, 2)
        total['local_taxes'] += round(week_local_taxes, 2)
        total['ssi_rate'] += round(week_ssi_rate, 2)
        total['medicare_rate'] += round(week_medicare_rate, 2)
        total['taxes'] += round(week_taxes, 2)
        total['401k'] += round(week_401k, 2)
        total['gross'] += round(week_gross, 2)
        total['net'] += round(week_net, 2)
      
        print(f"\nBase Pay: ${week_wage:,}\nShift Pay: ${week_shift_bonus:,}\nOvertime: ${week_overtime:,}\nNonstandard Pay: ${week_nonstandard:,}\nTotal Taxes: ${week_taxes:,}\n401k: ${week_401k}\nGross Pay: ${week_gross:,}\nNet Pay: ${week_net:,}")
    print(f"\nBase Pay: ${total['wage']:,}\nShift Pay: ${total['shift_bonus']:,}\nOvertime: ${total['overtime']:,}\nNonstandard Pay: ${total['nonstandard']:,}\nTotal Taxes: ${total['taxes']:,}\n401k: ${total['401k']}\nTotal Health Coverage: ${total_health_insurance:,}\nGross Pay: ${total['gross']:,}\nNet Pay: ${total['net']:,}")
    
    while True:
        paycheck_in_year = round (52 / weeksofwork)
        opt = input("What would you like to do? (Exit) (Details) (Salary)")
        if "exit" in opt.lower():
            break
        elif "details" in opt.lower():
            print(f"\nFederal Taxes: ${total['federal_taxes']:,}\nState Taxes: ${total['state_taxes']:,}\nLocal Taxes: ${total['local_taxes']:,}\nSocial Security: ${total['ssi_rate']:,}\nMedicare: ${total['medicare_rate']:,}\nTotal Taxes: ${total['taxes']:,}")
        elif "salary" in opt.lower() :
            print(f"\nBase Pay: ${total['wage'] * paycheck_in_year:,}\nShift Pay: ${total['shift_bonus'] * paycheck_in_year:,}\nOvertime: ${total['overtime'] * paycheck_in_year:,}\nNonstandard Pay: ${total['nonstandard'] * paycheck_in_year:,}\nTotal Taxes: ${total['taxes'] * paycheck_in_year:,}\nTotal 401k: ${total['401k'] * paycheck_in_year}\nTotal Health Coverage: ${total_health_insurance * paycheck_in_year:,}\nGross Pay: ${total['gross'] * paycheck_in_year:,}\nNet Pay: ${total['net'] * paycheck_in_year:,}")