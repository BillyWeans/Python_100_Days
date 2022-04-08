import pandas

#TODO 1. Create a dictionary in this format:
df_nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
#for (index, row) in df_nato_alpha.iterrows():
#    print(row.code)

dict_nato_alpha = {row.letter:row.code for (index, row) in df_nato_alpha.iterrows()}


def generate_nato_name():
    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    user_name = input("What is your name? ").upper()
    try:
        user_nato = [dict_nato_alpha[letter] for letter in user_name]
    except KeyError:
        print("Please use only alphabetic characters")
        generate_nato_name()
    else:
        print(user_nato)


generate_nato_name()
