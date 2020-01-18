from random import choice
from HangmanLetter import HangmanLetter


def set_word(file_name) -> list:
    lines = open(file_name).read().splitlines()
    build_word = []

    for letter in split(choice(lines).upper()):
        build_word.append(HangmanLetter(letter))

    # word = {build_word}

    return build_word


def split(word):
    return (char for char in word)
