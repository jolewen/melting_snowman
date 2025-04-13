from random import randint

WORD_CATALOGUE = ['alemannia', 'github', 'world','deepthought']

class Word:
    def __init__(self):
        self.word :str = self._random_word_picker()
        self.word_underscores :str = '_' * len(self.word)

    @staticmethod
    def _random_word_picker() -> str:
        return WORD_CATALOGUE[randint(a=0, b=len(WORD_CATALOGUE)-1)]

    def display_partly_solved_word(self, correct_guesses):
        display_word = ''
        for letter in self.word:
            if letter in correct_guesses:
                display_word += letter + " "
            else:
                display_word += "_ "
        return display_word