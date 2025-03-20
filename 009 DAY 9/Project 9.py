import os
import art

print(art.logo)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


bidders = {}

# def highest_bid(bidding_record):
#     winner = ""
#     max_bid = 0 
#     for bidder in bidding_record :
#         bid_amt = bidding_record[bidder]
#         if bid_amt > max_bid:
#             max_bid = bid_amt
#             winner = bidder
#     print(f"The winner is '{winner}' with amount '$ {max_bid}'")


'''ALTERNATE SOLUTION'''

def highest_bid(bidding_record):
    max_bids = max(bidding_record , key = bidding_record.get)
    print(f"The winner {max_bids} with amount {bidding_record[max_bids]}")

bidding_ends = False

while bidding_ends != True:
    
    bidder_name = input("What is your name: ")
    bidding_amt = int(input("Enter your bid amount: $ "))
    bidders.update({bidder_name:bidding_amt})


    other_bids = input("Are there any other bidders type 'yes' or 'no'\n").lower()
        
    if other_bids == 'no':
        highest_bid(bidders)
        bidding_ends = True

    elif other_bids == 'yes':
        clear() 
