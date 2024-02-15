import tkinter
import customtkinter

def roundvars(times = 1, num1 = 0, num2 = 0, num3 = 0, num4 = 0):
    match times:
        case 1: return(round(num1 * num2,2))
        case 2: return(round(num1 + num2,2))
        case 3: return(round(num1 + num2 + num3,2))
        case 4: return(round(num1 + num2 + num3 + num4,2))

def checkfloat(floatvar, by):
        floatvar = floatvar or 0
        floatvar = float(floatvar)
        return roundvars(1, floatvar, by)

def checkint(integer):
        integer = integer or 0
        return int(integer)

def calculate_wage():
    print("Null")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our App Frame
app = customtkinter.CTk()
app.geometry("480x720")
app.title("Wage Calculator")

# UI Elements

insert_wage = customtkinter.CTkLabel(app, text="Insert wage")
insert_wage.pack()
base_wage = tkinter.StringVar()
wage_input = customtkinter.CTkEntry(app, width=250, height=20, textvariable=base_wage)
wage_input.pack()

insert_shift_bonus = customtkinter.CTkLabel(app, text="Shift Bonus")
insert_shift_bonus.pack(anchor="w", padx="100")
shift_bonus = tkinter.StringVar()
shift_bonus_input = customtkinter.CTkEntry(app, width=150, height=20, textvariable=shift_bonus)
shift_bonus_input.pack(anchor="w", padx="60")

insert_taxes = customtkinter.CTkLabel(app, text="Total Taxes Taken Out %")
insert_taxes.pack(anchor="e", padx="100")
taxes = tkinter.StringVar()
taxes_input = customtkinter.CTkEntry(app, width=150, height=20, textvariable=shift_bonus)
taxes_input.pack(anchor="e", padx="60")

calculate = customtkinter.CTkButton(app, text="Calculate", command=calculate_wage)
calculate.pack()


#Run app
app.mainloop()