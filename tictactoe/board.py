from typing import List, Tuple


class TicTacToeBoard:
    _EMPTY_CELL = '-'
    _BOARD_COLUMNS = 3
    _BOARD_ROWS = 3

    _P1_SYMBOL = 'o'
    _P2_SYMBOL = 'x'

    def __init__(self) -> None:
        pass

    def build_new_board(self) -> None:
        self._board = []
        self._board.append([self._EMPTY_CELL]*3)
        self._board.append([self._EMPTY_CELL]*3)
        self._board.append([self._EMPTY_CELL]*3)
        self._taken_positions: List[Tuple[int, int]] = []

    def print_board(self):
        print('\n   0  1  2')
        for row in range(self._BOARD_ROWS):
            print(f'{row}', end='  ')
            for col in range(self._BOARD_COLUMNS):
                cell = self._board[row][col]
                print(cell, end='  ')
            print()

    def mark_board(self, row: int, col: int, player_symbol: str) -> bool:
        if self._board[row][col] == self._EMPTY_CELL:
            self._board[row][col] = player_symbol
            self._taken_positions.append((row, col))
            return True
        return False

    def check_if_winner(self) -> bool:
        return self._check_rows() or self._check_columns() or\
            self._check_diagnoals()

    def _check_rows(self) -> bool:
        for row_elements in self._board:
            if(self._check_if_all_elements_equal(row_elements)):
                return True

        return False

    def _check_columns(self) -> bool:

        for column_index in range(self._BOARD_COLUMNS):
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
                      for index in range(self._BOARD_ROWS)]

        diagonal_2 = [self._board[index][self._BOARD_COLUMNS-1-index]
                      for index in range(self._BOARD_ROWS)]

        if self._check_if_all_elements_equal(diagonal_1):
            return True
        elif self._check_if_all_elements_equal(diagonal_2):
            return True

        return False

    def _check_if_all_elements_equal(
            self, board_sequence: List[str]) -> bool:
        sequence_items = set(board_sequence)
        return len(sequence_items) == 1 and \
            not self._EMPTY_CELL in sequence_items

    @ property
    def p1_symbol(self) -> str:
        return self._P1_SYMBOL

    @ property
    def p2_symbol(self) -> str:
        return self._P2_SYMBOL


def main():
    board = TicTacToeBoard()
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
