from binary_realization.btree import BTree, GameOver
from basicboard import BasicBoard


class GameBoard(BasicBoard):
    def __init__(self):
        self.state = [[None for i in range(3)] for i in range(3)]
        # Last step: (if computer move, number of cell)
        self.last_move = (None, None)
        self.last_state = False
        self.free_cells = [i + 1 for i in range(9)]

    def player_move(self, cell):
        """
        Set players point in state by cell as position
        :param cell: choose by player cell
        :return: None
        """
        i, j = self.number_cell_to_state_indexes(cell)
        self.state[i][j] = False
        self.free_cells.remove(cell)
        self.last_move = (False, cell)
        # This state is the last possible
        if self.analyse_state() == self.LOSE_POINTS:
            raise GameOver('Player wins!')
        elif self.last_state:
            raise GameOver('No one wins.')

    def computer_move(self):
        """
        Set computer point in state
        Position determines by points of next possible steps
        :return:
        """
        # Tree of possible next steps
        tree = BTree(self.state, self.last_move)
        next_state = tree.choose_next_move()
        current_move = next_state.last_move
        i, j = self.number_cell_to_state_indexes(current_move[1])
        # Set point in state and removes bust cell from free cells
        self.free_cells.remove(current_move[1])
        self.state[i][j] = current_move[0]
        self.last_move = current_move
        # This state is the last possible
        if next_state.last_state:
            if next_state.points == self.WIN_POINTS:
                raise GameOver('Computer wins!')
            else:
                raise GameOver('No one wins.')
