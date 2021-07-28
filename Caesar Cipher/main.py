import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

again = True

def caesar(your_text, shift_amount, cipher_direction):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in your_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"Your {cipher_direction}d is {cipher_text}")

print(art.logo)
while(again == True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift %= 26
    caesar(your_text=text, shift_amount=shift, cipher_direction=direction)
    response = input("Do you want to restart the cipher program?\nType 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if response == "yes":
        again = True
    elif response == "no":
        print("GoodBye!")
        again = False
    else:
        print("Wrong Input! Thus exiting.....")
        again = False   