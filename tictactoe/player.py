from abc import ABCMeta, abstractmethod
from curses.ascii import isdigit
from typing import List, Optional, Tuple
import random


class IPlayer(metaclass=ABCMeta):
    def __init__(self, player_symbol: str) -> None:
        self.__player_symbol = player_symbol

    @abstractmethod
    def pick_board_position(
            self,
            taken_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        pass


class ComputerPlayer(IPlayer):
    def pick_board_position(
            self,
            taken_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        while True:
            position = self._generate_position()
            if position not in taken_positions:
                return position

    def _generate_position(self) -> Tuple[int, int]:
        valid_choices = [0, 1, 2]
        row = random.choice(valid_choices)
        col = random.choice(valid_choices)
        position = (row, col)
        return position


class HumanPlayer(IPlayer):

    def pick_board_position(
            self,
            taken_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        position: Tuple[int, int]
        while True:
            user_input = self._read_user_input()
            coordinates = self._convert_input_to_position(user_input)
            if coordinates:
                if coordinates in taken_positions:
                    print('Coordinates already taken! Take another one')
                else:
                    position = coordinates
                    break

        return position

    def _read_user_input(self) -> str:
        print('Enter the position in the form row,column: ')
        user_input = input()
        return user_input

    def _convert_input_to_position(self, user_input: str) ->\
            Optional[Tuple[int, int]]:
        coordinates = user_input.split(',')
        if self._validate_coordinates(coordinates):
            row, col = coordinates
            return (int(row), int(col))

        return None

    def _validate_coordinates(
            self,
            position: List[str]) -> bool:
        valid_choices = [0, 1, 2]
        if len(position) == 2:
            row, col = position
            if row.isdigit() and col.isdigit():
                if int(row) in valid_choices and int(col) in valid_choices:
                    return True

        return False


def main():
    taken_positions = [(0, 0), (1, 2), (1, 1), (2, 2)]
    human_player = HumanPlayer('x')
    computer_player = ComputerPlayer('o')
    print(computer_player.pick_board_position(taken_positions))
    print(human_player.pick_board_position(taken_positions))


if __name__ == '__main__':
    main()
