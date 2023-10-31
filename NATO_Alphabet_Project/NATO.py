import pandas as pd
df=pd.read_csv('nato_phonetic_alphabet.csv')
df.to_dict()
nato={row.letter:row.code for (index,row) in df.iterrows() }
game_on = True

while game_on:
    user_input=input("Enter Your Name:").upper()
    if user_input=='EXIT':
        game_on=False
    else:
        result=[nato[letter] for letter in user_input]
        print(result)



