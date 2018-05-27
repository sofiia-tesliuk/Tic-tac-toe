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
    def __init__(self, state, last_move):
        self._root = self.Tnode(state, last_move)

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
            best_states = list(filter(lambda x: x.points == top_score, self._root.next_states))
            return random.choice(best_states).last_move
        else:
            if self._root.points == 1:
                raise GameOver('Computer wins!')
            elif self._root.points == -1:
                raise GameOver('Player wins!')
            else:
                raise GameOver('No one wins.')


class GameOver(Exception):
    pass
