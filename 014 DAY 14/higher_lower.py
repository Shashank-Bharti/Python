# Import all external modules and data
import os
import random as r
import hl_art
from game_data import data

# Print welcome screen 
print(hl_art.const_logo)
 
a = []
b = []

high_score = 0
    
# make a while loop that keeps running till player keeps guessing right option 
    
on_streak = True

a.append(r.choice(data))
# Define logic()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def compare():
    if a[0]['follower_count'] > b[0]['follower_count'] :
        return 'a'
    else:
        return 'b'
      
while on_streak != False:
       
    b.append(r.choice(data))
    
    if b == a:
        b.append(r.choice(data))
        
    print(f" Compare A : {a[0]['name']}, {a[0]['description']}, {a[0]['country']} \n{hl_art.const_vs}\n Against B : {b[0]['name']}, {b[0]['description']}, {b[0]['country']}")
    
    compared_result = compare()
            
    # Ask user to choose between A or B
    user_choice = input("Who has more follower? Type 'A' or 'B' :" ).lower()
        
    # if statement - if A has > follower_count than B then correct option is B and 1 score is rewarded
    
    if user_choice == compared_result:
        clear_screen()
        high_score += 1
        print(f"You're right! Current Score {high_score}")
        a.clear()
        a += b
        b.clear()
    # exiting loop when user chooses wrong option
    else:
        clear_screen()
        on_streak = False
             
print(f"You're Wrong! Your Highest Score : {high_score}")       

    
    












