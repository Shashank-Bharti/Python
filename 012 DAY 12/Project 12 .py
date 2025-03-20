import random as r
   
        

chosen_num = r.randint(1,100)

print(chosen_num)
def choose_gm():
    gm = input("Select a game mode , Type 'easy' or 'hard' for respective modes.\n--> ").lower()
    if gm == 'easy':
        return 10
    elif gm == 'hard':
        return  5

print("I have chosen a number between (1-100).")


attempts = choose_gm()
def logic(c_num,rem_atmp,):
    """_main logic for the game_

    Args:
        chosen_num (var defined for random int): _compares user guess and rand int_
    """
    make_a_guess = int(input("Make a Guess : "))
    
    if make_a_guess > c_num:
        return f" 'Too High'\nYou have {rem_atmp} attempts remaining. "
    
    elif make_a_guess == c_num:
        return "Matched"
    else:
        return f" 'Too Low'\nYou have {rem_atmp} attempts remaining. " 
    

if attempts > 1:
    while logic(chosen_num,attempts) != "Matched":
        attempts -= 1
    print('You won')
                    
else:
    print("You ran out of attempts")
        
        
        
        
    
    