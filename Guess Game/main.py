import random

EASY_CHOICES = 10
HARD_CHOICES = 5
def check(guess, number, choices):
    if guess < number:
        print("Too Low.")
        return choices-1
    elif guess > number:
        print("Too High.")
        return choices-1

def choose_diff():
    difficulty = input("Choose the difficulty. Type 'easy' OR 'hard': ").lower()
    if difficulty == "easy":
        return EASY_CHOICES
    elif difficulty == "hard":
        return HARD_CHOICES
    else:
        print("Wrong Input!")
        exit()

def play():
    print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 to 100")
    number = random.randint(1, 101)
    turns = choose_diff()
    guess = 0
    while guess != number:
        print(f"Remaining Choices: {turns}")
        guess = int(input("Make a Guess: "))
        turns = check(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses!\nYou Lose!")
            exit()
    print("You Guessed Correct!\nYou Win!")

play()