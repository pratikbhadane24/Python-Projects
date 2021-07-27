# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

rand_char = [random.choice(letters)for _ in range(nr_letters)]
rand_num = [random.choice(numbers)for _ in range(nr_numbers)]
rand_sym = [random.choice(symbols)for _ in range(nr_symbols)]
chpass = ''
npass = ''
spass = ''
for ch in rand_char:
    chpass += ch
for n in rand_num:
    npass += n
for s in rand_sym:
    spass += s

password = chpass + npass + spass
result = ''.join(random.sample(password ,len(password)))
print(result)