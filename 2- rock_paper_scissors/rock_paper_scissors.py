import random


class Rock_Paper_Scissors:
    _SELECTIONS = ['r', 'p', 's']
    _LOSES_TO = {
        'r': 'p',
        'p': 's',
        's': 'r'
    }

    def __init__(self) -> None:
        pass

    def play(self):
        user_choice = input("'r' rock, 'p' for paper, 's' for scissors: ")
        computer_choice = random.choice(self._SELECTIONS)
        print(f"User pick '{user_choice}' and computer '{computer_choice}'")
        self.who_wins(user_choice, computer_choice)

    def who_wins(self, user_choice, computer_choice):
        if user_choice == self._LOSES_TO[computer_choice]:
            print('User won!!')
        elif computer_choice == self._LOSES_TO[user_choice]:
            print('Computer won!!')
        else:
            print('tie!')


def main():
    rock_paper_scissors_game = \
        Rock_Paper_Scissors()
    rock_paper_scissors_game.play()


if __name__ == '__main__':
    main()


"""
    Credits:
        Course developed by Kylie Ying. Check out her YouTube channel: https://www.youtube.com/ycubed
"""
