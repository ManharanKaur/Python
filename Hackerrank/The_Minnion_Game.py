#The Minnion Game
def minion_game(string):
    vowel_word = 0
    consonent_word = 0
    length = len(string)
    for i,c in enumerate(string):
        sub = length -i
        if c in 'AEIOU':
            vowel_word += sub
        else:
            consonent_word += sub
    print("Stuart",consonent_word) if consonent_word > vowel_word else print("Kevin", vowel_word) if vowel_word > consonent_word else print("Draw")
            
            
if __name__ == '__main__':
    s = input()
    minion_game(s)