# Rock Paper & Scissors Game
import random

print("Welcome to the Rock , Paper and Scissors Game")


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" 
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
outcomes = [rock, paper, scissor]

'''
PLAYERS TURN

'''
player = (input("Enter your name:\n "))

player_choice = int(input("Enter '0' to choose ROCK , '1' to choose PAPER and '2' to choose SCISSOR: \n "))

print(f"{player} threw :")

if player_choice >= 0 and player_choice <=2:  
   print(outcomes[player_choice])
   
else:
    print('Choose a number b/w 0 - 2 only!')
    


    

'''
COMPUTERS TURN

'''
   
computer = random.randint(0,2)  
print("Computer threw :")

print(outcomes[computer])



''' logic:
rock beats scissor ' 0 < 1
scissor beats paper' 1 > 2
paper beats rock.    2 > 0

'''
if player_choice > 3 and player_choice < 0:
    print("Invalid Input")
    
elif player_choice == 0 and  computer == 2:
    print(f"{player} Wins!")
    
elif computer == 0 and  player_choice == 2:
    print("Computer Wins!")

elif computer > player_choice:
    print("Computer Wins!")
    
elif player_choice > computer:
    print(f"{player} Wins!") 
    
elif player_choice == computer:
    print("It's a Draw")
    

