class TicTacToeBoard:
    _EMPTY_CELL = '-'
    _BOARD_COLUMNS = 3
    _BOARD_ROWS = 3

    _P1_SYMBOL = 'o'
    _P2_SYMBOL = 'x'

    def __init__(self) -> None:
        self.build_new_board()

    def build_new_board(self) -> None:
        self._board = []
        self._board.append([self._EMPTY_CELL]*3)
        self._board.append([self._EMPTY_CELL]*3)
        self._board.append([self._EMPTY_CELL]*3)

    def print_board(self):
        print('\n  0 1 2')
        for row in range(self._BOARD_ROWS):
            print(f'{row}', end=' ')
            for col in range(self._BOARD_COLUMNS):
                cell = self._board[row][col]
                print(cell, end=' ')
            print()

    def mark_board(self, row: int, col: int, player_symbol: str) -> bool:
        if self._board[row][col] == self._EMPTY_CELL:
            self._board[row][col] = player_symbol
            return True
        return False

    @property
    def p1_symbol(self) -> str:
        return self._P1_SYMBOL

    @property
    def p2_symbol(self) -> str:
        return self._P2_SYMBOL


def main():
    board = TicTacToeBoard()
    board.print_board()
    p1 = board.p1_symbol
    p2 = board.p2_symbol

    board.mark_board(0, 0, p1)
    board.mark_board(0, 2, p1)

    board.mark_board(1, 0, p2)
    board.mark_board(1, 1, p2)
    board.print_board()


if __name__ == '__main__':
    main()
