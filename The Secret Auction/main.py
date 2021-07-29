import art
import os
print(art.logo)

print("Welcome to The Secret Auction program.")

all_bids = {}

add_user = True

def find_highest_bidder(bid_records):
    highest_bid = 0
    for bidder in bid_records:
        bid_amount = bid_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with the bid of ${highest_bid}")
    

while (add_user == True):
    name = input("What is your name?\n")
    bid = int(input("What's your Bid?\n$"))
    all_bids[name] = bid
    continuation = input("Are there any other bidders?\nType 'yes' or 'no'\n").lower()
    if continuation == 'yes':
        os.system('cls')
    elif continuation == 'no':
        find_highest_bidder(all_bids)
        add_user = False
    else:
        print("Wrong Input!")
        exit()

