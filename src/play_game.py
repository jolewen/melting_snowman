import os
from copy import copy

from word import Word
from snowman import Snowman


def __demo(word):
    if os.getenv('Demo'):
        print('\nSTARTING DEBUGGING DEMO')
        print(f'I chose the word "{word.word}".')
        print(f'It contains {len(word.word)} "{word.word_underscores}".\n')


class Game:
    def __init__(self):
        self.word = Word()
        self.snowman = Snowman()
        self.correct_guesses = []
        self.wrong_guesses = []
        self.number_wrong_guesses = 0

    def _update_wrong_guesses(self, guess: str) -> bool:
        self.number_wrong_guesses = self.snowman.melted_levels
        if guess not in self.wrong_guesses:
            self.wrong_guesses.append(guess)
            return False
        else:
            return True

    def _update_word_status(self) -> None:
        display_word = self.word.display_partly_solved_word(self.correct_guesses)
        print(display_word)

    def _add_guess_to_correct_guesses(self, guess: str) -> bool:
        self.correct_guesses.append(guess)
        word_guessed = self.check_solution_status()
        return word_guessed

    def check_solution_status(self) -> bool:
        word_guessed = False
        solution = copy(self.word.word)
        for correct_guess in self.correct_guesses:
            solution = solution.replace(correct_guess, '')
        if not len(solution) >= 1:
            word_guessed = True
        return word_guessed

    def get_player_input(self, prompt: str = None) -> str:
        if not prompt:
            prompt = 'Please guess a letter: '
        guess = str(input(prompt)).lower()
        if len(guess) > 1:
            guess = self.get_player_input('Please insert a SINGLE character!: ')
        elif not guess.isalpha():
            guess = self.get_player_input('Please insert a LETTER!: ')
        return guess

    def run_game(self) -> None:
        while not self.snowman.melted:
            guess = self.get_player_input()
            if guess in self.word.word:
                print(f'YESSS! "{guess}" is in the word we are looking for!')
                word_completely_guessed = self._add_guess_to_correct_guesses(guess)
                self._update_word_status()
                if word_completely_guessed:
                    print(f'CONGRATULATIONS!!! You guessed all the letters of "{self.word.word}" correctly!')
                    break
            else:
                print(f'Unfortunately "{guess}" is not correct.')
                is_duplicate = self._update_wrong_guesses(guess)
                if not is_duplicate:
                    self.snowman.remove_level()
                else:
                    print(f'You tried {guess} already.')
                print(f"You've tried {self.wrong_guesses} already")


def main() -> None:
    print('Hello from your Snowman game!')
    game_state = Game()
    __demo(game_state.word)
    game_state.run_game()


if __name__ == '__main__':
    main()