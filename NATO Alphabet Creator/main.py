import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

def generate_phonetic():
    user_words = input("Enter a Word: ").upper()

    try:
        output_list = [nato_dict[letter] for letter in user_words]
    except KeyError:
        print("Sorry, only letters in alphabets please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()