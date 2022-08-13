import random


class GuessGame:
    def __init__(self) -> None:
        pass

    def start_game(self, guess_low_boundary: int = 1,
                   guess_high_boundary: int = 10):
        self._set_guess_boundaries(
            guess_low_boundary, guess_high_boundary)
        random_number = self.generate_random_number()
        user_guess = 0
        while user_guess != random_number:
            user_guess = self.read_user_guess()

            if user_guess < random_number:
                print('Sorry! Your guess is too low')
            elif user_guess > random_number:
                print('Sorry! Your guess is too high')

        print(f'Congrats! You have guessed the number {user_guess} correctly')

    def _set_guess_boundaries(self, guess_low_boundary: int,
                              guess_high_boundary: int):
        self.guess_low_boundary = guess_low_boundary
        self.guess_high_boundary = guess_high_boundary

    def generate_random_number(self) -> int:
        return random.randint(self.guess_low_boundary,
                              self.guess_high_boundary)

    def read_user_guess(self) -> int:
        user_guess_input = 0
        while True:
            print('Guess a number between ', end='')
            print(
                f'{self.guess_low_boundary} and {self.guess_high_boundary}: ', end='')
            user_guess_input = int(input())
            if self._validate_user_input(user_guess_input):
                break
            else:
                print(f'Please enter a valid value between \
                    {self.guess_low_boundary} and {self.guess_high_boundary}')
        return user_guess_input

    def _validate_user_input(self, user_guess_input: int) -> bool:
        if user_guess_input >= self.guess_low_boundary and\
                user_guess_input <= self.guess_high_boundary:
            return True
        else:
            return False


def main():
    guess_game = GuessGame()
    guess_game.start_game()


if __name__ == '__main__':
    main()


"""
    Credits:
        Course developed by Kylie Ying. Check out her YouTube channel: https://www.youtube.com/ycubed
"""
