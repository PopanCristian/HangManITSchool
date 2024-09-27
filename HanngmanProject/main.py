# 1.Avem nevoie de o lista de cuvinte
# 2.O functie ce va primi ca parametru lista de cuvinte si va alege random un cuvant pentru joc
# 3.O functie ce va imparti cuvantul in litere. Parementrul functiei este cuvantul luat random
# 4.O functie ce va verifica daca litera introdusa exista in lista de litere a cuvantului. Parametrii :lista de litere. Va returna o lista de indexi pentru
# litera introdusa
# 5.O functie ce va primi ca paranetru un numar de la 0-7. In functie de valoarea primita va construi greseala respectiva
# 6.O lista de mesaje haioase legate de Constanța Popa
from random import random
    #      -----
    #      |   |
    #      |   O
    #      |  /|\
    #      |   |
    #      |  / \
    #      |
#          =========

#1.
list_of_fruits = ["apple", "banana", "mango", "watermelon", "cherry", "grape", "kiwi", "ananas", "orange", "pineapple"]
#2
def choose_random_word(list_of_fruits):
    return random.choice(list_of_fruits).upper()
#5
def draw_hangman(mistakes):
    if mistakes == 0:
        print('''
               -----
               |   |
               |
               |
               |
               |
               |
               =========
        '''
        )
    elif mistakes == 1:
        print('''
               -----
               |   |
               |   O
               |
               |
               |
               |
               =========
        '''
              )
    elif mistakes == 2:
        print('''
               -----
               |   |
               |   O
               |   |
               |
               |
               |
               =========
        '''
              )
    elif mistakes == 3:
        print('''
               -----
               |   |
               |   O
               |   |
               |   |
               |
               |  
               =========
        '''
              )
    elif mistakes == 4:
        print('''
               -----
               |   |
               |   O
               |  /|
               |   |
               |
               |  
               =========
        '''
              )
    elif mistakes == 5:
        print('''
               -----
               |   |
               |   O
               |  /|\\
               |   |
               |
               |  
               =========
        '''
              )
    elif mistakes == 6:
        print('''
               -----
               |   |
               |   O
               |  /|\\
               |   |
               |  /
               |  
               =========
        '''
              )
    elif mistakes == 7:
        print('''
               -----
               |   |
               |   O
               |  /|\\
               |   |
               |  / \\
               |  
               =========
        '''
              )
        print("GAME OVER")

def play_hangman():
    chosen_word = choose_random_word(list_of_fruits)
    mistakes = 0
    max_mistakes = 6

    while mistakes <= max_mistakes:
        draw_hangman(mistakes)

    if mistakes > max_mistakes:
        draw_hangman(mistakes)
        print(f"You lost! The word was: {chosen_word}")


if __name__ == "__main__":
    play_hangman()


