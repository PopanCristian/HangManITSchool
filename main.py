import re
import random
from time import sleep
def from_word_to_list_of_characters(word):
    """
    Description : transform from a word to list with every character
    :param word: string
    :return: a list that contains each character from the word
    """
    list_of_characters = re.findall('[A-Z]',word)
    return list_of_characters
def check_character_in_list_of_characters(word,character):
    """
    Description : verify if input character exist in the word
    :param word: list
    :param character: string
    :return: A list with indexes for each appearance for the word
    """
    list_of_indexes = []
    for each_character in range(len(word)):
        if word[each_character] == character:
            list_of_indexes.append(each_character)

    return list_of_indexes
def choose_random_word():
    """
    :return: from a list of fruits a random fruit
    """
    list_of_fruits = ["apple", "banana", "mango", "watermelon", "cherry", "grape", "kiwi", "ananas", "orange",
                      "pineapple","apple", "strawberry", "lemon", "grape", "cherry", "watermelon", "raspberry",
              "mango", "peach", "pomegranate", "orange"]
    return random.choice(list_of_fruits).upper()
def hang_the_man(number_mistake):
    """
    Description: Print a specific paint of hang for mistake
    :param number_mistake: Number of mistake
    :return: Print the ilustration of Constanța
    """
    hangman_stages = {
        1: """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        2: """
           ------
           |    |
           |    ☺
           |
           |
           |
        --------
        """,
        3: """
           ------
           |    |
           |    ☺
           |    |
           |
           |
        --------
        """,
        4: """
           ------
           |    |
           |    ☺
           |   /|
           |
           |
        --------
        """,
        5: """
           ------
           |    |
           |    ☺
           |   /|\\
           |
           |
        --------
        """,
        6: """
           ------
           |    |
           |    ☺
           |   /|\\
           |   /
           |
        --------
        """,
        7: """
           ------
           |    |
           |    ☺
           |   /|\\
           |   / \\
           |
        --------
        """
    }

    return hangman_stages[number_mistake]
def generate_underlines(word):
    """

    :param word: list
    :return: a string that contains _ for each character from the word
    """
    len_word = len(word)
    underlines = ''
    while len_word > 0:
        underlines += "_"
        len_word -= 1

    return underlines
def generate_funny_message():
    """
    :return: F☺ck you Constanța !
    """
    funny_msg = ["Whoops!", "Smooth move!", "Epic fail!", "Nice try!", "Mission... failed!", "You had ONE job!",
                 "Next time, maybe?", "Try again, champ!"]

    return random.choice(funny_msg)

if __name__ == "__main__":
    print(f"\n\t\t\t\t\t\t\t\t\t\t\tWelcome to the HangMan game ! \n\nA random word from a LARGE list of fruits has been chosen to guess.\n")
    sleep(2)
    print(f"You need to write down a single letter that you think it's part of the random word.\n")
    print("Try to guess the word and you have 7 choices to save Constanța ")
    sleep(2)
    print(f"Let's start the game !\n")
    word_to_guess = from_word_to_list_of_characters(choose_random_word())
    list_with_underlines = list(generate_underlines(word_to_guess))
    count_mistakes = 0

    while count_mistakes != 7:
        string_with_underlines = ''.join(list_with_underlines)
        print(''.join(list_with_underlines))
        character = input("Type down a letter that you think exist in word : ").upper()# acceptam input de la jucator

        while len(character) != 1:
            character = input("You need to write just a letter: Try again : ") #inputul sa fie decat o litera

        list_of_index_character = check_character_in_list_of_characters(word_to_guess,character)
        if len(list_of_index_character) == 0:#daca lungimea listei de indexi este 0 inseamna ca nu exista aparitii a
            # literei in cuvantul de ghicit
            count_mistakes += 1
            print(hang_the_man(count_mistakes)) #Afisez desenul corespunzator greselii
            print(generate_funny_message()) #totodata si un mesaj hazliu

        else:# daca exista caracterul jucatorului in cuvant
            for index in list_of_index_character:
                list_with_underlines[index] = character #pentru fiecare aparitie a caracterului inlocuim _ cu caracter

        if count_mistakes == 7:
            print("Game over ! Constanța has been hanged up")

        if '_' not in list_with_underlines:
            print("\n\nCongratulation ! You save Constanța you little shit")
            break












