from HangmanWord import HangmanWord
from string import ascii_uppercase


class HangmanGame:
    testing = True
    guess_max = 10

    def __init__(self, name: str):
        self.name = name
        self.answer: HangmanWord = HangmanWord()
        self.guesses = set()
        self.available = sorted(ascii_uppercase)
        self.run = True
        self.guess_count = 0

    def play_text(self):
        i = 0
        while self.run:
            self.display_header()

            letter = self.get_valid_guess()
            if not self.run:
                print("Thanks for playing!....Quiter")
                break
            # At this point we have a valid guess
            # now we need to check if it is a good guess
            self.execute_guess(letter)

            # check if you are the winner
            if self.answer.guessed:
                print('You are the winner!! Congrats!')
                break

            # check if you still have guesses remaining
            if not self.guesses_remaining():
                print('Sorry loser, you are out of guesses!')
                break
            # displays the word
            # self.display_available()
            # print(str(self.answer.count_remaining()) + ' of ' + str(self.answer.count_total()))

        # show word at end
        print("The word is : {}".format(self.answer.get_word()))
        pass

    def get_valid_guess(self) -> str:
        good_guess = False
        while not good_guess:
            # Gets the raw input from the user
            guess = input("Enter a letter between A and Z? (Exit to Quit): ").upper()
            # Check if they are quiting
            if guess == 'EXIT':
                self.run = False
                good_guess = True
                break
            # If guess is in the available set then return the guess
            if guess in self.available:
                return guess
            else:
                print("Invalid guess")

    def display_available(self):
        print("Available: {}".format(self.available))
        print("Used: {}".format(sorted(self.guesses)))
        pass

    def execute_guess(self, letter):
        # only count guess when wrong

        self.available.remove(letter)
        self.guesses.add(letter)
        correct = self.answer.update_word(letter)
        if not correct:
            self.guess_count += 1
        pass

    def display_header(self):
        self.display_available()
        print(self.answer.get_word_space())
        print(str(self.guess_count) + ' of ' + str(HangmanGame.guess_max) + ' used')

        pass

    def guesses_remaining(self) -> bool:
        if self.guess_count < HangmanGame.guess_max:
            return True
        return False




