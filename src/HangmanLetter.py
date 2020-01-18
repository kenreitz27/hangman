class HangmanLetter:

    def __init__(self, letter):
        self.letter = letter
        self.show = False

    def display_letter_space(self) -> str:
        if self.show:
            return self.letter
        else:
            return '_'

    def display_letter(self) -> str:
        return self.letter
