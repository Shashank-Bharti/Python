#Tip Calculator 
print("Welcome to The Tip Calculator!")
amt = float(input("Enter Your Bill Amount:\n $ "))
tip = float(input("How much tip you would like to give(10,15,20):\n $ "))
num_of_ppl = int(input("How many people are there to Split the bill:\n "))
if num_of_ppl <= 0:
    print(f"Number of persons cannot be {num_of_ppl} ")
else:
    calculation = ((amt + tip) / num_of_ppl)
    print(f"Each person should pay:\n$ {round(calculation,2)} ")
    

    
    



