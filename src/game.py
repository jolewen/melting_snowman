import os
from random import randint

WORD_CATALOGUE = ['Alemannia', 'github', 'world','Deepthought']


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


def start_game():
    guess = input('Please guess a letter: ').lower()
    print(guess)


def main() -> None:
    print('Hello from your Snowman game!')
    word = Word()
    __demo(word)
    start_game()


if __name__ == '__main__':
    main()