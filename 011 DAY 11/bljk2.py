import random as r 
import ascii
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return r.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score,comp_score):
    if user_score == comp_score:
        return "Draw 😅"
    elif user_score == 0:
        return "You Won with a Blackjack!"
    elif comp_score == 0:
        return "You Lose , Opponent has Blackjack"
    elif user_score > 21:
        return "You Lose  , You went over"
    elif comp_score > 21:
        return "You win , Opponent went over"
    elif user_score > comp_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_game():
    user_cards = []
    computer_cards = []
    comp_score = -1
    user_score =-1
    is_game_over = False  
    
    print(ascii.welcome)
    print(ascii.bljk)
    print(ascii.shuffle)
    
    for _ in range (2):
        user_cards.append(deal_card())   
        computer_cards.append(deal_card())

    while not is_game_over: 
        user_score = calc_score(user_cards)
        comp_score = calc_score(computer_cards)
        print(f"Your cards : {user_cards} , current score {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score >21:
            is_game_over = True
        else:
            user_hit = input("Type 'y' to get another card and 'n' to pass").lower()
            if user_hit == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
                
    while comp_score != 0 and comp_score< 17: 
        computer_cards.append(deal_card())
        comp_score = calc_score(computer_cards)    
        
    print(f"Your Final cards : {user_cards} ,final score : {user_score}\nOpponent's final cards :{computer_cards} , final score : {comp_score} ")
    print(compare_score(user_score,comp_score))


while input("Do you Want to ply a game of Blackjack Type 'y' or 'n':  ") == 'y':
    
    clear()
    play_game()
  