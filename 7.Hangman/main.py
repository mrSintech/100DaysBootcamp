import os
import settings
import random
import shapes


class Hangman:
    def __init__(self):
        self.stage = 0
        self.life_remains = settings.MAX_LIFE
        self.word = self.pick_word()
        self.guessed_letters = []
        self.correct_letters = []
        self._word_placeholder = ["_"] * len(self.word)
        self.situation = False

    def pick_word(self):
        """
        pick a random word from file specified in settings
        :return:
        """
        # Import words as tuple
        with open(settings.WORDS_PATH, 'r') as file:
            words = tuple(set(file.read().split()))  # using set to remove duplicates

        return random.choice(words).upper()

    @property
    def word_placeholder(self):
        """
        convert placeholder list to string
        :return:
        """
        return ' '.join(self._word_placeholder)

    def find_letter_index(self, letter):
        """
        search for occurrences of letter in the word picked for game and return them as a list
        :param letter: user inputted letter get from self.update_word_placeholder
        :return: list of indices
        """
        indices = []
        for i, char in enumerate(self.word):
            if char == letter:
                indices.append(i)

        return indices

    def update_word_placeholder(self, letter):
        """
         search for occurrences of letter in the word picked for game and if correct replace placeholders
         with the correct answer
        :param letter: user inputted letter
        :return:
        """
        for i in self.find_letter_index(letter):
            self._word_placeholder[i] = letter

    def clear_screen(self):
        """
        event method clear previous texts on the screen for better UX
        :return:
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_guess_exist(self, letter):
        """
        check if guessed letter is in the picked word and generates corresponding reaction
        :param letter:
        :return:
        """
        if letter in self.guessed_letters:
            print(letter, "is duplicated answer")

        else:
            self.check_guess_correctness(letter)

    def check_guess_correctness(self, letter):
        self.guessed_letters.append(letter)
        if letter in self.word:
            self.correct_answer(letter)

        else:
            self.wrong_answer(letter)

    def correct_answer(self, letter):
        self.update_word_placeholder(letter)
        print(letter, ", you guessed right")
        self.check_user_won()

    def wrong_answer(self, letter):
        self.stage += 1
        self.life_remains -= 1
        print(letter, ", wrong answer")

    def check_user_won(self):
        if "_" not in self._word_placeholder:
            self.situation = True

    def reset(self):
        """
        reset the game and variables
        :return:
        """
        self.clear_screen()
        self.__init__()
        self.start()

    def start(self):
        """
        core method, start and execute the game
        :return:
        """
        # draw logo
        print(shapes.hangman_logo)
        print(f"i'm thinking about a {len(self.word)} letter word")
        print(self.word_placeholder)

        while self.life_remains > 0 and self.situation is False:
            guess_letter = input("Guess a letter in word: ").upper()
            self.clear_screen()
            self.check_guess_exist(guess_letter)
            print(shapes.stages[self.stage])  # draw shape of hangman related with stage of the game
            print(self.word_placeholder)

        # ending
        if self.end():
            self.reset()

    def end(self):
        """
        ask if user want to continue or quit the game
        :return:
        """
        if self.situation:
            print("you won!")

        else:
            print('you lost, try again')

        print("the word was", self.word)
        quit_or_restart = input("for restart hit Enter and to end the game type q: ")
        return False if quit_or_restart == 'q' else True


if __name__ == '__main__':
    Hangman().start()
