import os
from copy import copy
from random import randint

from snowman import Snowman

WORD_CATALOGUE = ['alemannia', 'github', 'world','deepthought']
CORRECT_GUESSES = []

class Word:
    def __init__(self):
        self.word :str = self._random_word_picker()
        self.word_underscores :str = '_' * len(self.word)

    @staticmethod
    def _random_word_picker() -> str:
        return WORD_CATALOGUE[randint(a=0, b=len(WORD_CATALOGUE)-1)]


def __demo(word):
    if os.getenv('Demo'):
        print('\nSTARTING DEBUGGING DEMO')
        print(f'I chose the word "{word.word}".')
        print(f'It contains {len(word.word)} "{word.word_underscores}".\n')

def _check_solution_status(word):
    word_guessed = False
    solution = copy(word.word)
    for correct_guess in CORRECT_GUESSES:
        solution = solution.replace(correct_guess, '')
    if not len(solution) >= 1:
        word_guessed = True
    return word_guessed


def add_guess_to_correct_guesses(word, guess) -> bool:
    CORRECT_GUESSES.append(guess)
    word_guessed = _check_solution_status(word)
    return word_guessed


def start_game(word, snowman):
    while not snowman.melted:
        guess = input('Please guess a letter: ').lower()
        if guess in word.word:
            print(f'YESSS! "{guess}" is in the word we are looking for!')
            word_completely_guessed = add_guess_to_correct_guesses(word, guess)
            if word_completely_guessed:
                print(f'CONGRATULATIONS!! You guessed all the letters of "{word.word}" correctly!')
                break
        else:
            print(f'Unfortunately "{guess}" is not correct.')
            snowman.remove_level()


def main() -> None:
    print('Hello from your Snowman game!')
    word = Word()
    snowman = Snowman()
    __demo(word)
    start_game(word, snowman)


if __name__ == '__main__':
    main()