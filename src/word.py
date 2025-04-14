from random import randint

WORD_CATALOGUE = ['alemannia', 'github', 'world','deepthought']

class Word:
    def __init__(self, last_word: str = None):
        self.word = self._random_word_picker()
        while self.word == last_word:
            self.word = self._random_word_picker()
        self.word_underscores = '_' * len(self.word)
        self._word_as_list = [l for l in self.word]
        self._word_underscores_as_list = ['_' for j in range(len(self.word))]
        self.word_solved = False

    @staticmethod
    def _random_word_picker() -> str:
        return WORD_CATALOGUE[randint(a=0, b=len(WORD_CATALOGUE)-1)]

    def display_current_solution_state(self, correct_guesses: list) -> None:
        """Display the solution status to stdout"""
        display_word = self.generate_partly_solved_word(correct_guesses)
        print(f"\nWord: {display_word}")

    def generate_partly_solved_word(self, correct_guesses: list) -> str:
        """Generate a visually easier to read version of the (partially) solved word"""
        display_word = ''
        for letter in self.word:
            if letter in correct_guesses:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word

    def resolve_single_correct_letter(self, letter: str) -> None:
        """Strings are immutable,
        so use lists and reconstruct self.word & self.word_underscores."""
        delimiter = ''
        for idx, char in enumerate(self._word_as_list):
            if letter == char:
                self._word_underscores_as_list[idx] = letter

        self.word_underscores = delimiter.join(self._word_underscores_as_list)
        self.word_solved = True if '_' not in self.word_underscores else False
