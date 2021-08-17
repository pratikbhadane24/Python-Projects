import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (
    index, row) in nato_data_frame.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_words = input("Enter a Word: ").upper()

output_list = [nato_dict[letter] for letter in user_words]
print(output_list)
