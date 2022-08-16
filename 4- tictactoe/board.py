from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class BoardProperties:
    EMPTY_CELL = '-'
    BOARD_COLUMNS = 3
    BOARD_ROWS = 3

    P1_SYMBOL = 'o'
    P2_SYMBOL = 'x'


class BoardChecker:

    def load_board_state(self, board: List, taken_positions: List[Tuple[int, int]]):
        self._board = board
        self._taken_positions = taken_positions

    def check_if_winner(self) -> bool:
        return self._check_rows() or self._check_columns() or\
            self._check_diagnoals()

    def check_if_drawn(self) -> bool:
        return len(self._taken_positions) == \
            BoardProperties.BOARD_COLUMNS * BoardProperties.BOARD_ROWS

    def _check_rows(self) -> bool:
        for row_elements in self._board:
            if(self._check_if_all_elements_equal(row_elements)):
                return True

        return False

    def _check_columns(self) -> bool:

        for column_index in range(BoardProperties.BOARD_COLUMNS):
            column_elements = self._get_column_elements(column_index)

            if(self._check_if_all_elements_equal(column_elements)):
                return True

        return False

    def _get_column_elements(self, column_index: int) -> List[str]:
        marks_in_column = [board_row[column_index]
                           for board_row in self._board]

        return marks_in_column

    def _check_diagnoals(self) -> bool:

        diagonal_1 = [self._board[index][index]
                      for index in range(BoardProperties.BOARD_ROWS)]

        diagonal_2 = [self._board[index][BoardProperties.BOARD_COLUMNS-1-index]
                      for index in range(BoardProperties.BOARD_ROWS)]

        if self._check_if_all_elements_equal(diagonal_1):
            return True
        elif self._check_if_all_elements_equal(diagonal_2):
            return True

        return False

    def _check_if_all_elements_equal(
            self, board_sequence: List[str]) -> bool:
        sequence_items = set(board_sequence)
        return len(sequence_items) == 1 and \
            not BoardProperties.EMPTY_CELL in sequence_items

    def clear_states(self):
        del self._board
        del self._taken_positions


class TicTacToeBoard:

    def __init__(self) -> None:
        self._board_checker = BoardChecker()

    def build_new_board(self) -> None:
        self._board = []
        self._board.append([BoardProperties.EMPTY_CELL]*3)
        self._board.append([BoardProperties.EMPTY_CELL]*3)
        self._board.append([BoardProperties.EMPTY_CELL]*3)
        self._taken_positions: List[Tuple[int, int]] = []

    def print_board(self):
        print('\n   0  1  2')
        for row in range(BoardProperties.BOARD_ROWS):
            print(f'{row}', end='  ')
            for col in range(BoardProperties.BOARD_COLUMNS):
                cell = self._board[row][col]
                print(cell, end='  ')
            print()

    def mark_board(self, row: int, col: int, player_symbol: str) -> bool:
        if self._board[row][col] == BoardProperties.EMPTY_CELL:
            self._board[row][col] = player_symbol
            self._taken_positions.append((row, col))
            self._board_checker.load_board_state(
                self._board, self._taken_positions)
            return True
        return False

    def check_if_winner(self) -> bool:
        return self._board_checker.check_if_winner()

    def check_if_drawn(self) -> bool:
        return self._board_checker.check_if_drawn()

    @ property
    def p1_symbol(self) -> str:
        return BoardProperties.P1_SYMBOL

    @ property
    def p2_symbol(self) -> str:
        return BoardProperties.P2_SYMBOL

    @property
    def taken_positions(self) -> List[Tuple[int, int]]:
        return self._taken_positions


def main():
    board = TicTacToeBoard()
    board.build_new_board()
    board.print_board()
    p1 = board.p1_symbol
    p2 = board.p2_symbol

    board.mark_board(0, 0, p1)
    board.mark_board(0, 1, p1)

    board.mark_board(0, 2, p2)
    board.mark_board(1, 1, p2)
    board.mark_board(2, 0, p2)
    board.print_board()
    have_winner = board.check_if_winner()
    print(f'have winner: {have_winner}')


if __name__ == '__main__':
    main()
