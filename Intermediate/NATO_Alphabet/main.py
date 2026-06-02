import pandas

#TODO 1. Create a dictionary in this format:
alphabet = pandas.read_csv("Intermediate/NATO_Alphabet/nato_phonetic_alphabet.csv")
alphabets_dict = {code.letter:code.code for (letter,code) in alphabet.iterrows()}
# print(alphabets_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
NATO_list = []
NATO = True
while NATO:
    word = str(input("Enter Word: "))
    # characters = list(word.upper())
    # print(characters)
    # for char in characters:
    #     for (letter,code) in alphabet.iterrows():
    #         if code.letter == char:
    #             NATO_list.append(code.code)
    NATO_list = [alphabets_dict[char] for char in word]
                
    print(NATO_list)
