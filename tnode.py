from basicboard import BasicBoard


class Tnode(BasicBoard):
    def __init__(self, state, last_move):
        # In state: True -- computer char
        #           False -- player char
        #           None -- empty
        self.state = state
        self.last_move = last_move
        self.free_cells = []
        for i, row in enumerate(state):
            for j, el in enumerate(row):
                if el is None:
                    self.free_cells.append(i * 3 + j + 1)
        self.next_states = []
        self.points = 0
        # Current state is the last of possible
        self.last_state = False

    def __gt__(self, other):
        return self.points > other.points

