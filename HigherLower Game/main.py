import art
import gamedata
import random

def playgame():
    currentscore = 0
    print(art.logo)
    new_items = True
    obj1 = random.choice(gamedata.data)
    obj2 = random.choice(gamedata.data)

    while new_items == True:
        print(f"Compare A: {obj1['name']}, {obj1['description']}, from {obj1['country']}.")
        followers1 = obj1['follower_count']
        print(art.vs)
        print(f"Compare B: {obj2['name']}, {obj2['description']}, from {obj2['country']}.")
        followers2 = obj2['follower_count']
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == 'a':
            if followers1 > followers2:
                currentscore += 1

                print(f"You are Right!\nCurrent Score: {currentscore}")
            else:
                print(f"Sorry, that's wrong. Final score: {currentscore}")
                new_items = False
        elif choice == 'b':
            if followers2 > followers1:
                currentscore += 1
                print(f"You are Right!\nCurrent Score: {currentscore}")

            else:
                print(f"Sorry, that's wrong. Final score: {currentscore}")
                new_items = False
        else:
            print("Wrong Input!\n")
            exit()
        obj1 = obj2
        obj2 = random.choice(gamedata.data)

playgame()