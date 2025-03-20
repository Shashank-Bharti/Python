import calculator_art
import pyttsx3

engine = pyttsx3.init()

engine.say ("Welcome to Py calculator")
engine.runAndWait()

print(calculator_art.typo + calculator_art.image)


def addition(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b 

def division(a,b):
    return a / b 

calculation_ends = False 
a = float(input("Enter a number : ")) 
while calculation_ends == False :
     b= float(input("Enter a number : "))
    
     operations = int(input("Choose the operation you want to carry out :\n1. '+'\n2. '-'\n3. '*'\n4. '/'\n-> ")) 
     
     if operations == 1:
        a = addition(a, b)
     elif operations == 2:
        a = subtract(a, b)
     elif operations == 3:
        a = multiply(a, b)
     elif operations == 4:
        a = division(a, b)
     else:
        print("Invalid choice!")
    
     print(f"Result: {a}")  

     calculate_more = input("Want to calculate further? 'y or 'n'\n ")
     
     if calculate_more == 'n':
         calculation_ends = True
         print("Thanks for using PyCalculator :) ")
         
     elif calculate_more == 'y':
        continue
     
     
        
     