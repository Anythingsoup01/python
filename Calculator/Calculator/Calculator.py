
from math import *


def add(num1, num2):
    return float(num1) + float(num2)
    
def subtract(num1, num2):
    return float(num1) - float(num2)
    
def multiply(num1, num2):
    return float(num1) * float(num2)
    
def divide(num1, num2):
    return float(num1) / float(num2)

def modulos(num1, num2):
    return float(num1) % float(num2)
    
def power(num1, num2):
    return float(num1) ** float(num2)
    
def square_root(num1):
    return sqrt(float(num1))

running = True
print("Welcome to the calculator")
while running:
    
    num1 = input("First number: ")
    if num1.lower() == "exit":
        break;
    
    opp = input("Opperation: ")
    if opp.lower() == "exit":
        break;
    elif opp.lower() == "sqrt":
        print(square_root(num1))
    else:
        
        num2 = input("Second number: ")
        
        if num2.lower() == "exit":
            break;
        if opp == "+":
            print(add(num1, num2))
        if opp == "-":
            print(subtract(num1, num2))
        if opp == "*":
            print(multiply(num1, num2))
        if opp == "/":
            print(divide(num1, num2))
        if opp == "%":
            print(modulos(num1, num2))
        if opp == "^":
            print(power(num1, num2))
            
    ans = input("Would you like to continue? Y/n\n").lower()
    if ans == "n":
        running = False

