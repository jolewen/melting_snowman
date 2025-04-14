import os
from copy import copy

from word import Word
from snowman import Snowman


def _demo(word):
    """A debugging tool to display the word for control
    :param word: The solution to the game to be printed to stdout
    :return: None
    """
    if os.getenv('demo'):
        print("\nSTARTING DEBUGGING DEMO")
        print(f"I chose the word '{word.word}'.")
        print(f"It contains {len(word.word)} '{word.word_underscores}'.")


class Game:
    def __init__(self):
        self.word = Word()
        self.snowman = Snowman()
        self.correct_guesses = []
        self.wrong_guesses = []
        self.number_wrong_guesses = 0

    def _update_wrong_guesses(self, guess: str) -> None:
        """Update the class variable containing the number of wrong guesses
        and add the most recent guess to the list of those already tried.

        :param guess: The player input as a single char string
        :return: bool whether the guess has been tried before
        """
        self.number_wrong_guesses = self.snowman.melted_levels
        self.wrong_guesses.append(guess)

    def _check_if_guess_is_duplicate(self, guess: str) -> bool:
        """Check whether the guess is already contained in the made guesses"""
        _all_guesses = self.wrong_guesses + self.correct_guesses
        if guess in _all_guesses:
            return True
        else:
            return False

    def _check_solution_status(self) -> bool:
        """Check whether the solution matches the sum of the guesses"""
        word_guessed = False
        solution = copy(self.word.word)
        for correct_guess in self.correct_guesses:
            solution = solution.replace(correct_guess, '')
        if len(solution) == 0:
            word_guessed = True
        return word_guessed

    def _get_solution_status(self, guess: str) -> bool:
        """The player guessed a correct letter.
        Add the guess to the correct guesses.

        :param guess: The player input as a single char string
        :return: bool whether the solution is complete
        """
        word_guessed_completely = self._check_solution_status()
        self.display_current_solution_state()
        return word_guessed_completely

    def display_current_solution_state(self) -> None:
        """Display the solution status to stdout"""
        display_word = self.word.generate_partly_solved_word(self.correct_guesses)
        print(f"Word: {display_word}")

    def get_player_input(self, prompt: str = None) -> str:
        """Prompt the player to input a single letter.

        :param prompt: Mutable prompt for more contextual information to the player
        :return: A single character representing a letter.
        """
        if not prompt:
            prompt = 'Please guess a letter: '
        guess = str(input(f'\n{prompt}')).lower()
        if guess == '.hist':
            self.show_history()
            self.get_player_input()
        elif guess == '.exit' or guess == '.quit':
            exit(1)
        elif len(guess) > 1:
            guess = self.get_player_input('Please insert a SINGLE character!: ')
        elif not guess.isalpha():
            guess = self.get_player_input('Please insert a LETTER!: ')
        elif self._check_if_guess_is_duplicate(guess):
            guess = self.get_player_input(f"You've tried '{guess}' before - Choose again: ")
        return guess

    def run_game(self) -> None:
        """Handle the main game loop by prompting player input
        and deciding whether the guess is correct."""
        self.snowman.show_snowman()
        self.display_current_solution_state()
        while True:
            guess = self.get_player_input()
            if guess in self.word.word:
                print(f"YES! '{guess}' is in the word we are looking for!")
                self.correct_guesses.append(guess)
                self.word.resolve_single_correct_letter(guess)
                self.display_current_solution_state()
                self.snowman.show_snowman()
                if self.word.word_solved:
                    print(f"CONGRATULATIONS!!! You guessed all the letters of '{self.word.word}' correctly!")
                    break
            else:
                print(f"Unfortunately '{guess}' is not correct.")
                self.wrong_guesses.append(guess)
                self.snowman.remove_level()
                if self.snowman.is_melted:
                    break
                self.display_current_solution_state()
                self.snowman.show_snowman()



    def show_history(self):
        print(f"Sofar, you've tried {self.wrong_guesses + self.correct_guesses}")


def main() -> None:
    print("\nHello from your Melting Snowman game!")
    game_state = Game()
    _demo(game_state.word)
    game_state.run_game()


if __name__ == '__main__':
    main()
