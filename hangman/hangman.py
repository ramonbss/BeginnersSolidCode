"""
        Hangman game but with SOLID principles applied (at least those I know by the time)
"""
import random
from typing import Set
from words_storage import HangMang_Words


class HangManGame():
    'Hang Man game class'
    _WORDS_LIST_FILE_NAME = 'hangman/words_list.txt'
    _tries = 5

    def __init__(self) -> None:
        self._words_list = HangMang_Words.get_words_from_file(
            self._WORDS_LIST_FILE_NAME
        )

    def start_game(self):
        self.remaining_tries = self._tries
        self.all_attempts: Set[str] = set()
        self.correct_attempts: Set[str] = set()
        self._target_word = self.pick_word()
        self._target_letters = set(self._target_word)

        while self.remaining_tries > 0:
            self.print_game_state()
            user_guess = self.read_user_input()
            if user_guess in self.all_attempts:
                print('You already entered this letter. Try another one.')
                continue
            self.all_attempts.add(user_guess)

            if user_guess in self._target_letters:
                self.correct_attempts.add(user_guess)
            else:
                self.remaining_tries -= 1

            if self._target_letters.difference(self.correct_attempts) == 0:
                print(
                    f'Well done! You correctly found the word: {self._target_word}')
                return

        print(f'The word was: {self._target_word}')
        print('End of the game')

    def pick_word(self) -> str:
        return random.choice(self._words_list)

    def print_game_state(self):
        print('\n\t\tGame status')
        print(f'Tries: {self.remaining_tries}/{self._tries}')
        print(f'Previous attempts: {self.all_attempts}')
        print(
            [letter if letter in self.all_attempts else '-'
             for letter in self._target_word])

    def read_user_input(self) -> str:
        print('Enter a letter and press Enter: ')
        letter = str(input())

        if len(letter) != 1 or not letter.isalpha():
            raise RuntimeError("You entered an invalid input!")

        return letter


def main():
    hang_man = HangManGame()
    hang_man.start_game()


if __name__ == '__main__':
    main()
