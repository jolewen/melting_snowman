import os
from copy import copy

from word import Word
from snowman import Snowman


def __demo(word):
    """A debugging tool to display the word for control
    :param word: The solution to the game to be printed to stdout
    :return: None
    """
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
        """Update the class variable containing the number of wrong guesses
        and add the most recent guess to the list of those already tried.

        :param guess: The player input as a single char string
        :return: bool whether the guess has been tried before
        """
        self.number_wrong_guesses = self.snowman.melted_levels
        if guess not in self.wrong_guesses:
            self.wrong_guesses.append(guess)
            return False
        else:
            return True

    def _check_solution_status(self) -> bool:
        """Check whether the solution matches the sum of the guesses"""
        word_guessed = False
        solution = copy(self.word.word)
        for correct_guess in self.correct_guesses:
            solution = solution.replace(correct_guess, '')
        if len(solution) == 0:
            word_guessed = True
        return word_guessed

    def _update_solution_status(self, guess) -> bool:
        """The player guessed a correct letter.
        Add the guess to the correct guesses.

        :param guess: The player input as a single char string
        :return: bool whether the solution is complete
        """
        self.correct_guesses.append(guess)
        word_guessed_completely = self._check_solution_status()
        self.display_current_solution_state()
        return word_guessed_completely

    def display_current_solution_state(self) -> None:
        """Display the solution status to stdout"""
        display_word = self.word.display_partly_solved_word(self.correct_guesses)
        print(display_word)



    def get_player_input(self, prompt: str = None) -> str:
        """Prompt the player to input a single letter.

        :param prompt: Mutable prompt for more contextual information to the player
        :return: A single character representing a letter.
        """
        if not prompt:
            prompt = 'Please guess a letter: '
        guess = str(input(prompt)).lower()
        if len(guess) > 1:
            guess = self.get_player_input('Please insert a SINGLE character!: ')
        elif not guess.isalpha():
            guess = self.get_player_input('Please insert a LETTER!: ')
        return guess

    def run_game(self) -> None:
        """Handle the main game loop by prompting player input
        and deciding whether the guess is correct."""
        while not self.snowman.is_melted:
            guess = self.get_player_input()
            if guess in self.word.word:
                print(f'YESSS! "{guess}" is in the word we are looking for!')
                word_completely_guessed = self._update_solution_status(guess)
                if word_completely_guessed:
                    print(f'CONGRATULATIONS!!! You guessed all the letters of "{self.word.word}" correctly!')
                    break
            else:
                print(f'Unfortunately "{guess}" is not correct.')
                is_duplicate = self._update_wrong_guesses(guess)
                if not is_duplicate:
                    self.snowman.remove_level()
                    self.display_current_solution_state()
                else:
                    print(f'You tried {guess} already.')
                print(f"Sofar, you've tried {self.wrong_guesses}")


def main() -> None:
    print('Hello from your Melting Snowman game!')
    game_state = Game()
    __demo(game_state.word)
    game_state.run_game()


if __name__ == '__main__':
    main()