import os
import art
import random

print("WELCOME TO BLACKJACK")
def deal_card():
    """Deals Random Card from Deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)        

def compare(uscore, cscore):
  if uscore > 21 and cscore > 21:
    return "You went over! You lose!! 😤"
  if uscore == cscore:
    return "Draw!! 🙃"
  elif cscore == 0:
    return "You Lose!! Opponent has Blackjack!! 😱"
  elif uscore == 0:
    return "Win with a Blackjack!! 😎"
  elif uscore > 21:
    return "You went over! You lose!!😭"
  elif cscore > 21:
    return "Opponent went over! You win!!! 😁"
  elif uscore > cscore:
    return "You win!!!😃"
  else:
    return "You lose!!!😤"


def playgame():
    print(art.logo)
    print("---------------------------------------------------------------------------------------------------------")
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards) 
        computer_score = calculate_score(computer_cards) 
        print(f"    Your cards are {user_cards} and Score is: {user_score}")
        print(f"    Dealer's First Card: {computer_cards[0]}")
        print("---------------------------------------------------------------------------------------------------------")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            other_card = input("Do you want to draw another card? 'y' for YES OR 'n' for NO OR any key to exit.: ").lower()
            if other_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0  and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print("---------------------------------------------------------------------------------------------------------")
    print(f"Your final hand: {user_cards} and final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards} and final score: {computer_score}")
    print(compare(user_score, computer_score))
            
still_play = True

while still_play == True:
    do_play = input("Do you want to play BlackJack?\n   'y' for yes 'n' for no: ").lower()
    print("-----*****-----*****-----*****-----*****-----*****-----*****-----*****-----*****-----*****-----*****")
    if do_play == "y":
        playgame()
    elif do_play == "n":
        print("You decided not to Play!!\nBummer!!\nAnyways :) Thank You For Trying Our Game!!!!")
        still_play = False
    else:
        os.system('cls')
        print("-----*****-----*****-----*****-----*****-----*****-----*****-----*****-----*****-----*****-----*****")
        print("Thank You For Trying Our Game!!!!")
        still_play = False