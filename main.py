import re
def from_word_to_list_of_characters(word):
    list_of_characters = re.findall('[a-z]',word)
    return list_of_characters

def check_character_in_list_of_characters(word,character):
    list_of_indexes = []
    for each_character in range(len(word)):
        if word[each_character] == character:
            list_of_indexes.append(each_character)

    return list_of_indexes


