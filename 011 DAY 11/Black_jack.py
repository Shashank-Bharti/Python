
import random as r 
import ascii 

def deal_card(k):
  
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = r.choices(cards,k = k )
    return card
def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

    
user_cards = []
comp_cards = []

consent = input("Do you want to play the game of blackjack? \nType 'y' or 'n' for yes/no:\n ")
comp_cards = deal_card(2)
rev_comp_card = comp_cards[r.randint(0,1)]
if consent == 'y' :
    user_cards = deal_card(2)
    print(f"Your Cards are : {user_cards} & Your score = {sum(user_cards)}")
    print(f"Computer's card {rev_comp_card}")
    loop1 = True
    while calc_score(user_cards) < 21 and loop1 != False:
        action = input("Do you want to Hit or Deal ?\nType 'h' or 'd' for hit/deal\n")
        
        if action == 'h':
            user_cards.append(deal_card(1)[0])
            print(f"Your Cards are : {user_cards} & your score = {sum(user_cards)}")
            print(f"Computer's card is {rev_comp_card}")
            if sum(user_cards) > 21:
                loop1 = False
                print(f"'You got Bust'\nYour score was {sum(user_cards)}")
                print(f"Computer Wins\nComputer's Cards : {comp_cards} & score = {sum(comp_cards)}")
            elif sum(user_cards) == 21:
                print(ascii.bljk)
            
        elif action == 'd':
            if sum(comp_cards) < 17:
                comp_cards.append(deal_card(1)[0])
                print(f"Computer cards: {comp_cards}")
                if sum(comp_cards) > 21:
                    loop1 = False
                    print("'Dealer got Bust'")
                    print(f"You win!\nYour Cards are : {user_cards} & score = {sum(user_cards)}")
                else:    
                    loop1 = False
                    if sum(user_cards) > sum(comp_cards) :
                        
                        print(f"You win!\nYour Cards are : {user_cards} & score = {sum(user_cards)}")
                        print(f"computer's cards = {comp_cards}, score = {sum(comp_cards)}")
                    elif sum(user_cards)< sum(comp_cards):
                        
                        print(f"Computer Wins\nComputer's Cards : {comp_cards} & score = {sum(comp_cards)}")
                        print(f"Your Cards are : {user_cards} & your score = {sum(user_cards)}")
                        
                    elif sum(comp_cards) == sum(user_cards):
                        print("its a draw!")
                
                
            
        
        
        
        
    