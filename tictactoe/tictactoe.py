from board import TicTacToeBoard
from player import HumanPlayer, ComputerPlayer, IPlayer
import random


class TicTacToeGame:
    _GAME_HUMAN_HUMAN = 0
    _GAME_COMPUTER_HUMAN = 1
    _GAME_COMPUTER_COMPUTER = 2

    _P1_NAME = 'Player1'
    _P2_NAME = 'Player2'

    def __init__(self) -> None:
        self._player1: IPlayer
        self._player2: IPlayer
        self._board = TicTacToeBoard()

    def start_game(self) -> None:
        game_type = self._prompt_game_type()
        self._initialize_players(game_type)
        current_player = random.choice([self._player1, self._player2])
        while True:
            self._board.print_board()
            print(f'{current_player.player_name} turn')
            current_player.pick_board_position(
                self._board.taken_positions
            )
            if self._board.check_if_winner():
                print(f'Player {current_player.player_name} won the game!!!')
                break
            if current_player == self._player1:
                current_player = self._player2
            else:
                current_player = self._player1

    def _prompt_game_type(self) -> int:
        while True:
            print('1- Player vs Player\t2- Player vs Computer', end=' ')
            print('3- Computer vs Computer')
            print('Enter the game type: ', end='')
            game_type = int(input())
            if game_type >= 0 and game_type < 3:
                break
        return game_type

    def _initialize_players(self, game_type: int):
        if game_type == self._GAME_HUMAN_HUMAN:
            self._player1 = HumanPlayer(self._board.p1_symbol, self._P1_NAME)
            self._player2 = HumanPlayer(self._board.p2_symbol, self._P2_NAME)
        elif game_type == self._GAME_COMPUTER_HUMAN:
            self._player1 = HumanPlayer(self._board.p1_symbol, self._P1_NAME)
            self._player2 = ComputerPlayer(
                self._board.p2_symbol, self._P2_NAME)
        elif game_type == self._GAME_COMPUTER_COMPUTER:
            self._player1 = ComputerPlayer(
                self._board.p1_symbol, self._P1_NAME)
            self._player2 = ComputerPlayer(
                self._board.p2_symbol, self._P2_NAME)


def main():
    tictactoe = TicTacToeGame()
    tictactoe.start_game()


if __name__ == '__main__':
    main()
