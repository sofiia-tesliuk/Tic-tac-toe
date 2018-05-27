import random
from board import Board


class Tree:
    # ----- Tree node -----
    class Tnode(Board):
        def __init__(self, state, last_move):
            # In state: True -- computer char
            #           False -- player char
            #           None -- empty
            super().__init__(state, last_move)
            self.next_states = []
            self.points = 0

        def __gt__(self, other):
            return self.points > other.points

    # ----- Tree -----
    def __init__(self, root):
        self._root = root

    def _next_states(self):
        def recurse(current_node):
            current_node.points = current_node.analyse_state()
            if current_node.points == 0:
                for cell in current_node.free_cells:
                            next_state = current_node.state
                            next_move = (not current_node.last_move[0],
                                         cell)
                            next_state[(cell - 1) // 3][cell % 3] = next_move[0]
                            new_node = self.Tnode(next_state, next_move)
                            current_node.next_states.append(new_node)
                            recurse(new_node)
                current_node.points = sum([next_node.points
                                           for next_node in
                                           current_node.next_states])

        recurse(self._root)

    def choose_next_move(self):
        self._next_states()
        if self._root.next_states:
            top_score = max(self._root.next_states)
            



class GameOver:
    pass