from tnode import Tnode
from basicboard import BasicBoard
import random
import copy


class Tree:
    def __init__(self, state, last_move):
        self._root = Tnode(state, last_move)

    def _next_states(self):
        """
        Finds all possible states from root
        """
        def recurse(current_node):
            current_node.points = current_node.analyse_state()
            if current_node.points == 0:
                for cell in current_node.free_cells:
                            next_state = copy.deepcopy(current_node.state)
                            next_move = (not current_node.last_move[0],
                                         cell)
                            i, j = BasicBoard.number_cell_to_state_indexes(cell)
                            next_state[i][j] = next_move[0]
                            new_node = Tnode(next_state, next_move)
                            current_node.next_states.append(new_node)
                            recurse(new_node)
                current_node.points = sum([next_node.points
                                           for next_node in
                                           current_node.next_states])

        recurse(self._root)

    def choose_next_move(self):
        """
        Finds best one state to continue
        :return: best state to continue
        """
        self._next_states()
        if self._root.next_states:
            # Best score in next possible states
            top_score = max(self._root.next_states).points
            # States with best score
            best_states = list(filter(lambda x: x.points == top_score,
                                      self._root.next_states))
            return random.choice(best_states)
        else:
            raise GameOver('No one wins.')


class GameOver(Exception):
    pass
