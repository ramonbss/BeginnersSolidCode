from abc import ABCMeta, abstractmethod
from typing import List, Tuple


class IPlayer(metaclass=ABCMeta):
    def __init__(self, player_symbol: str) -> None:
        self.__player_symbol = player_symbol

    @abstractmethod
    def pick_board_position(
            self,
            taken_positions: List[Tuple[int, int]]) -> Tuple[int, int]:
        pass


def main():
    pass


if __name__ == '__main__':
    main()
