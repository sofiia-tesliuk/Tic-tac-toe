from binary_realization.btnode import BTnode
from basicboard import BasicBoard
import random
import copy


class BTree:
    def __init__(self, state, last_move):
        self._root = BTnode(state, last_move)

    def _next_states(self):
        """
        Finds all possible states from root
        """
        def get_next_node(previous_node, cell):
            current_state = copy.deepcopy(previous_node.state)
            next_move = (not previous_node.last_move[0],
                         cell)
            i, j = BasicBoard.number_cell_to_state_indexes(cell)
            current_state[i][j] = next_move[0]
            return BTnode(current_state, next_move)

        def recurse(current_node):
            current_node.points = current_node.analyse_state()
            if current_node.points == 0:
                if len(current_node.free_cells) >= 2:
                    left_cell, right_cell = random.sample(current_node.free_cells, 2)
                    left_node = get_next_node(current_node, left_cell)
                    right_node = get_next_node(current_node, right_cell)
                    current_node.left = left_node
                    current_node.right = right_node
                    recurse(left_node)
                    recurse(right_node)
                    current_node.points = left_node.points + right_node.points
                elif len(current_node.free_cells) == 1:
                    left_cell = current_node.free_cells[0]
                    left_node = get_next_node(current_node, left_cell)
                    current_node.left = left_node
                    recurse(left_node)
                    current_node.points = left_node.points

        recurse(self._root)

    def choose_next_move(self):
        """
        Finds best one state to continue
        :return: best state to continue
        """
        self._next_states()
        if self._root.left or self._root.right:
            # Best state in next possible states
            best_state = max(self._root.left, self._root.right)
            return best_state
        else:
            raise GameOver('No one wins.')


class GameOver(Exception):
    pass
