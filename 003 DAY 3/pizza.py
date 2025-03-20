print("Welcome to Python Pizza Deliveries!")
size = input("What size would you like to have? S / M / L:\n ").upper()
paneer = input("Do you want paneer on your pizaa? Y / N :\n ").upper()
cheese = input("Do you want extra cheese? Y/N:\n ").upper()

bill = 0

#price acc. to size    

if size == "S":
    bill += 150
    
elif size == "M":
    bill += 190
    
elif size == "L":
    bill += 295
       
else:
    print("You Typed Wrong Input")
    
#extra price add if they want paneer    

if paneer == "Y":
    bill += 20 
    
#extra cost if they want cheese     

if cheese == "Y":
    bill += 15       
    
print(f"Your Total Bill is of : ₹{bill}")
print("Thanks for using our Service")
    
    
    

