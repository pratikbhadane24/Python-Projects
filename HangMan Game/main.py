# HangMan Game
import random
import word_list
import art

print(art.logo)

end_game = False
word_list.word_list
chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)
lives = 6

print(art.stages[6])

display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")


while not end_game:
    guess = input("Guess a letter!\n").lower()
    if guess in display:
      print(f"You've already guessed {guess}!")  

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
      print(f"The letter {guess} is not in the word")
      lives -= 1
      if lives == 0:
          end_game = True
          print("You Lose!\nGame Over!!")
          print(f"The word was {chosen_word}")

    print(art.stages[lives])
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_game = True
        print("You Win!!")
 