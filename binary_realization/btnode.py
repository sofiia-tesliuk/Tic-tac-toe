from basicboard import BasicBoard


class BTnode(BasicBoard):
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
        self.left = None
        self.right = None
        self.points = 0
        # Current state is the last of possible
        self.last_state = False

    def __gt__(self, other):
        if isinstance(other, BTnode):
            return self.points > other.points
        else:
            return self
