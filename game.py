from board import Board
from tree import GameOver
from colored import fg, bg, attr


class Game:
    CHARS = ['X', 'O']
    TITLE_STYLE = "\n%s%s\t {}\t\t%s" % (fg(55), bg(189), attr(0))
    BOARD_STYLE = '\n%s%s{}%s' % (fg(55), bg(231), attr(0))

    def __init__(self):
        self._player_char = None
        self._computer_char = None
        self._board = None
        self._player_first = None

    def start_new_game(self):
        print(self.TITLE_STYLE.format('Tic-Tac-Toe!'))
        self._player_first = input("Do you want to be the first player? (Y/N): "
                                   ).strip().upper() == 'Y'
        self._player_char = self.CHARS[not self._player_first]
        print('Your char is: {}'.format(self._player_char))
        self._computer_char = self.CHARS[self._player_first]
        self._board = Board(self._player_char, self._computer_char)

    def _input_player_move(self):
        try:
            player_move = int(input('Enter number of cell: '))
            assert player_move in self._board.free_cells
        except (TypeError, ValueError, AssertionError):
            print('Invalid number.')
            return self._input_player_move()

    def _print_board_state(self):
        board_str = str(self._board). \
            replace('True', self._computer_char). \
            replace('False', self._player_char)
        print(self.BOARD_STYLE.format(board_str))

    def run(self):
        self._print_board_state()
        if self._player_first:
            self._board.player_move(self._input_player_move())
        try:
            while True:
                self._board.computer_move()
                self._print_board_state()
                self._board.player_move(self._input_player_move())
                self._print_board_state()
        except GameOver as err:
            self.game_over(err)

    def game_over(self, message):
        if message == 'Computer wins!':
            print('You lose!')
        elif message == 'Player wins!':
            print('Congratulations! You win!')
        else:
            print(message)


def main():
    game = Game()
    game.start_new_game()
    game.run()


if __name__ == "__main__":
    main()
