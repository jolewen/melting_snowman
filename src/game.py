import os
from random import randint


WORD_CATALOGUE = {'0': 'Alemannia', '1': 'github', '2': 'world', '3': 'Deepthought'}

def main() -> None:
    print('Hello from your Snowman game!')
    word = Word()
    if os.getenv('Demo'):
        print('\nSTARTING DEBUGGING DEMO')
        print(f'I chose the word "{word.word}".')
        print(f'It contains {len(word.word)} "{word.word_underscores}".')

class Word:
    def __init__(self):
        self.word :str = self._random_word_picker()
        self.word_underscores :str = '_' * len(self.word)

    @staticmethod
    def _random_word_picker() -> str:
        return WORD_CATALOGUE[str(randint(a=0, b=3))]

def word_guesser():
    pass


if __name__ == '__main__':
    main()