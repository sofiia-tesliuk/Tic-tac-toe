from gameboard import GameBoard
from binary_realization.btree import GameOver


class Game:
    CHARS = ['X', 'O']

    def __init__(self):
        self._player_char = None
        self._computer_char = None
        self._board = None
        self._player_first = None

    def start_new_game(self):
        """
        Initialisation of the game.
        Prints introduction.
        Asks about being first player.
        """
        # Game introduction
        print('Tic-Tac-Toe!')
        self._player_first = input("Do you want to be the first player? (Y/N): "
                                   ).strip().upper() == 'Y'
        self._player_char = self.CHARS[not self._player_first]
        print('Your char is: {}'.format(self._player_char))
        self._computer_char = self.CHARS[self._player_first]
        self._board = GameBoard()

    def _input_player_move(self):
        """
        :return: valid player input from possible next cells
        """
        try:
            player_move = int(input('Enter number of cell: '))
            assert player_move in self._board.free_cells
            return player_move
        except (TypeError, ValueError, AssertionError):
            print('Invalid number.')
            return self._input_player_move()

    def _print_board_state(self):
        """
        Prints visualisation of board
        """
        # Changes True -- computer_char
        #         False -- player_char
        board_str = str(self._board). \
            replace('True', self._computer_char). \
            replace('False', self._player_char)
        print(board_str)

    def run(self):
        """
        Running game
        """
        self._print_board_state()
        # Player move, if first
        if self._player_first:
            self._board.player_move(self._input_player_move())
            self._print_board_state()
        try:
            while True:
                self._board.computer_move()
                self._print_board_state()
                self._board.player_move(self._input_player_move())
                self._print_board_state()
        except GameOver as err:
            # Print result board
            self._print_board_state()
            self.game_over(str(err))

    def game_over(self, message):
        # End of the game
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
