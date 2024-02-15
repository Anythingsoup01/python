from defines import *

base_wage = checkfloat(input("Enter your wage: "), 1)
shift_bonus = checkfloat(input("Enter shift bonus %"), base_wage)
shift_bonus = round2M(shift_bonus, .01)
overtime_wage = base_wage * 1.5
taxes = checkfloat(input("How much is your total tax deductible? %"), .01)

while True: 
    weeksofwork = checkint(input("\nHow many weeks of work have you got? "))

    for week in range(1, weeksofwork + 1):
        if weeksofwork >= 5 or weeksofwork <= 0:
            print(f"Sorry {weeksofwork} is out of range, please use 4 or lower!")
            break
        match week:
            case 1:
                weekone_hours = checkfloat(input("\n\nEnter total hours for week 1: "), 1)
                    
                if weekone_hours > 40:
                    weekone_shift_bonus = round2M(shift_bonus,weekone_hours)
                    weekone_base_wage = round2M(base_wage, 40)
                    weekone_overtime_hours = weekone_hours - 40
                    weekone_overtime = round2M(weekone_overtime_hours, overtime_wage)
                else:
                    weekone_shift_bonus = round2M(shift_bonus,weekone_hours)
                    weekone_base_wage = round2M(base_wage, weekone_hours)
                    weekone_overtime = 0
                    
                weekone_sick_pay = checkfloat(input("Any sick pay? "), base_wage)
                weekone_gross_pay = round4A(weekone_shift_bonus,weekone_base_wage,weekone_overtime,weekone_sick_pay)
                weekone_net_pay = round2M(weekone_gross_pay, taxes)
                print(f"Shift Bonus: {weekone_shift_bonus}\nBase Wage: {weekone_base_wage}\nOvertime Total: {weekone_overtime}\nSick Pay Total: {weekone_sick_pay}\nGross Pay: {weekone_gross_pay}\nNet Pay: {weekone_net_pay}\n")
            case 2:
                weektwo_hours = checkfloat(input("Enter total hours for week 2: "), 1)
                    
                if weektwo_hours > 40:
                    weektwo_shift_bonus = round2M(shift_bonus,weektwo_hours)
                    weektwo_base_wage = round2M(base_wage, 40)
                    weektwo_overtime_hours = weektwo_hours - 40
                    weektwo_overtime = round2M(weektwo_overtime_hours, overtime_wage)
                else:
                    weektwo_shift_bonus = round2M(shift_bonus,weektwo_hours)
                    weektwo_base_wage = round2M(base_wage, weektwo_hours)
                    weektwo_overtime = 0

                weektwo_sick_pay = checkfloat(input("Any sick pay? "), base_wage)
                    
                weektwo_gross_pay = round4A(weektwo_shift_bonus,weektwo_base_wage,weektwo_overtime,weektwo_sick_pay)
                weektwo_net_pay = round2M(weektwo_gross_pay, taxes)
                print(f"Shift Bonus: {weektwo_shift_bonus}\nBase Wage: {weektwo_base_wage}\nOvertime Total: {weektwo_overtime}\nSick Pay Total: {weektwo_sick_pay}\nGross Pay: {weektwo_gross_pay}\nNet Pay: {weektwo_net_pay}\n")
                if weeksofwork == 2:
                    final_shift_bonus = round2A(weekone_shift_bonus,weektwo_shift_bonus)
                    final_base_wage =   round2A(weekone_base_wage, weektwo_base_wage)
                    final_overtime =    round2A(weekone_overtime, weektwo_overtime)
                    final_sick_pay =    round2A(weekone_sick_pay, weektwo_sick_pay)
                    final_gross_pay =   round2A(weekone_gross_pay, weektwo_gross_pay)
                    final_net_pay =     round2A(weekone_net_pay, weektwo_net_pay)
                    print(f"Pay Period Shift Bonus: {final_shift_bonus}\nPay Period Base Total: {final_base_wage}\nPay Period Overtime: {final_overtime}\nPay Period Sick Pay Total: {final_sick_pay }\nGross Pay: {final_gross_pay}\nNet Pay: {final_net_pay}")
            case 3:
                weekthree_hours = checkfloat(input("Enter total hours for week 3: "), 1)
                    
                if weekthree_hours > 40:
                    weekthree_shift_bonus = round2M(shift_bonus,weekthree_hours)
                    weekthree_base_wage = round2M(base_wage, 40)
                    weekthree_overtime_hours = weektwo_hours - 40
                    weekthree_overtime = round2M(weekthree_overtime_hours, overtime_wage)
                else:
                    weekthree_shift_bonus = round2M(shift_bonus,weekthree_hours)
                    weekthree_base_wage = round2M(base_wage, weekthree_hours)
                    weekthree_overtime = 0

                weekthree_sick_pay = checkfloat(input("Any sick pay? "), base_wage)
                    
                weekthree_gross_pay = round4A(weekthree_shift_bonus,weekthree_base_wage,weekthree_overtime,weekthree_sick_pay)
                weekthree_net_pay = round2M(weekthree_gross_pay, taxes)
                print(f"Shift Bonus: {weekthree_shift_bonus}\nBase Wage: {weekthree_base_wage}\nOvertime Total: {weekthree_overtime}\nSick Pay Total: {weekthree_sick_pay}\nGross Pay: {weekthree_gross_pay}\nNet Pay: {weekthree_net_pay}\n")
                if weeksofwork == 3:
                    final_shift_bonus = round3A(weekone_shift_bonus,weektwo_shift_bonus,weekthree_shift_bonus)
                    final_base_wage   = round3A(weekone_base_wage, weektwo_base_wage, weekthree_base_wage)
                    final_overtime    = round3A(weekone_overtime, weektwo_overtime, weekthree_overtime)
                    final_sick_pay    = round3A(weekone_sick_pay, weektwo_sick_pay, weekthree_sick_pay)
                    final_gross_pay   = round3A(weekone_gross_pay, weektwo_gross_pay, weekthree_gross_pay)
                    final_net_pay     = round3A(weekone_net_pay, weektwo_net_pay, weekthree_net_pay)
                    
                    print(f"Pay Period Shift Bonus: {final_shift_bonus}\nPay Period Base Total: {final_base_wage}\nPay Period Overtime: {final_overtime}\nPay Period Sick Pay Total: {final_sick_pay }\nGross Pay: {final_gross_pay}\nNet Pay: {final_net_pay}")
            case 4:
                weekfour_hours = checkfloat(input("Enter total hours for week 4: "), 1)
                    
                if weekfour_hours > 40:
                    weekfour_shift_bonus = round2M(shift_bonus,weekfour_hours)
                    weekfour_base_wage = round2M(base_wage, 40)
                    weekfour_overtime_hours = weektwo_hours - 40
                    weekfour_overtime = round2M(weekfour_overtime_hours, overtime_wage)
                else:
                    weekfour_shift_bonus = round2M(shift_bonus,weekfour_hours)
                    weekfour_base_wage = round2M(base_wage, weekfour_hours)
                    weekfour_overtime = 0

                weekfour_sick_pay = checkfloat(input("Any sick pay? "),1)
                    
                weekfour_gross_pay = round4A(weekfour_shift_bonus,weekfour_base_wage,weekfour_overtime,weekfour_sick_pay)
                weekfour_net_pay = round2M(weekfour_gross_pay, taxes)
                print(f"Shift Bonus: {weektwo_shift_bonus}\nBase Wage: {weekfour_base_wage}\nOvertime Total: {weekfour_overtime}\nSick Pay Total: {weekfour_sick_pay}\nGross Pay: {weekfour_gross_pay}\nNet Pay: {weekfour_net_pay}\n")
                if weeksofwork == 4:
                    final_shift_bonus = round4A(weekone_shift_bonus, weektwo_shift_bonus, weekthree_shift_bonus, weekfour_shift_bonus)
                    final_base_wage   = round4A(weekone_base_wage  , weektwo_base_wage  , weekthree_base_wage  , weekfour_base_wage)
                    final_overtime    = round4A(weekone_overtime   , weektwo_overtime   , weekthree_overtime   , weekfour_overtime)
                    final_sick_pay    = round4A(weekone_sick_pay   , weektwo_sick_pay   , weekthree_sick_pay   , weekfour_sick_pay)
                    final_gross_pay   = round4A(weekone_gross_pay  , weektwo_gross_pay  , weekthree_gross_pay  , weekfour_gross_pay)
                    final_net_pay     = round4A(weekone_net_pay    , weektwo_net_pay    , weekthree_net_pay    , weekfour_net_pay)
                    
                    print(f"Pay Period Shift Bonus: {final_shift_bonus}\nPay Period Base Total: {final_base_wage}\nPay Period Overtime: {final_overtime}\nPay Period Sick Pay Total: {final_sick_pay}\nGross Pay: {final_gross_pay}\nNet Pay: {final_net_pay}")
                