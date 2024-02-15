def roundvars(times = 1, num1 = 0, num2 = 0, num3 = 0, num4 = 0):
    match times:
        case 1: return(round(num1 * num2,2))
        case 2: return(round(num1 + num2,2))
        case 3: return(round(num1 + num2 + num3,2))
        case 4: return(round(num1 + num2 + num3 + num4,2))
        
def checkfloat(floatvar, by):
    
    if floatvar.lower() == "exit":
        quit()
        
    else:
        floatvar = floatvar or 0
        floatvar = float(floatvar)
        return roundvars(1, floatvar, by)

def checkint(integer):
    
    if integer.lower() == "exit":
        quit()
        
    else:
        integer = integer or 0

        return int(integer)
    
base_wage = checkfloat(input("Enter your wage: "), 1)

shift_bonus = checkfloat(input("Enter shift bonus %"), base_wage)
shift_bonus = roundvars(1, shift_bonus, .01)

overtime_wage = base_wage * 1.5

taxes = checkfloat(input("How much is your total tax deductible? %"), .01)

while True: 
    
    weeksofwork = checkint(input("\nHow many weeks of work have you got? "))
    
    week_hours           = []
    week_shift_bonus     = []
    week_base_wage       = []
    week_overtime        = []
    week_overtime_hours  = [] 
    week_sick_pay        = []
    week_gross_pay       = []
    week_net_pay         = []
    week_taxes_deducted  = []
    
    final_shift_bonus    = 0
    final_base_wage      = 0
    final_overtime       = 0
    final_sick_pay       = 0
    final_gross_pay      = 0
    final_net_pay        = 0
    final_taxes_deducted = 0
    
    for week in range(0, weeksofwork):
        if weeksofwork >= 5 or weeksofwork <= 0:
            print(f"Sorry {weeksofwork} is out of range, please use 4 or lower!")
            break 
        
        week_hours.append(checkfloat(input(f"\n\nEnter total hours for week {week + 1} : "), 1))  
        
        if week_hours[week] > 40:
            week_shift_bonus.append(roundvars(1, shift_bonus,week_hours[week]))
            week_base_wage.append(roundvars(1, base_wage, 40))
            week_overtime_hours.append(week_hours[week] - 40)
            week_overtime.append(roundvars(1, week_overtime_hours[week], overtime_wage))

        else:
            week_shift_bonus.append(roundvars(1, shift_bonus,week_hours[week]))
            week_base_wage.append(roundvars(1, base_wage, week_hours[week]))
            week_overtime.append(0)  
            
        week_sick_pay.append(checkfloat(input("Any sick pay? "), base_wage))
        week_gross_pay.append(roundvars(4, week_shift_bonus[week],week_base_wage[week],week_overtime[week],week_sick_pay[week]))
        week_net_pay.append(roundvars(1, week_gross_pay[week], taxes)) 
        week_taxes_deducted.append(round(week_gross_pay[week] - week_net_pay[week], 2))
        
        final_shift_bonus     = roundvars(2, final_shift_bonus    , week_shift_bonus[week])
        final_base_wage       = roundvars(2, final_base_wage      , week_base_wage[week])
        final_overtime        = roundvars(2, final_overtime       , week_overtime[week])
        final_sick_pay        = roundvars(2, final_sick_pay       , week_sick_pay[week])
        final_gross_pay       = roundvars(2, final_gross_pay      , week_gross_pay[week])
        final_net_pay         = roundvars(2, final_net_pay        , week_net_pay[week])
        final_taxes_deducted  = roundvars(2, final_taxes_deducted , week_taxes_deducted[week])
        
        print(f"Shift Bonus: ${week_shift_bonus[week]:,}\
              \nBase Wage: ${week_base_wage[week]:,}\
              \nOvertime Total: ${week_overtime[week]:,}\
              \nSick Pay Total: ${week_sick_pay[week]:,}\
              \nGross Pay: ${week_gross_pay[week]:,}\
              \nNet Pay: ${week_net_pay[week]:,}\
              \nTaxes Deducted: ${week_taxes_deducted[week]:,}\
              \n")

    if final_gross_pay != 0:
        if weeksofwork > 1:
            print(f"Pay Period Shift Bonus: ${final_shift_bonus:,}\
                  \nPay Period Base Total: ${final_base_wage:,}\
                  \nPay Period Overtime: ${final_overtime:,}\
                  \nPay Period Sick Pay Total: ${final_sick_pay:,}\
                  \nGross Pay: ${final_gross_pay:,}\
                  \nNet Pay: ${final_net_pay:,}\
                  \nTaxes Deducted: ${final_taxes_deducted:,}")