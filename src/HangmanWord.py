from HangmanLetter import HangmanLetter

from hangman_utils import set_word


class HangmanWord:
    word_file = 'usa.txt'

    def __init__(self):
        self.word: list[HangmanLetter] = set_word(HangmanWord.word_file)
        self.guessed = False

    def get_word_space(self) -> str:
        word = []
        for letter in self.word:
            word.append(letter.display_letter_space())

        return ' '.join(map(str, word))

    def get_word(self) -> str:
        word = []
        for letter in self.word:
            word.append(letter.display_letter())

        return ' '.join(map(str, word))

    def update_word(self, letter) -> bool:
        new_answer = []
        correct_letter = False
        # Go through each letter and set to true
        for hang_letter in self.word:
            if hang_letter.letter == letter:
                hang_letter.show = True
                correct_letter = True
            new_answer.append(hang_letter)
        self.word = new_answer
        return correct_letter

    def count_remaining(self) -> int:
        count = 0
        for letter in self.word:
            if not letter.show:
                count += 1
        return count

    def count_total(self) -> int:
        return len(self.word)

    def set_guessed(self):
        if self.count_remaining() == self.count_total():
            self.guessed = True
